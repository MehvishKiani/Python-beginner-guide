"""Mini Projects — grade_manager.py

Part of Python Beginner Guide: https://github.com/MehvishKiani/Python-beginner-guide
"""
from dataclasses import dataclass, field


@dataclass
class Student:
    name: str
    marks: dict = field(default_factory=dict)

    @property
    def average(self) -> float:
        return round(sum(self.marks.values()) / len(self.marks), 1) if self.marks else 0.0

    @property
    def grade(self) -> str:
        avg = self.average
        for limit, letter in ((90, "A+"), (80, "A"), (70, "B"), (60, "C"), (50, "D")):
            if avg >= limit:
                return letter
        return "F"


class GradeBook:
    def __init__(self):
        self.students: list[Student] = []

    def add(self, name, **marks):
        self.students.append(Student(name, marks))

    def ranking(self):
        return sorted(self.students, key=lambda s: s.average, reverse=True)

    def subject_topper(self, subject):
        return max(self.students, key=lambda s: s.marks.get(subject, 0)).name

    def report(self):
        print(f"{'Rank':<5}{'Name':<8}{'Avg':>6}  Grade")
        print("-" * 26)
        for rank, s in enumerate(self.ranking(), start=1):
            print(f"{rank:<5}{s.name:<8}{s.average:>6}  {s.grade}")


if __name__ == "__main__":
    book = GradeBook()
    book.add("Ali", python=88, math=72, english=81)
    book.add("Sara", python=95, math=91, english=89)
    book.add("Zain", python=64, math=58, english=70)
    book.add("Hina", python=79, math=85, english=92)
    book.report()
    print("\nPython topper:", book.subject_topper("python"))
    print("Students with A or above:", [s.name for s in book.students if s.grade in ("A", "A+")])
