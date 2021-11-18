from nab_dict import nab_dict


def handle_course(worksheet):
  students_grades = nab_dict()
  title = worksheet.title
  course_name, classcode = title.split('-')

  for row in worksheet.get_all_values()[1:]:
    students_grades.insert((row[0], row[1], classcode), row[2], course_name)

  return students_grades
