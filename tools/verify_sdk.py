"""
Test script to verify the Miden Python SDK installation.
"""

import sys
from miden_sdk import MidenClient, Wallet, Account, NoteType, AccountType

def main():
    print(f"Python version: {sys.version}")
    print(f"Successfully imported Miden Python SDK")
    
    # Create a client instance
    client = MidenClient()
    print(f"Client created with endpoint: {client.rpc_endpoint}")
    
    # Try to create a mock account
    account = Account(
        account_id="0x1234567890abcdef1234567890abcdef12345678",
        storage_mode=AccountType.PRIVATE,
        mutable=True
    )
    print(f"Account created with ID: {account.account_id}")
    
    # Try to create a mock wallet
    wallet = Wallet(
        account_id="0x1234567890abcdef1234567890abcdef12345678",
        storage_mode=AccountType.PRIVATE,
        mutable=True
    )
    print(f"Wallet created with ID: {wallet.account_id}")
    print(f"Wallet keypair generated: {wallet.keypair}")
    
    print("\nSDK installation verified successfully!")

if __name__ == "__main__":
    main() 