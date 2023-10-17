

def get_second_lowest_scorer_student(students):
    students_found = []
    students.sort(key=lambda x: x[1])
    lowest = students[0][1]
    second_lowest = 0
    for student in students:
        if lowest == student[1]:
            continue
        if second_lowest == 0:
            second_lowest = student[1]
            students_found.append(student[0])
            continue
        if second_lowest == student[1]:
            students_found.append(student[0])

    students_found.sort()

    return students_found


if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        students.append([name, score])
    
    results = get_second_lowest_scorer_student(students)
    for result in results:
        print(result)
        
    