import json
import pickle
import os
from colors import RED, GREEN, YELLOW, BLUE, RESET

FILE = "university_members_file"

class UniversityMember:
    """"Basic class for university members."""

    def __init__(self, id: int, name: str, age: str) -> None:
        self.id = id
        self.name = name
        self.age = age


class Student(UniversityMember):
    """The class representing the student."""

    def __init__(self, id: int, name: str, age: str, course: str, year: int, gpa: str) -> None:
        super().__init__(id, name, age)
        self.course = course
        self.year = year
        self.gpa = gpa


class Professor(UniversityMember):
    """The class representing the professors."""

    def __init__(self, id, name, age, department, title, salary):
        super().__init__(id, name, age)
        self.department = department
        self.title = title
        self.salary = salary


class AdminStaff(UniversityMember):
    """The class representing the admin_staffs."""

    def __init__(self, id, name, age, position, years_of_service, salary):
        super().__init__(id, name, age)
        self.position = position
        self.years_of_service = years_of_service
        self.salary = salary


def serialize_json(members: list, file_path: str) -> None:
    """Serializes a list of members into a JSON file."""

    members_json = []

    for member in members:
        if isinstance(member, Student):
            member_json = {
                "type": "student",
                "value":{
                    "id": member.id,
                    "name": member.name,
                    "age": member.age,
                    "course": member.course,
                    "year": member.year,
                    "gpa": member.gpa
                }
            }
            members_json.append(member_json)
        elif isinstance(member, Professor):
            member_json = {
                "type": "professor",
                "value":{
                    "id": member.id,
                    "name": member.name,
                    "age": member.age,
                    "department": member.department,
                    "title": member.title,
                    "salary": member.salary
                }
            }
            members_json.append(member_json)
        elif isinstance(member, AdminStaff):
            member_json = {
                "type": "adminstaff",
                "value":{
                    "id": member.id,
                    "name": member.name,
                    "age": member.age,
                    "position": member.position,
                    "years_of_service": member.years_of_service,
                    "salary": member.salary
                }
            }
            members_json.append(member_json)

    with open(file_path, "w") as f:
        json.dump(members_json, f, indent=4)


def serialize_pkl(members: list, file_path: str) -> None:
    """Serializes a list of members into a pkl file."""

    with open(file_path, "wb") as f:
        pickle.dump(members, f)


def deserialize_json(file_path: str) -> list:
    """Deserializes a list of members from a JSON file."""

    members = []

    try:
        if os.path.exists(file_path):
            with open(file_path) as f:
                members_json = json.load(f)
            for member in members_json:
                value = member["value"]
                if member["type"] == "student":
                    member = Student(value["id"],
                                    value["name"],
                                    value["age"],
                                    value["course"],
                                    value["year"],
                                    value["gpa"])
                    members.append(member)
                elif member["type"] == "professor":
                    member = Professor(value["id"],
                                    value["name"],
                                    value["age"],
                                    value["department"],
                                    value["title"],
                                    value["salary"])
                    members.append(member)
                elif member["type"] == "adminstaff":
                    member = AdminStaff(value["id"],
                                    value["name"],
                                    value["age"],
                                    value["position"],
                                    value["years_of_service"],
                                    value["salary"])
                    members.append(member)
                else:
                    print(f"Unsupported type {member["type"]} with value {member["value"]}")
    except KeyError as err:
        pass
    return members


def deserialize_pkl(file_path: str) -> list:
    """Deserializes a list of members from a pkl file."""

    members = []

    try:
        if os.path.exists(file_path):   
            with open(file_path, 'rb') as f:
                members = pickle.load(f)
    except KeyError as err:
        pass
    return members


def show_members(members: list) -> None:
    """Displays information about members on the screen."""

    if not members:
        print(f"\n{RED}There are no users!{RESET}")
        return

    for index, member in enumerate(members):
        if isinstance(member, Student):
            print(
                f"\n{index}| student | id: {member.id}, name: {member.name}, "
                f"age: {member.age}, course: {member.course}, "
                f"year: {member.year}, gpa: {member.gpa}")
        elif isinstance(member, Professor):
            print(
                f"\n{index}| professor | id: {member.id}, name: {member.name}, "
                f"age: {member.age}, department: {member.department}, "
                f"title: {member.title}, salary: {member.salary}")
        elif isinstance(member, AdminStaff):
            print(
                f"\n{index}| admin_staff | id: {member.id}, name: {member.name}, "
                f"age: {member.age}, position: {member.position}, "
                f"years_of_service: {member.years_of_service}, salary: {member.salary}")


