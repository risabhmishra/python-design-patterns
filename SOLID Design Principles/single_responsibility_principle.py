# Single Responsibility Priciple or Separation of Concerns Principle

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f'{self.count} - {text}')

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return '\n'.join(self.entries)


class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        with open(filename, 'w+') as file:
            file.write(journal.__str__())
            file.close()


if __name__ == '__main__':
    journal = Journal()
    journal.add_entry("entry 1")
    journal.add_entry("entry 2")
    journal.add_entry("entry 3")

    print("Journal Entries : ", journal)

    PersistenceManager.save_to_file(journal, "journal.txt")



