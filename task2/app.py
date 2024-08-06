# 
# Part 1: Implement phone book class
# 

class PhoneBook:
    book_list = []
    
    def __init__(self) -> None:
        pass

    def add(self, name: str) -> None:
        self.book_list.append(name)

    def update(self, name: str, surname: str, phone: str) -> bool:
        """??? (https://peps.python.org/pep-0257/)"""
        pass

    def remove(self, name: str, surname: str) -> int:
        """??? (https://peps.python.org/pep-0257/)"""
        pass

    def search(self, name: str = None, surname: str = None) -> list[dict]:
        """??? (https://peps.python.org/pep-0257/)"""
        return []


PhoneBook_1 = PhoneBook()
PhoneBook_1.add('Bob')
PhoneBook_1.add('Jon')
PhoneBook_1.add('Jack')
print(PhoneBook_1.book_list)


# 
# Part 2: Implement console support
# 

def _main():
    pass


if __name__ == "__main__":
    _main()
