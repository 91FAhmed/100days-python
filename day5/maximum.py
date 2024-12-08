
student_score = input().split()
for n in range(0,len(student_score)):
    student_score[n] = int(student_score[n])
 
greatest = 0
for score in student_score:
    print(score)
    if(score > greatest):
        greatest = score

print(f"the maximum score is {greatest}")
    
