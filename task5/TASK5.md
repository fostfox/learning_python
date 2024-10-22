## Task: University Members Storage System

### Description
Create a Python program that manages the storage of university members (students, professors, and administrative staff). The system should utilize serialization and deserialization to save and load member data from the disk, ensuring persistence across program runs.

### Requirements

1. **Classes for University Members:**
   - Implement a base class `UniversityMember` with attributes common to all members, such as `name`, `age`, and `id`.
   - Create the following subclasses that inherit from `UniversityMember`, each with specific attributes:
     - `Student`: attributes include `course`, `year`, and `gpa`.
     - `Professor`: attributes include `department`, `title`, and `salary`.
     - `AdminStaff`: attributes include `position`, `years_of_service`, and `salary`.

2. **Serialization:**
   - Implement methods to serialize (save) the university members' data to disk using the `JSON` format (use [json module](https://docs.python.org/3/library/json.html))
   - Store the serialized data in a file named `university_members.json`.

3. **Deserialization:**
   - Implement methods to deserialize (load) the data from the `university_members.json` file back into objects.
   - Ensure that the deserialized data can be used as if it was freshly created during the current program session.

4. **Data Management:**
   - Implement functions to add new members, delete members by ID, and list all members.
   - The program should automatically load existing data from the disk when started and save any changes to the disk before exiting.

5. **User Interface:**
   - Provide a simple command-line interface (CLI) that allows the user to:
     - Add a new member (student, professor, or admin staff).
     - View all members.
     - Remove a member by ID.
     - Exit the program (automatically saving data).

6. **Error Handling:**
   - Handle cases where the `university_members.json` file does not exist (e.g., on the first run).
   - Ensure that the program gracefully handles attempts to deserialize data that does not match the expected format.

7. **Testing with `pytest`:**
   - Write tests using the `pytest` framework to validate the functionality of your classes and methods.
   - Tests should cover:
     - Creation of different types of university members.
     - Serialization and deserialization processes.
     - Adding, deleting, and listing members.
     - Error handling scenarios.
   - Ensure that your test suite is comprehensive and runs without errors.

### Example Use Case

1. The user runs the program and is greeted with a menu.
2. The user selects "Add New Member" and inputs data for a new student.
3. The program serializes the data and stores it on the disk.
4. The user exits the program.
5. The next time the program is run, it automatically loads the previous data from the disk, allowing the user to view the student added earlier.

### Deliverables

- A Python script that implements the above functionality.
- The `university_members.json` file should be generated and managed by the script.
- A brief README explaining how to run the program and its features.

### Key Concepts

- **Object-Oriented Programming (OOP):** Utilizing classes and inheritance to model university members.
- **Serialization:** Using the `JSON` format to convert objects into a byte stream for storage.
- **Deserialization:** Loading objects from a byte stream back into memory.
- **File Handling:** Reading from and writing to files for data persistence.
- **Error Handling:** Ensuring robustness in file operations and data integrity.
