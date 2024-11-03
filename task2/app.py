# Part 1: Implement phone book class
"""Part 1"""


class PhoneBook:
    """"PhoneBook"""
    def __init__(self) -> None:
        self.contacts = []
        self.index_names = {}
        self.index_surnames = {}

    def add(self, name: str, surname: str, phone: str) -> None:
        """Adds a person to the phone book."""
        for contact in self.contacts:
            if contact['name'] == name and contact['surname'] == surname:
                return
        contact = {'name': name, 'surname': surname, 'phone': phone}
        self.contacts.append(contact)

        if name not in self.index_names:
            self.index_names[name] = []
        self.index_names[name].append(contact)

        if surname not in self.index_surnames:
            self.index_surnames[surname] = []
        self.index_surnames[surname].append(contact)

    def update(self, name: str, surname: str, phone: str) -> bool:
        """Updates information about a person in the phone book."""
        for contact in self.contacts:
            if contact['name'] == name and contact['surname'] == surname:
                contact['phone'] = phone
                return True
        return False

    def remove(self, name: str, surname: str) -> int:
        """Removes a person from the phone book."""
        for index, contact in enumerate(self.contacts):
            if contact['name'] == name and contact['surname'] == surname:
                self.contacts.pop(index)
                return 1
        return 0

    def search(self, name: str = None, surname: str = None) -> list[dict]:
        """Searches for a person in the phone book."""
        # if name is None and surname is None:
        #     return self.contacts
        # result = []
        # for contact in self.contacts:
        #     if (contact['name'] == name) or (contact['surname'] == surname):
        #         result.append(contact)
        # return result
        if name and surname:
            return [contact for contact in self.contacts if contact['name'] == name and contact['surname'] == surname]
        elif name:
            return self.index_names[name]
        elif surname:
            return self.index_surnames[surname]
        return self.contacts


# Part 2: Implement console support


def _main():
    pass


if __name__ == "__main__":
    _main()
