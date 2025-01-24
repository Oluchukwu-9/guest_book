"""A program that prompts users for their name and stores all of it in a guest_book.txt file."""

from pathlib import Path

name = ''
while name != 'quit':
    user_name = input("Enter your name here (to exit enter (q)uit): ").lower()
    name += f"Name: {user_name.strip()}\n"
    if user_name in ('quit', 'q'):
        break

    path = Path('guest_book.txt')
    path.write_text(name)
