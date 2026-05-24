
"""
Laboratory work #4, task 1, variant 24
Program: Student records management with CSV and Pickle serialization.
Author: Student
Version: 1.0
Date: 2026-05-07
"""

import csv
import pickle
import os
from abc import ABC, abstractmethod


class ValidationMixin:
    """Mixin class providing basic validation methods."""
    def validate_nonempty(self, value, field_name):
        if not value or not str(value).strip():
            raise ValueError(f"{field_name} cannot be empty")
        return str(value).strip()

class Student(ValidationMixin):
    """Represents a student with personal and academic info."""
    valid_languages = ['russian', 'english', 'german', 'french', 'spanish']

    def __init__(self, surname, needs_dormitory, work_experience, graduated_from, language):
        self.surname = surname
        self.needs_dormitory = needs_dormitory
        self.work_experience = work_experience
        self.graduated_from = graduated_from
        self.language = language

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        self._surname = self.validate_nonempty(value, "Surname")

    @property
    def needs_dormitory(self):
        return self._needs_dormitory

    @needs_dormitory.setter
    def needs_dormitory(self, value):
        self._needs_dormitory = bool(value)

    @property
    def work_experience(self):
        return self._work_experience

    @work_experience.setter
    def work_experience(self, value):
        try:
            exp = int(value)
            if exp < 0:
                raise ValueError("Work experience cannot be negative")
            self._work_experience = exp
        except ValueError:
            raise ValueError("Work experience must be an integer")

    @property
    def graduated_from(self):
        return self._graduated_from

    @graduated_from.setter
    def graduated_from(self, value):
        self._graduated_from = self.validate_nonempty(value, "Graduated from")

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        lang = value.strip().lower()
        if lang not in self.valid_languages:
            raise ValueError(f"Invalid language. Allowed: {', '.join(self.valid_languages)}")
        self._language = lang

    #svoistvo
    @property
    def work_experience_months(self):
        """Return work experience in months."""
        return self._work_experience * 12
    
    #magic
    def __str__(self):
        dorm = "Yes" if self.needs_dormitory else "No"
        return f"{self.surname} | Dorm: {dorm} | Exp: {self.work_experience} yrs | Graduated: {self.graduated_from} | Language: {self.language}"

    def __repr__(self):
        return f"Student('{self.surname}', {self.needs_dormitory}, {self.work_experience}, '{self.graduated_from}', '{self.language}')"

    #conversion to/from dict for serialization
    def to_dict(self):
        return {
            'surname': self.surname,
            'needs_dormitory': self.needs_dormitory,
            'work_experience': self.work_experience,
            'graduated_from': self.graduated_from,
            'language': self.language
        }

    # Vmesto peregruza init tak prinyato delat
    @classmethod
    def from_dict(cls, data):
        return cls(data['surname'], data['needs_dormitory'], data['work_experience'], data['graduated_from'], data['language'])


# Serialization classes with polymorphism 
class Serializer(ABC):
    """Abstract base class for all serializers."""
    @abstractmethod
    def save(self, students, filename):
        pass

    @abstractmethod
    def load(self, filename):
        pass

class CsvSerializer(Serializer):
    """CSV format serializer."""
    def save(self, students, filename):
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            if students:
                fieldnames = students[0].to_dict().keys()
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                for s in students:
                    writer.writerow(s.to_dict())
            else:
                writer = csv.DictWriter(f, fieldnames=['surname', 'needs_dormitory', 'work_experience', 'graduated_from', 'language'])
                writer.writeheader()

    def load(self, filename):
        students = []
        if not os.path.exists(filename):
            return students
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['needs_dormitory'] = row['needs_dormitory'].lower() == 'true'
                row['work_experience'] = int(row['work_experience'])
                students.append(Student.from_dict(row))
        return students

class PickleSerializer(Serializer):
    """Pickle (binary) format serializer."""
    def save(self, students, filename):
        with open(filename, 'wb') as f:
            pickle.dump(students, f)

    def load(self, filename):
        if not os.path.exists(filename):
            return []
        with open(filename, 'rb') as f:
            return pickle.load(f)


