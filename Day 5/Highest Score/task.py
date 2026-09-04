student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

print(len(student_scores))
sum_of_scores = 0
for score in student_scores:
    sum_of_scores += score
print(sum_of_scores)
max_score = student_scores[0]
for i in range(1,len(student_scores)):
    if student_scores[i] > max_score:
        max_score = student_scores[i]
print(max_score)
x = max(student_scores)

print(x)