def get_unused_id(members: list) -> int:
    """Generates the next unique ID for the new member."""

    existing_ids = {member.id for member in members}
    next_id = 1
    while next_id in existing_ids:
        next_id += 1
    return next_id


def remove_member_by_id(members: list) -> None:
    """Deletes a member by the given ID."""

    try:
        id_to_remove = int(input("\nEnter ID to remove: "))
        for member in members:
            if member.id == id_to_remove:
                members.remove(member)
                print(f"\n{GREEN}ID {id_to_remove} successfully removed!{RESET}")
                return
        print(f"\n{RED}ID {id_to_remove} not found.{RESET}")
    except ValueError:
        print("You cannot enter symbols!")


def add_member_student(members: list):
    """Adds a new member to the list."""

    id = get_unused_id(members)
    print(f"\nID: {id}")
    name = input("Name: ")
    age = input("Age: ")
    course = input("Course: ")
    year = input("Year: ")
    gpa = input("GPA: ")
    member = Student(id, name, age, course, year, gpa)
    members.append(member)


def add_member_professor(members: list):
    """Adds a new member to the list."""

    id = get_unused_id(members)
    print(f"\nID: {id}")
    name = input("Name: ")
    age = input("Age: ")
    department = input("Department: ")
    title = input("Title: ")
    salary = input("Salary: ")
    member = Professor(id, name, age, department, title, salary)
    members.append(member)


def add_member_adminstaff(members: list):
    """Adds a new member to the list."""

    id = get_unused_id(members)
    print(f"\nID: {id}")
    name = input("Name: ")
    age = input("Age: ")
    position = input("Position: ")
    years_of_service = input("Years of service: ")
    salary = input("Salary: ")
    member = AdminStaff(id, name, age, position, years_of_service, salary)
    members.append(member)


def detect_file_format(file_path: str) -> str:
    if not os.path.exists(file_path):
        return
    with open(file_path, 'rb') as f:
        header = f.read(2)
    if header.startswith(b'\x80'):
        return 'pickle'
    elif header.startswith(b'['):
        return 'json'
    else:
        return

def cli():
    """Launches the command line interface for managing."""
    
    if detect_file_format(FILE) == "json":
        members = deserialize_json(FILE)
    elif detect_file_format(FILE) == "pickle":
        members = deserialize_pkl(FILE)
    else:
        print(f"{YELLOW}Available formats:\n{RESET}")
        print(f"{YELLOW}1. JSON{RESET}")
        print(f"{YELLOW}2. PICKLE\n{RESET}")
        format = input(f"{BLUE}Please choose a format: {RESET}")
        if format == "1":
            members = deserialize_json(FILE)
        elif format == "2":
            members = deserialize_pkl(FILE)

    while True:
        print(f"{YELLOW}\nMenu:{RESET}")
        print(f"{YELLOW}1. Add member{RESET}")
        print(f"{YELLOW}2. Add Professor{RESET}")
        print(f"{YELLOW}3. Add Admin Staff{RESET}")
        print(f"{YELLOW}4. View All Members{RESET}")
        print(f"{YELLOW}5. Remove a member by ID{RESET}")
        print(f"{YELLOW}6. Exit the program. Saving data in the selected format!\n{RESET}")

        choice = input(f"{BLUE}Please choose an option: {RESET}")

        if choice == "1":
            add_member_student(members)
        elif choice == "2":
            add_member_professor(members)
        elif choice == "3":
            add_member_adminstaff(members)
        elif choice == "4":
            show_members(members)
        elif choice == "5":
            remove_member_by_id(members)
        elif choice == "6":
            print(f"{YELLOW}Available formats:\n{RESET}")           
            print(f"{YELLOW}1. JSON{RESET}")
            print(f"{YELLOW}2. PICKLE\n{RESET}")
            format = input(f"{BLUE}Please choose a format: {RESET}")
            if format == "1":
                serialize_json(members, FILE)
            elif format == "2":
                serialize_pkl(members, FILE)
            break
        else:
            print(f"{RED}Invalid choice. Please select a valid option.{RESET}")


if __name__ == "__main__":
    try:
        cli()
    except KeyboardInterrupt:
        print(f"\n{RED}\nProgram interrupted by user. Exiting...{RESET}")