#Student manager
class StudentManager:
    """Manages student collection: load, save, queries, statistics."""
    def __init__(self, serializer, filename):
        self.serializer = serializer
        self.filename = filename
        self.students = self.load()

    def load(self):
        return self.serializer.load(self.filename)

    def save(self):
        self.serializer.save(self.students, self.filename)

    def add_student(self, student):
        self.students.append(student)
        self.save()

    def remove_student(self, surname):
        self.students = [s for s in self.students if s.surname.lower() != surname.lower()]
        self.save()

    def find_by_surname(self, surname):
        return [s for s in self.students if s.surname.lower() == surname.lower()]

    #number of students who need a dormitory
    def count_needs_dormitory(self):
        return sum(1 for s in self.students if s.needs_dormitory)

    #list of students with work experience > 2 years
    def get_experience_gt_2(self):
        return [s for s in self.students if s.work_experience > 2]

    #list of students who graduated from technical college
    def get_graduated_technical(self):
        return [s for s in self.students if s.graduated_from.lower() == 'technical']

    #language groups (dictionary language -> list of students)
    def get_language_groups(self):
        groups = {}
        for s in self.students:
            groups.setdefault(s.language, []).append(s)
        return groups

    def sort_by_surname(self):
        self.students.sort(key=lambda s: s.surname)
        self.save()

    def display_all(self):
        if not self.students:
            print("Student list is empty.")
        for s in self.students:
            print(s)


#Helper functions for user input (with validation)
def input_student():
    """Interactive creation of a Student object with error handling."""
    print("\nEnter student data")
    while True:
        surname = input("Surname: ").strip()
        if surname:
            break
        print("Surname cannot be empty.")
    while True:
        dorm = input("Needs dormitory? (yes/no): ").strip().lower()
        if dorm in ('yes', 'no'):
            needs = dorm == 'yes'
            break
        print("Please enter 'yes' or 'no'.")
    while True:
        exp = input("Work experience (years, integer): ").strip()
        try:
            exp_int = int(exp)
            if exp_int >= 0:
                break
            else:
                print("Experience cannot be negative.")
        except ValueError:
            print("Enter an integer.")
    while True:
        graduated = input("Graduated from (school, technical, university, etc.): ").strip()
        if graduated:
            break
        print("Field cannot be empty.")
    while True:
        lang = input(f"Language ({', '.join(Student.valid_languages)}): ").strip().lower()
        if lang in Student.valid_languages:
            break
        print(f"Invalid language. Allowed: {', '.join(Student.valid_languages)}")
    return Student(surname, needs, exp_int, graduated, lang)


def task1_run():
    #Choose serialization format
    while True:
        fmt = input("\nSelect storage format (csv/pickle): ").strip().lower()
        if fmt in ('csv', 'pickle'):
            break
        print("Invalid choice. Enter 'csv' or 'pickle'.")

    if fmt == 'csv':
        serializer = CsvSerializer()
        filename = "students.csv"
    else:
        serializer = PickleSerializer()
        filename = "students.pkl"

    manager = StudentManager(serializer, filename)

    while True:
        print("MENU:")
        print("1. Add student")
        print("2. Show all students")
        print("3. Find student by surname")
        print("4. Remove student by surname")
        print("5. Statistics: number needing dormitory")
        print("6. List students with experience > 2 years")
        print("7. List students who graduated from technical college")
        print("8. Show language groups")
        print("9. Sort by surname")
        print("0. Exit")

        choice = input("Your choice: ").strip()
        try:
            if choice == '1':
                student = input_student()
                manager.add_student(student)
                print("Student added.")
            elif choice == '2':
                manager.display_all()
            elif choice == '3':
                surname = input("Enter surname to find: ").strip()
                found = manager.find_by_surname(surname)
                if found:
                    print("Found:")
                    for s in found:
                        print(s)
                else:
                    print("Student not found.")
            elif choice == '4':
                surname = input("Enter surname to remove: ").strip()
                manager.remove_student(surname)
                print("Removed (if existed).")
            elif choice == '5':
                cnt = manager.count_needs_dormitory()
                print(f"Students needing dormitory: {cnt}")
            elif choice == '6':
                lst = manager.get_experience_gt_2()
                if lst:
                    print("Students with experience > 2 years:")
                    for s in lst:
                        print(s)
                else:
                    print("No such students.")
            elif choice == '7':
                lst = manager.get_graduated_technical()
                if lst:
                    print("Students graduated from technical college:")
                    for s in lst:
                        print(s)
                else:
                    print("No such students.")
            elif choice == '8':
                groups = manager.get_language_groups()
                if not groups:
                    print("No students.")
                else:
                    for lang, students in groups.items():
                        print(f"\nLanguage: {lang}")
                        for s in students:
                            print(f"  {s.surname}")
            elif choice == '9':
                manager.sort_by_surname()
                print("Sorted by surname.")
            elif choice == '0':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")
        except Exception as e:
            print(f"Error: {e}")

#task1_run()