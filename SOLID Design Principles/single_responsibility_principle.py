class Journal:
    """
    Represents a journal with entries.

    Attributes:
        entries (list): A list to store journal entries.
        count (int): An integer representing the count of entries.
    """

    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        """
        Adds a new entry to the journal.

        Args:
            text (str): The text of the entry.
        """
        self.count += 1
        self.entries.append(f'{self.count} - {text}')

    def remove_entry(self, pos):
        """
        Removes an entry from the journal at the specified position.

        Args:
            pos (int): The position of the entry to be removed.
        """
        del self.entries[pos]

    def __str__(self):
        """
        Returns a formatted string representation of the journal.

        Returns:
            str: The formatted string containing all journal entries.
        """
        return '\n'.join(self.entries)


class PersistenceManager:
    """
    Manages persistence of the Journal class by saving it to a file.

    Methods:
        save_to_file(journal, filename): Saves the journal to a file.

    """

    @staticmethod
    def save_to_file(journal, filename):
        """
        Saves the journal entries to a file.

        Args:
            journal (Journal): The Journal instance to be saved.
            filename (str): The name of the file to save the journal entries to.
        """
        with open(filename, 'w+') as file:
            file.write(journal.__str__())


if __name__ == '__main__':
    # Example usage
    journal = Journal()
    journal.add_entry("entry 1")
    journal.add_entry("entry 2")
    journal.add_entry("entry 3")

    print("Journal Entries: ", journal)

    PersistenceManager.save_to_file(journal, "journal.txt")
