import csv

apt = 0
python = 0
sql = 0
communication = 0

no_projects_completed_more_than_5 = 0
no_python_more_than_80 = 0
no_sql_more_than_80 = 0
no_overall_more_than_80 = 0

with open(
    "placement_readiness.csv",
    "r",
    newline="",
    encoding="utf-8"
) as f:

    reader = csv.reader(f)

    next(reader)  # skip header

    for row in reader:

        python_score = int(row[2])
        sql_score = int(row[3])
        aptitude_score = int(row[4])
        communication_score = int(row[5])
        projects_completed = int(row[6])

        overall_score = (
            python_score
            + sql_score
            + aptitude_score
            + communication_score
        ) / 4

        python += python_score
        sql += sql_score
        apt += aptitude_score
        communication += communication_score

        if projects_completed > 5:
            no_projects_completed_more_than_5 += 1

        if python_score > 80:
            no_python_more_than_80 += 1

        if sql_score > 80:
            no_sql_more_than_80 += 1

        if overall_score > 80:
            no_overall_more_than_80 += 1


print("----- REPORT OF COLLEGE PLACEMENT READINESS TRACKER -----")

print(
    f"Number of students with projects completed more than 5: "
    f"{no_projects_completed_more_than_5}"
)

print(
    f"Number of students with Python score more than 80: "
    f"{no_python_more_than_80}"
)

print(
    f"Number of students with SQL score more than 80: "
    f"{no_sql_more_than_80}"
)

print(
    f"Number of students with overall score more than 80: "
    f"{no_overall_more_than_80}"
)

print(f"Average aptitude score: {apt / 120:.2f}")
print(f"Average Python score: {python / 120:.2f}")
print(f"Average SQL score: {sql / 120:.2f}")
print(f"Average Communication score: {communication / 120:.2f}")