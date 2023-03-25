student_id = 1
with open("text_file.txt","w") as file:
 while True:
    student_name = input('student_name: ')
    if student_name == 'Q':
        break
    mark = input('marks: ')
    file.write(f"student_id:{student_id},student_name: {student_name},student_mark: {mark}\n")
    student_id += 1
 


