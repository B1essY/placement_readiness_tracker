import random as rd
NUM_STUDENTS=60
import csv
rows=[]
for i in range(NUM_STUDENTS):
    student_id = i+1
    aptitude_score = rd.randint(0, 100)
    dsa_score = rd.randint(0, 100)
    github_score = rd.randint(0, 100)
    communication_score = rd.randint(0, 100)
    resume_score = rd.randint(0, 100)
    rows.append([student_id, aptitude_score, dsa_score, github_score, communication_score, resume_score])

with open('student_Data.csv','w',newline="",encoding='utf-8') as f:
    writer=csv.writer(f)
    writer.writerow(['Student_ID','Aptitude_Score','DSA_Score','GitHub_Score','Communication_Score','Resume_Score'])
    writer.writerows(rows)

print("Data generated successfully")