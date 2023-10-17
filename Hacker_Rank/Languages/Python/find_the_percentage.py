


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    query_marks = student_marks[query_name]
    average = round(sum(query_marks) / len(query_marks), 2)
    print(f"{average:.2f}")
