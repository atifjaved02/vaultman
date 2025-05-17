# VaultMan 🔐

VaultMan is a lightweight, open-source, CLI-based password manager written in Python. It securely stores usernames and passwords for multiple services in an encrypted `.enc` file, and allows retrieval using a master password.

## Features

- Encrypts and stores credentials securely using AES encryption (Fernet)
- Supports multiple usernames per service
- Store, list, retrieve, and delete credentials from the vault
- Easy-to-use CLI interface
- Plain-sight storage via encrypted JSON
- Requires only a master password to decrypt

## Prerequisites

- Python >= 3.8
- `cryptography` library

Install dependencies:
```bash
pip install -r requirements.txt
