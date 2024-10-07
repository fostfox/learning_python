from university_members import Student, Professor, AdminStaff

def test_student_creation():
    student = Student(id=1, name="Bob", age=20, course="Math", year=2, gpa=3.5)
    assert student.id == 1
    assert student.name == "Bob"
    assert student.age == 20
    assert student.course == "Math"
    assert student.year == 2
    assert student.gpa == 3.5

def test_professor_creation():
    professor = Professor(id=2, name="Tom", age=55, department="Prog", title="Senior", salary=250000.1)
    assert professor.id == 2
    assert professor.name == "Tom"
    assert professor.age == 55
    assert professor.department == "Prog"
    assert professor.title == "Senior"
    assert professor.salary == 250000.1

def test_admin_staff_creation():
    admin = AdminStaff(id=3, name="Frank", age=30, position="Manager", years_of_service=10, salary=50000.5)
    assert admin.id == 3
    assert admin.name == "Frank"
    assert admin.age == 30
    assert admin.position == "Manager"
    assert admin.years_of_service == 10
    assert admin.salary == 50000.5
