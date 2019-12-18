from typing import List


class School:
    def __init__(self):
        self.students: dict[str:int] = {}

    def add_student(self, name: str, grade: int):
        self.students[name] = grade

    def roster(self) -> List[str]:
        students = [student[0] for student in sorted(self.students.items(), key=self.student_sort)]
        return students

    def student_sort(self, student):
        return f"{student[1]}{student[0]}"

    def grade(self, grade_number: int) -> List[str]:
        students_in_grade = [student for student in self.students.keys() if self.students[student] == grade_number]
        students_in_grade.sort()
        return students_in_grade
