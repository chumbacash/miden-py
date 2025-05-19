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
    
    # In a real scenario, we would generate a STARK proof
    # This requires the miden-client binary to be installed and working
    try:
        print("Generating STARK proof (this may take some time)...")
        tx.generate_proof()
        print("Proof generated successfully!")
        
        # Submit transaction
        print("Submitting transaction to the Miden node...")
        tx_id = client.send_transaction(tx)
        print(f"Transaction submitted with ID: {tx_id}")
    except Exception as e:
        print(f"Error: {str(e)}")
        print("Saving transaction locally instead...")
        tx_path = f"tx_{tx.id}.json"
        tx.save(tx_path)
        print(f"Transaction saved to {tx_path}")


if __name__ == "__main__":
    main() 