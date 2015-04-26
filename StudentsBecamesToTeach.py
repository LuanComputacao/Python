lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}


def average(lst_num):
    total = float(sum(lst_num))
    return float(total / len(lst_num))


def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    return 0.1 * homework + 0.3 * quizzes + 0.6 * tests


def get_letter_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


def print_average_list(students):
    for student in students:
        print(student["name"])
        print(get_letter_grade(student))


def print_everage_class(lst_students):
    class_average = get_class_average(lst_students)
    print("Class:")
    print(class_average)
    print(get_letter_grade(class_average))


def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(student))
    return average(results)


lst_students = [lloyd, alice, tyler]
print(print_average_list(lst_students))
print(print_everage_class(lst_students))