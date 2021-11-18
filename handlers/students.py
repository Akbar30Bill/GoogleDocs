def handle_students(worksheet):
  students = []
  for row in worksheet.get_all_values()[1:]:
    students.append({
      'class_code': row[0],
      'name': row[1],
      'lastname': row[2],
      'student_id': row[3],
      'ssn': row[4],
    })

  return students
