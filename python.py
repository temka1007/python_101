course_titles = ['Linear Algebra', 'Cell Biology', 'Programming']
midterm_scores = {
    'Alice': [62, 60, 77],
    'Bob': [84, 88, 87],
    'Carol': [88, 88, 97],
    'Chuck': [92, 71, 93],
    'Craig': [81, 89, 72],
    'Dan': [79, 100, 97],
    'Erin': [76, 72, 65],
    'Eve': [69, 84, 67],
    'Faythe': [66, 60, 70],
    'Frank': [88, 76, 64],
    'Grace': [66, 77, 92],
    'Heidi': [93, 93, 82],
    'Mallory': [77, 89, 82],
    'Oscar': [67, 63, 67],
    'Peggy': [70, 81, 86],
    'Sybil': [96, 94, 62],
    'Trent': [67, 66, 61],
    'Trudy': [85, 74, 90],
    'Victor': [82, 67, 94],
    'Walter': [67, 84, 86],
    'Wendy': [97, 92, 66]
}


def print_scores(param):
    if param in midterm_scores.keys():
        print(f"""{param}:
    {course_titles[0]}: {midterm_scores[param][0]}
    {course_titles[1]}: {midterm_scores[param][1]}
    {course_titles[2]}: {midterm_scores[param][2]}
    Average: {sum(midterm_scores[param])/len(midterm_scores[param])}""")
    else:
        print(f"There is no student named {param}")

print_scores(input())


    