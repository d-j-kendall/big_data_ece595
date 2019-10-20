import csv
import operator

letter_gpa ={
    'A': 4,
    'B': 3,
    'C': 2,
    'D': 1,
    'F': 0,
}


def letter_grade(percent):
    if percent<=59:
        return 'F'
    elif percent <= 69:
        return 'D'
    elif percent <=79:
        return 'C'
    elif percent <=89:
        return 'B'
    else:
        return 'A'


records = open('records.txt', 'r')
records_rows = csv.DictReader(records)
records_rows = [i for i in records_rows]

print("\n\nHighest Grade in Each Course \n")
records_rows.sort(key=operator.itemgetter('ece595'), reverse=True)
print(f"{records_rows[0]['student']} has the highest grade in ECE 595 with {records_rows[0]['ece595']} percent")
records_rows.sort(key=operator.itemgetter('ece547'), reverse=True)
print(f"{records_rows[0]['student']} has the highest grade in ECE 547 with {records_rows[0]['ece547']} percent")
records_rows.sort(key=operator.itemgetter('ece354'), reverse=True)
print(f"{records_rows[0]['student']} has the highest grade in ECE 354 with {records_rows[0]['ece354']} percent")

print("Student Grades in Each Subject: ")
for row in records_rows:
    row['ece595L'] = letter_grade(int(row['ece595']))
    row['ece547L'] = letter_grade(int(row['ece547']))
    row['ece354L'] = letter_grade(int(row['ece354']))
    gpa = 4*(letter_gpa[row['ece595L']]+letter_gpa[row['ece547L']]+letter_gpa[row['ece354L']])/12
    print(f"\n\n{row['student']}\t\t GPA = {gpa:.2}")
    print("ECE 595\tECE 547\tECE 354")
    print(f"\t{row['ece595L']}"
          f"   \t{row['ece547L']}"
          f"   \t{row['ece354L']}")
