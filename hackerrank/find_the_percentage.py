if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    obj = student_marks[query_name]

    avj = float(sum(obj)) / float(len(obj))
    print(f"{avj:.2f}")
