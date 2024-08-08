# 
# Part 1: Implement phone book class
# 

class PhoneBook:
    
    def __init__(self) -> None:
        self.contacts = []

    def add(self, name: str, surname: str, phone: str) -> None:
        """??? (https://peps.python.org/pep-0257/)"""
        for contact in self.contacts:
            if contact['name'] == name and contact['surname'] == surname:
                return
        self.contacts.append({'name': name, 'surname': surname, 'phone': phone})

    def update(self, name: str, surname: str, phone: str) -> bool:
        """??? (https://peps.python.org/pep-0257/)"""
        for contact in self.contacts:
            if contact['name'] == name and contact['surname'] == surname:
                contact['phone'] = phone

    def remove(self, name: str, surname: str) -> int:
        """??? (https://peps.python.org/pep-0257/)"""
        for contact in self.contacts:
            if contact['name'] == name and contact['surname'] == surname:
                self.contacts.remove(contact)
            return 1
        return 0

    def search(self, name: str = None, surname: str = None) -> list[dict]:
        """??? (https://peps.python.org/pep-0257/)"""
        if name == None and surname == None:
            return self.contacts
        result = []
        for contact in self.contacts:
            if (contact['name'] == name) or (contact['surname'] == surname):
                result.append(contact)
        return result



# 
# Part 2: Implement console support
# _ - приватная функция

def _main():
    book = PhoneBook()
    book.add("Bob", "Johnson", "098-765-4321")
    book.remove("Bob", "Johnson")
    print(book.contacts)


if __name__ == "__main__":
    _main()
