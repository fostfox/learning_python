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
        result = []
        for x in self.contacts:
            if self.contacts[x]['name'] == name and self.contacts[x]['surname'] == surname:
                result.append({'name': self.contacts[x]['name'],'surname': self.contacts[x]['surname'], 'phone': self.contacts[x]['phone']})
            
        return result



# 
# Part 2: Implement console support
# 

def _main():
    book = PhoneBook()
    book.add("Alice", "Smith", "123-456-7890")
    book.add("Blice", "Smith", "123-456-7890")
    print(book.contacts)
    print(book.search("Alice", "Smith"))
    print(book.contacts[0]["phone"] == "123-456-7890")


if __name__ == "__main__":
    _main()
