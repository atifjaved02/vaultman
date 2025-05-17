import json
from .crypto import decrypt_vault, encrypt_vault

VAULT_FILE = "vault.enc"

def load_vault(master_password):
    try:
        with open(VAULT_FILE, "rb") as f:
            encrypted = f.read()
        return decrypt_vault(encrypted, master_password)
    except FileNotFoundError:
        return {}
    except Exception as e:
        raise e

def save_vault(data, master_password):
    encrypted = encrypt_vault(data, master_password)
    with open(VAULT_FILE, "wb") as f:
        f.write(encrypted)

def add_entry(service, username, password, master_password):
    data = load_vault(master_password)
    if service not in data:
        data[service] = {}
    # Update or add username password pair
    data[service][username] = password
    save_vault(data, master_password)

def get_service(service, master_password):
    data = load_vault(master_password)
    if service not in data:
        return None
    return data[service]

def delete_entry(service, username, master_password):
    data = load_vault(master_password)
    if service not in data:
        return False
    if username:
        if username in data[service]:
            del data[service][username]
            if not data[service]:  # if no usernames left, remove service
                del data[service]
        else:
            return False
    else:
        # Delete entire service
        del data[service]
    save_vault(data, master_password)
    return True

def list_services(master_password):
    data = load_vault(master_password)
    return list(data.keys())