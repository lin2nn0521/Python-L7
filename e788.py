n = int(input())
students = []
students_id_first = []
students_id_last = []

for i in range(n):
    students.append([])
    students_id_first.append([])
    students_id_last.append([])
    students[i] = input().split()

    students_id_last[i] = students[i][0]
    students_id_last[i] = students_id_last[i][8]

    students_id_first[i] = students[i][0]
    students_id_first[i] = students_id_first[i][0]

    students[i].append(students_id_last[i])
    students[i].append(students_id_first[i])

students.sort(key = lambda s: (s[2],s[3]))

for i in range(n):
    print(students[i][2]+": "+students[i][1])