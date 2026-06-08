#daily practice project.
class Student():
    def __init__(self,name: str, emailAddr: str, currentGrade: int):
        if not isinstance(name,str):
            raise TypeError("invalid argument for 'name'")
        if not isinstance(emailAddr,str):
            raise TypeError("invalid argument for 'emailAddr'")
        if not isinstance(currentGrade,(int,float)):
            raise TypeError("invalid argument for 'currentGrade'")
        self.name = name
        self.emailAddr = emailAddr
        self.currentGrade = currentGrade
    def show_info(self):        
        print(f"Name: {self.name}\nEmail Address: {self.emailAddr}\nGrade: {self.currentGrade}")
#input initial value, use a method to display them. easy peasy

if __name__ == "__main__":
    student_1 = Student("Joe","JoeBert@example.com",99.5)
    student_2 = Student("Freya","WhateverFreya'sEmailIs@hotmail.com",98.5)
    student_1.show_info()
    student_2.show_info()
    #TODO from ChatGPT (for tomorrow)
    """TODO PROJECT — Mini Student Management System

GOAL:
Create a program that can manage multiple students using OOP.

==================================================
PART 1 — ADD MORE METHODS
==================================================

Inside the Student class, add these methods:

- update_grade(new_grade)
- change_email(new_email)
- is_passing()

Requirements:
- update_grade() should validate input
- change_email() should check:
    - value is a string
    - contains "@"
- is_passing() should return True if grade >= 75

==================================================
PART 2 — IMPLEMENT __str__
==================================================

Make this work:

    print(student)

instead of:

    student.show_info()

Implement:

    def __str__(self):

Return a formatted string containing:
- name
- email
- grade

==================================================
PART 3 — STORE MULTIPLE STUDENTS
==================================================

Create a list:

    students = []

Add multiple Student objects into the list.

Loop through the list and:
- print every student
- print only passing students

==================================================
PART 4 — CLASS VARIABLE
==================================================

Add a class variable:

    student_count = 0

Every time a Student object is created:
- increment student_count

Print total number of students created.

==================================================
PART 5 — TEST EXCEPTIONS
==================================================

Intentionally break your class with invalid data.

Examples:

    Student(123, "x@gmail.com", 90)
    Student("Joe", [], 90)
    Student("Joe", "x@gmail.com", "A+")

Verify that your validation works correctly.

==================================================
BONUS CHALLENGES
==================================================

BONUS 1:
Create a function:

    average_grade(student_list)

Return the average grade.

------------------------------

BONUS 2:
Find the top student with the highest grade.

------------------------------

BONUS 3:
Practice encapsulation.

Rename attributes like:

    self._grade

Create getter/setter methods.

==================================================
CONCEPTS PRACTICED
==================================================

- constructors
- instance methods
- class variables
- validation
- lists of objects
- iteration
- encapsulation
- special methods (__str__)
- exceptions"""