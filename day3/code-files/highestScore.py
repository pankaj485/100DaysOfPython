# highest score identifier 
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = 0

for score in student_scores:
    if highest_score < score:
        highest_score = score

print(f"highest sore: {highest_score}")
