def print_help():
    help_text = """
VaultMan CLI - Commands Overview:

1. add <service> <username> <password>
   - Add or update a username-password pair under the specified service.

2. get <service>
   - List all usernames and passwords stored for a service.

3. delete <service> [--username <username>]
   - Delete a specific username under a service.
   - If --username is omitted, deletes the entire service.

4. list-services
   - Lists all services stored in the vault.

Usage examples:
  python3 cli.py add github myuser mypass
  python3 cli.py get github
  python3 cli.py delete github --username myuser
  python3 cli.py delete github
  python3 cli.py list-services
"""
    print(help_text)

if __name__ == "__main__":
    print_help()
