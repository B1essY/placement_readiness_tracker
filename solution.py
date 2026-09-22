import csv
res=apt=dsa=git=com=0
no_resume_more_than_80 = 0
no_dsa_more_than_80 = 0
no_overall_more_than_80 = 0
with open('student_Data.csv','r', newline="", encoding='utf-8') as f:
    reader=csv.reader(f)
    next(reader)
    for row in reader:
        res+=int(row[5])
        apt+=int(row[1])
        dsa+=int(row[2])
        git+=int(row[3])
        com+=int(row[4])
        overall_score = (int(row[1]) + int(row[2]) + int(row[3]) + int(row[4]) + int(row[5])) / 5
        if int(row[5]) > 80:
            no_resume_more_than_80 += 1
        if int(row[2])  > 80:
            no_dsa_more_than_80 += 1
        if overall_score > 80:
            no_overall_more_than_80 += 1
print("-----REPORT OF COLLEGE PLACEMET READINESS TRACKER-----")
print(f"Number of students with resume score more than 80: {no_resume_more_than_80}")
print(f"Number of students with DSA score more than 80: {no_dsa_more_than_80}")
print(f"Number of students with overall score more than 80: {no_overall_more_than_80}")
print(f"Average aptitude score of all students: {apt/60}")
print(f"Average DSA score of all students: {dsa/60}")
print(f"Average GitHub score of all students: {git/60}")
print(f"Average Communication score of all students: {com/60}")
print(f"Average Resume score of all students: {res/60}")