from university_members_storage_system import Student, Professor, AdminStaff

def test_add_student():
    student = Student(123456789,'Bogdan', 10, 'Computer Science', 2, 5.5)
    result = {
        'id': 123456789,
        'name': 'Bogdan',
        'age': 10,
        'cource': 'Computer Science',
        'year': 2,
        'gpa': 5.5
    }
    assert student.to_dict() == result

def test_add_professor():
    professor = Professor(987654321,'Kali', 15, 'Math', 7, 95000)
    result = {
        'id': 987654321,
        'name': 'Kali',
        'age': 15,
        'department': 'Math',
        'title': 7,
        'salary': 95000
    }
    assert professor.to_dict() == result

def test_add_adminstaff():
    adminstaff = AdminStaff(123123123,'Jon', 15, 'Senior', 3, 45000)
    result = {
        'id': 123123123,
        'name': 'Jon',
        'age': 15,
        'position': 'Senior',
        'years_of_service': 3,
        'salary': 45000
    }
    assert adminstaff.to_dict() == result