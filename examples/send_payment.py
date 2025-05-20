#!/usr/bin/env python3
"""
Example: Send a payment
----------------------

This example demonstrates how to send a payment transaction using the Miden Python SDK.
"""

from miden_sdk import MidenClient, Wallet, Transaction, NoteType


def main():
    # Initialize client with testnet endpoint (default)
    client = MidenClient()
    
    # Load a wallet
    # For this example, we assume you've already created a wallet using create_wallet.py
    wallet_path = "wallet.json"
    try:
        wallet = Wallet.load(wallet_path, client=client)
    except FileNotFoundError:
        print(f"Wallet file {wallet_path} not found!")
        print("Please run create_wallet.py first to create a wallet.")
        return
    
    print(f"Loaded wallet with account ID: {wallet.account_id}")
    
    # Set up transaction parameters
    recipient = "0x1234567890abcdef1234567890abcdef12345678"
    amount = 100
    asset_id = "0x01"  # Default asset ID
    
    # Create a payment transaction
    print(f"Creating a payment transaction to send {amount} units of asset {asset_id} to {recipient}")
    tx = Transaction.pay_to_id(
        sender=wallet,
        recipient_address=recipient,
        amount=amount,
        asset_id=asset_id,
        note_type=NoteType.PRIVATE,
        memo="Test payment"
    )
    
    print(f"Transaction created with ID: {tx.id}")
    
    # Skip proof generation since we don't have miden-client installed
    print("Skipping STARK proof generation (requires miden-client binary)")
    
    # Save transaction locally
    tx_path = f"tx_{tx.id}.json"
    tx.save(tx_path)
    print(f"Transaction saved to {tx_path}")
    
    # Print transaction details
    print("\nTransaction details:")
    print(f"  Type: {tx.data['type']}")
    print(f"  Sender: {tx.data['sender']}")
    print(f"  Recipient: {tx.data['recipient']}")
    print(f"  Amount: {tx.data['amount']}")
    print(f"  Asset ID: {tx.data['asset_id']}")
    print(f"  Note Type: {tx.data['note_type']}")
    print(f"  Memo: {tx.data['memo']}")


if __name__ == "__main__":
    main() 