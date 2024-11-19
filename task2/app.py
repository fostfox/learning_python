# Part 1: Implement phone book class
"""Part 1"""


class PhoneBook:
    """"PhoneBook"""
    def __init__(self) -> None:
        self.contacts = []
        self.index_names = {}
        self.index_surnames = {}
        self.index_names_surnames = {}

    def add(self, name: str, surname: str, phone: str) -> None:
        """Adds a person to the phone book."""
        key = (name, surname)
        if key in self.index_names_surnames:
            return
        
        contact = {'name': name, 'surname': surname, 'phone': phone}
        self.contacts.append(contact)

        self.index_names_surnames[key] = contact

        if name not in self.index_names:
            self.index_names[name] = []
        self.index_names[name].append(contact)

        if surname not in self.index_surnames:
            self.index_surnames[surname] = []
        self.index_surnames[surname].append(contact)

    def update(self, name: str, surname: str, phone: str) -> bool:
        """Updates information about a person in the phone book."""
        result = self.index_names_surnames.get((name, surname))
        if result:
            result['phone'] = phone
            return True
        return False

    def remove(self, name: str, surname: str) -> int:
        """Removes a person from the phone book."""
        contact_to_delete = self.index_names_surnames.pop((name, surname), None)
        if contact_to_delete:
            self.index_names.pop((name))
            self.index_surnames.pop((surname))
            self.contacts.remove(contact_to_delete)
            return 1
        return 0

    def search(self, name: str = None, surname: str = None) -> list[dict]:
        """Searches for a person in the phone book."""
        try:
            if name and surname:
                result = self.index_names_surnames[(name, surname)]
                return [result]
            elif name:
                return self.index_names[name]
            elif surname:
                return self.index_surnames[surname]
            return self.contacts
        except KeyError:
            return []


# Part 2: Implement console support


def _main():
    pass


if __name__ == "__main__":
    _main()
