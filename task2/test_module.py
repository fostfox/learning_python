import task2.app as app

def test_add_contact():
    phone_book = app.PhoneBook()
    phone_book.add("Alice", "Smith", "123-456-7890")
    _contacts = phone_book.search("Alice", "Smith")
    assert len(_contacts) == 1
    assert _contacts[0].phone == "123-456-7890"


def test_add_existing_contact():
    phone_book = app.PhoneBook()
    phone_book.add("Alice", "Smith", "123-456-7890")
    phone_book.add("Alice", "Smith", "000-999-1111")
    _contacts = phone_book.search("Alice", "Smith")
    assert len(_contacts) == 1
    assert _contacts[0].phone == "123-456-7890"


def test_update_contact():
    phone_book = app.PhoneBook()
    phone_book.add("Bob", "Johnson", "098-765-4321")
    phone_book.update("Bob", "Johnson", "444-555-6666")
    _contacts = phone_book.search("Bob", "Johnson")
    assert len(_contacts) == 1
    assert _contacts[0].phone == "444-555-6666"


def test_remove_contact():
    phone_book = app.PhoneBook()
    phone_book.add("Bob", "Johnson", "098-765-4321")
    removed_numbers = phone_book.remove("Bob", "Johnson")
    assert removed_numbers == 1
    result = phone_book.search()
    assert len(result) == 0

def test_remove_misspelled_surname():
    phone_book = app.PhoneBook()
    phone_book.add("Bob", "Johnson", "098-765-4321")
    removed_numbers = phone_book.remove("Bob", "Wrangler")
    assert removed_numbers == 0
    result = phone_book.search()
    assert len(result) == 1


def test_remove_nonexistent_contact():
    phone_book = app.PhoneBook()
    removed_numbers = phone_book.remove("Charlie", "Brown")
    assert removed_numbers == 0


def test_search__contacts_by_name():
    phone_book = app.PhoneBook()
    phone_book.add("Bob", "Dilan", "111-222-3333")
    phone_book.add("Grace", "Wright", "444-555-6666")
    phone_book.add("Bob", "Johnson", "777-888-9999")
    result = phone_book.search(name="Bob")
    assert len(result) == 2


def test_search_same__contacts_by_surname():
    phone_book = app.PhoneBook()
    phone_book.add("Frank", "Smith", "111-222-3333")
    phone_book.add("Grace", "Wright", "444-555-6666")
    phone_book.add("Alice", "Smith", "123-456-7890")
    result = phone_book.search(surname="Smith")
    assert len(result) == 2


def test_search_nonexistent_contact():
    phone_book = app.PhoneBook()
    result = phone_book.search("Eve", "Davis")
    assert len(result) == 0


def test_search__contacts():
    phone_book = app.PhoneBook()
    phone_book.add("Frank", "Wright", "111-222-3333")
    phone_book.add("Grace", "Lee", "444-555-6666")
    result = phone_book.search()
    assert app.Contact("Frank", "Wright", "111-222-3333") in result
    assert app.Contact("Grace", "Lee", "444-555-6666") in result
