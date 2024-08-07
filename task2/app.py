# 
# Part 1: Implement phone book class
# 

class PhoneBook:
    
    def __init__(self) -> None:
        self.contacts = []

    def add(self, name: str, surname: str, phone: str) -> None:
        """??? (https://peps.python.org/pep-0257/)"""
        self.contacts.append({'name': name, 'surname': surname, 'phone': phone})

    def update(self, name: str, surname: str, phone: str) -> bool:
        """??? (https://peps.python.org/pep-0257/)"""
        pass

    def remove(self, name: str, surname: str) -> int:
        """??? (https://peps.python.org/pep-0257/)"""
        pass

    def search(self, name: str = None, surname: str = None) -> list[dict]:
        """??? (https://peps.python.org/pep-0257/)"""
        return []



# 
# Part 2: Implement console support
# 

def _main():
    book = PhoneBook()
    book.add("Bob", "Dilan", "+1234")
    book.add("Jon", "Dilan", "+1234")
    print(book.contacts)


if __name__ == "__main__":
    _main()
