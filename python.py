language_skills: dict = {
    'Alice': {'English', 'Spanish', 'German'},
    'Bob': {'English', 'French'},
    'Carol': {'Spanish', 'German', 'Japanese'},
    'Dan': {'English', 'Spanish', 'Korean'},
    'Eve': {'German', 'Korean'}
}

def compare_languages(student1, student2):
    if student1 not in language_skills.keys():
        print(f"There is no student named {student1}.")
        exit()

    if student2 not in language_skills.keys():
        print(f"There is no student named {student2}.")
        exit()


    firstStudent = language_skills[student1]
    secondStudent = language_skills[student2]

    bothKnows: set = firstStudent & secondStudent
    uniqueToStudent1: set = firstStudent.difference(secondStudent)
    uniqueToStudent2: set = secondStudent.difference(firstStudent)

    print(f'''{student1} knows: {firstStudent}
{student2} knows: {secondStudent}
Languages known by both {student1} and {student2}: {bothKnows}
Languages unique to {student1}: {uniqueToStudent1}
Languages unique to {student2}: {uniqueToStudent2}''')


compare_languages(input("Enter first student: "), input("Enter second student: "))