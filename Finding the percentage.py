if __name__ == '__main__':
    p = int(input())
    student_marks = {}
    for _ in range(p):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    a=student_marks.get(query_name)
    print("{0:.2f}".format(sum(a)/len(a)))
