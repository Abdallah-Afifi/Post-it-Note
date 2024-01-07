import os
import pickle

class PostItNote:
    def __init__(self):
        self.notes = []
        self.load_notes()

    def load_notes(self):
        if os.path.exists('post_it_notes.pkl'):
            with open('post_it_notes.pkl', 'rb') as file:
                self.notes = pickle.load(file)

    def save_notes(self):
        with open('post_it_notes.pkl', 'wb') as file:
            pickle.dump(self.notes, file)

    def display_notes(self):
        print("\nYour Post-It Notes:")
        if self.notes:
            for i, note in enumerate(self.notes, start=1):
                print(f"{i}. {note}")
        else:
            print("No notes available.")

    def add_note(self, new_note):
        self.notes.append(new_note)
        self.save_notes()
        print("Note added successfully.")

    def delete_note(self, note_index):
        if 1 <= note_index <= len(self.notes):
            deleted_note = self.notes.pop(note_index - 1)
            self.save_notes()
            print(f"Note deleted: {deleted_note}")
        else:
            print("Invalid note index. Please enter a valid index.")

def main():
    post_it = PostItNote()

    while True:
        print("\nOptions:")
        print("1. Display Notes")
        print("2. Add Note")
        print("3. Delete Note")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            post_it.display_notes()
        elif choice == '2':
            new_note = input("Enter your new note: ")
            post_it.add_note(new_note)
        elif choice == '3':
            post_it.display_notes()
            note_index = int(input("Enter the index of the note to delete: "))
            post_it.delete_note(note_index)
        elif choice == '4':
            print("Exiting the Post-It Note Program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
