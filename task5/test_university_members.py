import pytest
import os
import json
import pickle
from unittest.mock import patch
from university_members import (Student, Professor, AdminStaff, serialize_json, deserialize_json, serialize_pkl,
                                deserialize_pkl, remove_member_by_id, add_member_student, add_member_professor,
                                add_member_adminstaff, show_members)


def test_student_creation():
    student = Student(id=1, name="Bob", age=20, course=3, year=2, gpa=3.5)
    assert student.id == 1
    assert student.name == "Bob"
    assert student.age == 20
    assert student.course == 3
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


def test_serialize_json(tmp_path):
    members = [
            Student(id=1, name="Bob", age=20, course=3, year=2, gpa=3.5),
            Professor(id=2, name="Tom", age=55, department="Prog", title="Senior", salary=250000.1),
            AdminStaff(id=3, name="Frank", age=30, position="Manager", years_of_service=10, salary=50000.5)
        ]
    json_file = tmp_path / "test_members.json"
    serialize_json(members, json_file)
    assert json_file.exists()

    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        assert len(data) == 3
        assert data[0]['type'] == 'student'
        assert data[1]['type'] == 'professor'
        assert data[2]['type'] == 'adminstaff'


def test_serialize_json(tmp_path):
    members = [
            Student(id=1, name="Bob", age=20, course=3, year=2, gpa=3.5),
            Professor(id=2, name="Tom", age=55, department="Prog", title="Senior", salary=250000.1),
            AdminStaff(id=3, name="Frank", age=30, position="Manager", years_of_service=10, salary=50000.5)
        ]
    json_file = tmp_path / "test_members.json"
    serialize_json(members, json_file)
    assert json_file.exists()

    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        assert len(data) == 3
        assert data[0]['type'] == 'student'
        assert data[1]['type'] == 'professor'
        assert data[2]['type'] == 'adminstaff'


def test_deserialize_json(tmp_path):
    members = [
            Student(id=1, name="Bob", age=20, course=3, year=2, gpa=3.5),
            Professor(id=2, name="Tom", age=55, department="Prog", title="Senior", salary=250000.1),
            AdminStaff(id=3, name="Frank", age=30, position="Manager", years_of_service=10, salary=50000.5)
        ]
    json_file = tmp_path / "test_members.json"
    serialize_json(members, json_file)
    assert json_file.exists()
    members = deserialize_json(json_file)
    assert isinstance(members[0], Student)
    assert isinstance(members[1], Professor)
    assert isinstance(members[2], AdminStaff)


def test_serialize_pkl(tmp_path):
    members = [
            Student(id=1, name="Bob", age=20, course=3, year=2, gpa=3.5),
            Professor(id=2, name="Tom", age=55, department="Prog", title="Senior", salary=250000.1),
            AdminStaff(id=3, name="Frank", age=30, position="Manager", years_of_service=10, salary=50000.5)
        ]
    pkl_file = tmp_path / "test_members.pkl"
    serialize_pkl(members, pkl_file)
    assert pkl_file.exists()

    with open(pkl_file, 'rb') as f:
        data = pickle.load(f)
        assert len(data) == 3
        assert isinstance(data[0], Student)
        assert isinstance(data[1], Professor)
        assert isinstance(data[2], AdminStaff)


def test_deserialize_pkl(tmp_path):
    members = [
            Student(id=1, name="Bob", age=20, course=3, year=2, gpa=3.5),
            Professor(id=2, name="Tom", age=55, department="Prog", title="Senior", salary=250000.1),
            AdminStaff(id=3, name="Frank", age=30, position="Manager", years_of_service=10, salary=50000.5)
        ]
    pkl_file = tmp_path / "test_members.pkl"
    serialize_pkl(members, pkl_file)
    assert pkl_file.exists()
    members = deserialize_pkl(pkl_file)
    assert isinstance(members[0], Student)
    assert isinstance(members[1], Professor)
    assert isinstance(members[2], AdminStaff)


@patch('builtins.input', return_value='1')
def test_remove_member(mock_input):
    members = [
            Student(id=1, name="Bob", age=20, course=3, year=2, gpa=3.5),
            Professor(id=2, name="Tom", age=55, department="Prog", title="Senior", salary=250000.1),
            AdminStaff(id=3, name="Frank", age=30, position="Manager", years_of_service=10, salary=50000.5)
        ]
    length = len(members)
    remove_member_by_id(members)
    assert len(members) == length - 1


@patch('builtins.input', side_effect=['Kol', '29', '3', '2021', '3.8'])
def test_add_member_student(mock_input):
    members = [
            Student(id=1, name="Bob", age=20, course=3, year=2, gpa=3.5),
            Professor(id=2, name="Tom", age=55, department="Prog", title="Senior", salary=250000.1),
            AdminStaff(id=3, name="Frank", age=30, position="Manager", years_of_service=10, salary=50000.5)
        ]
    add_member_student(members)
    assert len(members) == 4
    new_student = members[-1]
    assert isinstance(new_student, Student)
    assert new_student.id == 4
    assert new_student.name == "Kol"
    assert new_student.age == 29
    assert new_student.course == 3
    assert new_student.year == 2021
    assert new_student.gpa == 3.8


def test_show_members_with_various_members():
    members = [
            Student(id=1, name="Bob", age=20, course=3, year=2, gpa=3.5),
            Professor(id=2, name="Tom", age=55, department="Prog", title="Senior", salary=250000.1),
            AdminStaff(id=3, name="Frank", age=30, position="Manager", years_of_service=10, salary=50000.5)
        ]
    with patch('builtins.print') as mock_print:
        show_members(members)
        
        expected_strings = [
            "\n0| student | id: 1, name: Bob, age: 20, course: 3, year: 2, gpa: 3.5",
            "\n1| professor | id: 2, name: Tom, age: 55, department: Prog, title: Senior, salary: 250000.1",
            "\n2| admin_staff | id: 3, name: Frank, age: 30, position: Manager, years_of_service: 10, salary: 50000.5"
        ]
        
        for expected_string in expected_strings:
            mock_print.assert_any_call(expected_string)


def test_serialize_json_with_invalid_data(tmp_path):
    invalid_members = [
        ('Invalid')
    ]
    json_file = tmp_path / "invalid_members.json"
    
    with pytest.raises(TypeError):
        serialize_json(invalid_members, json_file)
