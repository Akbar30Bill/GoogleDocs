from nab_dict import nab_dict
from providers.worksheet import get_worksheet
from config import sheets_url
from handlers.course import handle_course


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
def get_student_data():
  students_grades = nab_dict()
  students = []
  for worksheet in get_worksheet(sheets_url):
    if worksheet.title == 'لیست دانش‌آموزان':
      students = handle_students(worksheet)
    else:
      students_grades.merge(handle_course(worksheet))
  return students_grades, students