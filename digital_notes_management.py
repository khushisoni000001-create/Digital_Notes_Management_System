from pathlib import Path

FILE_NAME = Path(__file__).with_name("notes.txt")


def load_notes():
    """Load notes from ID|Title|Content lines."""
    notes = []
    if not FILE_NAME.exists():
        return notes

    with FILE_NAME.open("r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split("|", 2)
            if len(parts) == 3:
                note_id, title, content = parts
                notes.append({"id": note_id, "title": title, "content": content})
    return notes


def save_notes(notes):
    """Save all notes in the required ID|Title|Content format."""
    with FILE_NAME.open("w", encoding="utf-8") as file:
        for note in notes:
            file.write(
                f"{note['id']}|{note['title']}|{note['content']}\n"
            )


def next_note_id(notes):
    numbers = []
    for note in notes:
        note_id = note["id"]
        if note_id.startswith("N") and note_id[1:].isdigit():
            numbers.append(int(note_id[1:]))
    return f"N{max(numbers, default=0) + 1}"


def add_note():
    notes = load_notes()
    title = input("Title: ").strip()
    if not title:
        print("Title cannot be empty. Note not saved.")
        return

    content = input("Content: ").strip()
    # The file uses | as a separator, so replace it in user input.
    title = title.replace("|", "/")
    content = content.replace("|", "/")
    note_id = next_note_id(notes)
    notes.append({"id": note_id, "title": title, "content": content})
    save_notes(notes)
    print(f"Note saved. ID: {note_id} | {title}")


def view_notes():
    notes = load_notes()
    if not notes:
        print("No notes found.")
        return

    for note in notes:
        print(f"{note['id']} | {note['title']} | {note['content']}")


def search_notes():
    notes = load_notes()
    keyword = input("Enter search keyword: ").strip().lower()
    matches = [
        note for note in notes
        if keyword in note["title"].lower()
        or keyword in note["content"].lower()
    ]
    if not matches:
        print("No matching notes found.")
        return

    for note in matches:
        print(f"{note['id']} | {note['title']} | {note['content']}")


def edit_note():
    notes = load_notes()
    note_id = input("Enter note ID to edit: ").strip().upper()
    for note in notes:
        if note["id"].upper() == note_id:
            new_content = input("Enter new content: ").strip()
            note["content"] = new_content.replace("|", "/")
            save_notes(notes)
            print(f"Note {note_id} updated.")
            return
    print("Note ID not found. No changes made.")


def delete_note():
    notes = load_notes()
    note_id = input("Enter note ID to delete: ").strip().upper()
    remaining = [note for note in notes if note["id"].upper() != note_id]
    if len(remaining) == len(notes):
        print("Note ID not found. No note deleted.")
        return

    save_notes(remaining)
    print(f"Note {note_id} deleted. Notes left: {len(remaining)}")


def main():
    actions = {
        "1": add_note,
        "2": view_notes,
        "3": search_notes,
        "4": edit_note,
        "5": delete_note,
    }

    while True:
        print("\\n===== DIGITAL NOTES MANAGEMENT SYSTEM =====")
        print("1. Add Note")
        print("2. View All Notes")
        print("3. Search Notes")
        print("4. Edit Note")
        print("5. Delete Note")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "6":
            print("Thank you for using Digital Notes Management System.")
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid option. Please choose 1 to 6.")


if __name__ == "__main__":
    main()
