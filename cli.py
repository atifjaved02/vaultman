import argparse
from getpass import getpass
from vaultman.vault import add_entry, get_service, delete_entry, list_services

def main():
    parser = argparse.ArgumentParser(description="VaultMan password manager")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Add command
    add_parser = subparsers.add_parser("add", help="Add/update a username-password under a service")
    add_parser.add_argument("service", help="Service name")
    add_parser.add_argument("username", help="Username")
    add_parser.add_argument("password", help="Password")

    # Get command
    get_parser = subparsers.add_parser("get", help="Get all usernames and passwords under a service")
    get_parser.add_argument("service", help="Service name")

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a username under a service or entire service")
    delete_parser.add_argument("service", help="Service name")
    delete_parser.add_argument("--username", help="Username to delete (omit to delete entire service)", default=None)

    # List-services command
    subparsers.add_parser("list-services", help="List all service names stored")

    args = parser.parse_args()
    master_password = getpass("Master password: ")

    try:
        if args.command == "add":
            add_entry(args.service, args.username, args.password, master_password)
            print(f"✅ Added/Updated username '{args.username}' under service '{args.service}'.")

        elif args.command == "get":
            result = get_service(args.service, master_password)
            if not result:
                print(f"❌ Service '{args.service}' not found.")
                return
            print(f"🔐 Credentials for '{args.service}':")
            for user, pwd in result.items():
                print(f"  - {user} : {pwd}")

        elif args.command == "delete":
            success = delete_entry(args.service, args.username, master_password)
            if success:
                if args.username:
                    print(f"✅ Deleted username '{args.username}' from service '{args.service}'.")
                else:
                    print(f"✅ Deleted entire service '{args.service}'.")
            else:
                print(f"❌ Entry not found to delete.")

        elif args.command == "list-services":
            services = list_services(master_password)
            if not services:
                print("❌ Vault is empty.")
                return
            print("📋 Stored services:")
            for s in services:
                print(f" - {s}")

    except ValueError as ve:
        print(f"❌ {ve}")

if __name__ == "__main__":
    main()