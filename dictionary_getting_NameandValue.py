'''
The first line contains the integer N, the number of students' records.
The next  lines contain the names and marks obtained by a student, each value separated by a space.
The final line contains query_name, the name of a student to query.
'''

if __name__ == '__main__':
    n = int(input())
    a=[]
    b=0
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    a=student_marks[query_name]
    for i in a:
        b+=i
    print("{:.2f}".format(b/len(a)))

INPUT:
2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh

OUTPUT:
26.50
