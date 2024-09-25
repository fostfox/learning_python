import json

# ANSI escape sequences for colors
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

class UniversityMember:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

class Student(UniversityMember):
    def __init__(self, id, name, age, course, year, gpa):
        super().__init__(id, name, age)
        self.course = course
        self.year = year
        self.gpa = gpa
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'cource': self.course,
            'year': self.year,
            'gpa': self.gpa
        }
        
class Professor(UniversityMember):
    def __init__(self, id, name, age, department, title, salary):
        super().__init__(id, name, age)
        self.department = department
        self.title = title
        self.salary = salary

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'department': self.department,
            'title': self.title,
            'salary': self.salary
        }        

class AdminStaff(UniversityMember):
    def __init__(self, id, name, age, position, years_of_service, salary):
        super().__init__(id, name, age)
        self.position = position
        self.years_of_service = years_of_service
        self.salary = salary
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'position': self.position,
            'years_of_service': self.years_of_service,
            'salary': self.salary
        } 

def cli():
    
    while True:
        print(f"{YELLOW}\nMenu:{RESET}")
        print(f"{YELLOW}1. Add Student{RESET}")
        print(f"{YELLOW}2. Add Professor{RESET}")
        print(f"{YELLOW}3. Add Admin Staff{RESET}")
        print(f"{YELLOW}4. View All Members{RESET}")
        print(f"{YELLOW}5. Remove a member by ID{RESET}")
        print(f"{YELLOW}6. Exit the program (automatically saving data)\n{RESET}")

        choice = input(f"{BLUE}Please choose an option: {RESET}")

        if choice == '1':
            name = input("Name: ")
            age = input("Age: ")
            member_id = input("ID: ")
            with open('university_members.json', 'r') as file:
                    data = json.load(file)
            
            if isinstance(data, list):
                # data = [i for i in data if i.get("id") != id_to_remove]
                
                for i in data:
                    if i.get("id") == member_id:
                        print("Такой ID уже существует, попробуйте снова.")
                        

            else:
                print("Error: the list of data in the JSON-file was expected!")
            
            course = input("Course: ")
            year = input("Year: ")
            gpa = input("GPA: ")
            student = Student(name, age, member_id, course, year, gpa).to_dict()
                                    
            try:
                with open('university_members.json', 'r') as file:
                    data = json.load(file)
            except FileNotFoundError:
                data = []
            except json.decoder.JSONDecodeError:
                print('Incorrect .json file format! Overwrite?')
                answer = input('yes/no: ')
                if answer == 'yes':
                    data = []
                elif answer == 'no':
                    print(f'{RED}\n\nIncorrect .json file format: {RESET}')
                    with open('university_members.json', 'r') as file:
                        content = file.read()
                        print(content)
                    break
                else:
                    print("Exit to the main menu...")
                    continue

            if isinstance(data, list):
                data.append(student)
            else:
                print("Error: the list of data in the JSON-file was expected!")
            
            with open('university_members.json', 'w') as file:
                json.dump(data, file, indent=4)            

        elif choice == '2':
            name = input("Name: ")
            age = input("Age: ")
            member_id = input("ID: ")
            department = input("Department: ")
            title = input("Title: ")
            salary = input("Salary: ")
            professor = Professor(name, age, member_id, department, title, salary).to_dict()
            
            try:
                with open('university_members.json', 'r') as file:
                    data = json.load(file)
            except FileNotFoundError:
                data = []
            except json.decoder.JSONDecodeError:
                print('Incorrect .json file format! Overwrite?')
                answer = input('yes/no: ')
                if answer == 'yes':
                    data = []
                elif answer == 'no':
                    print(f'{RED}\n\nIncorrect .json file format: {RESET}')
                    with open('university_members.json', 'r') as file:
                        content = file.read()
                        print(content)
                    break
                else:
                    print("Exit to the main menu...")
                    continue  
            
            if isinstance(data, list):
                data.append(professor)
            else:
                print("Error: the list of data in the JSON-file was expected!")
            
            with open('university_members.json', 'w') as file:
                json.dump(data, file, indent=4)

        elif choice == '3':
            name = input("Name: ")
            age = input("Age: ")
            member_id = input("ID: ")
            position = input("Position: ")
            years_of_service = input("Years of Service: ")
            salary = input("Salary: ")
            admin_staff = AdminStaff(name, age, member_id, position, years_of_service, salary).to_dict()
            
            try:
                with open('university_members.json', 'r') as file:
                    data = json.load(file)
            except FileNotFoundError:
                data = []
            except json.decoder.JSONDecodeError:
                print('Incorrect .json file format! Overwrite?')
                answer = input('yes/no: ')
                if answer == 'yes':
                    data = []
                elif answer == 'no':
                    print(f'{RED}\n\nIncorrect .json file format: {RESET}')
                    with open('university_members.json', 'r') as file:
                        content = file.read()
                        print(content)
                    break
                else:
                    print("Exit to the main menu...")
                    continue  
            
            if isinstance(data, list):
                data.append(admin_staff)
            else:
                print("Error: the list of data in the JSON-file was expected!")
            
            with open('university_members.json', 'w') as file:
                json.dump(data, file, indent=4)

        elif choice == '4':
            print("\nContents of the file university_members.json: ")
            with open('university_members.json', 'r') as file:
                content = file.read()
                print(content)

        elif choice == '5':
            id_to_remove = input("Enter ID to remove: ")
                        
            with open('university_members.json', 'r') as file:
                    data = json.load(file)
            
            if isinstance(data, list):
                data = [i for i in data if i.get("id") != id_to_remove]
            else:
                print("Error: the list of data in the JSON-file was expected!")
            
            with open('university_members.json', 'w') as file:
                json.dump(data, file, indent=4)
            

        elif choice == '6':
            print(f"\n{GREEN}Exiting the program. Goodbye!{RESET}\n")
            break

        else:
            print(f"\n{RED}Invalid choice, please select again.{RESET}")





if __name__ == "__main__":
    cli()

