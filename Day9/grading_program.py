students_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione":99,
    "Draco":74,
    "Neville": 63,
}



student_grades = {}
grade = ''
for student in students_scores:
    if students_scores[student]>90:
        student_grades[student] = "Outstanding"
    elif students_scores[student]>80:
        student_grades[student] = "Exceeds Expectations"
    elif students_scores[student] >70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"


print(student_grades)