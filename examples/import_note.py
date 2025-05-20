#!/usr/bin/env python3
"""
Example: Import and create notes
-------------------------------

This example demonstrates how to import and create notes using the Miden Python SDK.
"""

from miden_sdk import MidenClient, Note, NoteType


def create_sample_note():
    """Create a sample note and save it to a file."""
    # Create a sample note
    sender = "0xabcdef1234567890abcdef1234567890abcdef12"
    recipient = "0x1234567890abcdef1234567890abcdef12345678"
    
    note = Note.create(
        sender=sender,
        recipient=recipient,
        amount=50,
        asset_id="0x01",
        note_type=NoteType.PRIVATE,
        memo="Sample note for testing"
    )
    
    # Save the note to a file
    note_path = "sample_note.json"
    note.save(note_path)
    
    print(f"Created sample note with ID: {note.id}")
    print(f"Saved note to {note_path}")
    
    return note_path


def main():
    # Initialize client with testnet endpoint (default)
    client = MidenClient()
    
    # First, create a sample note
    print("Creating a sample note...")
    note_path = create_sample_note()
    
    # Import the note
    print("\nImporting note from file...")
    note = Note.import_note(note_path)
    
    # Print note information
    print(f"Note imported successfully!")
    print(f"Note ID: {note.id}")
    print(f"Sender: {note.sender}")
    print(f"Recipient: {note.recipient}")
    print(f"Amount: {note.amount}")
    print(f"Asset ID: {note.asset_id}")
    print(f"Note type: {note.note_type}")
    print(f"Memo: {note.memo}")
    
    # Skip adding note to client's note store as it requires node connectivity
    print("\nSkipping adding note to client's note store (requires node connectivity)")
    
    # Create a new note directly
    print("\nCreating a new note directly...")
    new_note = Note.create(
        sender="0x2468024680246802468024680246802468024680",
        recipient="0x1357913579135791357913579135791357913579",
        amount=75,
        asset_id="0x02",
        note_type=NoteType.PUBLIC,
        memo="Another test note"
    )
    
    # Print new note information
    print(f"Note created successfully!")
    print(f"Note ID: {new_note.id}")
    print(f"Sender: {new_note.sender}")
    print(f"Recipient: {new_note.recipient}")
    print(f"Amount: {new_note.amount}")
    print(f"Asset ID: {new_note.asset_id}")
    print(f"Note type: {new_note.note_type}")
    print(f"Memo: {new_note.memo}")
    
    # Export the new note
    new_note_path = "new_note.json"
    new_note.export_note(new_note_path)
    print(f"Exported new note to {new_note_path}")


if __name__ == "__main__":
    main() 