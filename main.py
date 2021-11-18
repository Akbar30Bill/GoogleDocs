import sys
from handlers.course import handle_course
from handlers.students import handle_students
from nab_dict import nab_dict
from providers.worksheet import get_worksheet

sheets_url = 'https://docs.google.com/spreadsheets/d/13EcQlxTGkirllkSx60CbZbjCNDjgQEkWi50LZVftBcM/'

students_grades = nab_dict()
students = []

for worksheet in get_worksheet(sheets_url, sys.argv[1]):
  if worksheet.title == 'لیست دانش‌آموزان':
    students = handle_students(worksheet)
  else:
    students_grades.merge(handle_course(worksheet))

print(students)