#!/usr/bin/env python3
"""
Example: Create a new wallet
----------------------------

This example demonstrates how to create a new wallet using the Miden Python SDK.
"""

from miden_sdk import MidenClient, Wallet, AccountType


def main():
    # Initialize client with testnet endpoint (default)
    client = MidenClient()
    
    # Create a private, mutable wallet
    print("Creating a new private, mutable wallet...")
    wallet = client.new_wallet(storage_mode=AccountType.PRIVATE, mutable=True)
    
    # Print wallet information
    print(f"Wallet created successfully!")
    print(f"Account ID: {wallet.account_id}")
    print(f"Storage mode: {wallet.account.storage_mode}")
    print(f"Mutable: {wallet.account.mutable}")
    
    # Save wallet to JSON
    wallet_path = "wallet.json"
    wallet.save(wallet_path)
    print(f"Wallet saved to {wallet_path}")
    
    # Create a second wallet (public, immutable)
    print("\nCreating a new public, immutable wallet...")
    public_wallet = client.new_wallet(storage_mode=AccountType.PUBLIC, mutable=False)
    
    # Print wallet information
    print(f"Wallet created successfully!")
    print(f"Account ID: {public_wallet.account_id}")
    print(f"Storage mode: {public_wallet.account.storage_mode}")
    print(f"Mutable: {public_wallet.account.mutable}")
    
    # Save wallet to JSON
    public_wallet_path = "public_wallet.json"
    public_wallet.save(public_wallet_path)
    print(f"Wallet saved to {public_wallet_path}")
    
    # Load a wallet from file
    print("\nLoading wallet from file...")
    loaded_wallet = Wallet.load(wallet_path, client=client)
    print(f"Loaded wallet with account ID: {loaded_wallet.account_id}")


if __name__ == "__main__":
    main() 