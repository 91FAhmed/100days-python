student_score = {
    "harry":81,
    "Ron":78,
    "josh":99,
    "Draco":74,
    "neville":69
}

student_grades = {}

for student in student_score:
   if(student_score[student] > 91):
      student_grades[student] = "outstanding"
   elif(student_score[student] > 81 and student_score[student] < 90):
      student_grades[student] = "Exceeds expectation"
   elif(student_score[student] > 71 and student_score[student] < 81):
      student_grades[student] = "Acceptable"
   else:
       student_grades[student] = "Fail "
print(student_grades)

travel_log = {
   "france":["brjon","Lille",["Trash"]],
   "Germany":["Hamburger","Fire",{"dictionary":"Owl Kitty"}]
}

print(travel_log["Germany"][2]['dictionary'])