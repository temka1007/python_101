attendance_data = {
    'Math Club': {
        'Alice': 'Present', 
        'Bob': 'Absent', 
        'Carol': 'Present'
        },
    'Science Club': {
        'Alice': 'Absent', 
        'Bob': 'Present', 
        'Carol': 'Present'
        },
    'Book Club': {
        'Alice': 'Present', 
        'Carol': 'Absent', 
        'Dan': 'Present'
        },
    'Music Club': {
        'Bob': 'Present', 
        'Dan': 'Absent', 
        'Carol': 'Present'
        }
}


def attendance_report(student_name):
    present = 0
    taken = 4
    try:
        math = attendance_data["Math Club"][student_name]
        if math == "Present": present += 1
    except:
        math = "Didn't take the this class!"
        taken -= 1

    try:
        science = attendance_data["Science Club"][student_name]
        if science == "Present": present += 1
        
    except:
        science = "Didn't take the this class!"
        taken -= 1

    try:
        book = attendance_data["Book Club"][student_name]
        if book == "Present": present += 1
    except:
        book = "Didn't take the this class!"
        taken -= 1

    try:
        music = attendance_data["Music Club"][student_name]
        if music == "Present": present += 1
    except:
        music = "Didn't take the this class!"
        taken -= 1

    if student_name in attendance_data['Book Club'].keys():
        print(f"""{student_name}:
    Math Club: {math}
    Science Club: {science}
    Book Club: {book}
    Music Club: {music}
    Total Events Attended: {present}
    Attendance Percentage: {round((present/taken)*100, 1)}%""")
    else:
        print(f"There is no student named {student_name}.")

attendance_report(input())