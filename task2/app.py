from dataclasses import dataclass


# Part 1: Implement phone book class


@dataclass
class Contact:
    """Contact"""
    name: str
    surname: str
    phone: str

class PhoneBook:
    """"PhoneBook"""
    def __init__(self) -> None:
        self._contacts: list[Contact] = []
        self._index_names: dict[str, list[Contact]] = {}
        self._index_surnames: dict[str, list[Contact]] = {}
        self._index_names_surnames: dict[str, Contact] = {}

    def add(self, name: str, surname: str, phone: str) -> None:
        """Adds a person to the phone book."""
        key = (name, surname)
        if key in self._index_names_surnames:
            return
        
        contact = Contact(name, surname, phone)
        
        self._contacts.append(contact)

        self._index_names_surnames[key] = contact

        self._index_names.setdefault(name, []).append(contact)

        self._index_surnames.setdefault(surname, []).append(contact)

    def update(self, name: str, surname: str, phone: str) -> bool:
        """Updates information about a person in the phone book."""
        result = self._index_names_surnames.get((name, surname))
        if result:
            result.phone = phone
            return True
        return False

    def remove(self, name: str, surname: str) -> int:
        """Removes a person from the phone book."""
        contact_to_delete = self._index_names_surnames.pop((name, surname), None)
        if contact_to_delete:
            self._index_names.pop((name))
            self._index_surnames.pop((surname))
            self._contacts.remove(contact_to_delete)
            return 1
        return 0

    def search(self, name: str = None, surname: str = None) -> list[Contact]:
        """Searches for a person in the phone book."""
        try:
            if name and surname:
                result = self._index_names_surnames[(name, surname)]
                return [result]
            elif name:
                return self._index_names[name]
            elif surname:
                return self._index_surnames[surname]
            return self._contacts
        except KeyError:
            return []


# Part 2: Implement console support


def _main():
    pass


if __name__ == "__main__":
    _main()
