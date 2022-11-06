# problem statement - https://www.hackerrank.com/challenges/finding-the-percentage/problem?h_r=next-challenge&h_v=zen&isFullScreen=true
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    if query_name in student_marks.keys():
        # print(query_name)
        # print(student_marks[query_name])
        sum_score = sum(student_marks[query_name])/len(student_marks[query_name])
        print("{0:.2f}".format(sum_score))
