import sys
from handlers.course import handle_course
from handlers.students import handle_students
from nab_dict import nab_dict
from providers.worksheet import get_worksheet
from datetime import datetime, timedelta
from flask import Flask

app = Flask(__name__)

sheets_url = 'https://docs.google.com/spreadsheets/d/13EcQlxTGkirllkSx60CbZbjCNDjgQEkWi50LZVftBcM/'

students_grades = nab_dict()
students = []
last_update_timestamp = datetime.now() - timedelta(minutes=10)

def get_student_data():
  students_grades = nab_dict()
  students = []
  for worksheet in get_worksheet(sheets_url, 'robotic-totem-278911-8c98d424f570.json'):
    if worksheet.title == 'لیست دانش‌آموزان':
      students = handle_students(worksheet)
    else:
      students_grades.merge(handle_course(worksheet))
  return students_grades, students

def request_handler(ssn):
  global last_update_timestamp, students, students_grades
  if last_update_timestamp < datetime.now() - timedelta(minutes=5):
    students_grades, students = get_student_data()
    last_update_timestamp = datetime.now()
  for student in students:
    if student['ssn'] == ssn:
      return str(students_grades[(student['name'], student['lastname'], student['class_code'], )])
  return 'No Students Found'

@app.route('/<ssn>')
def get_grades(ssn):
  print(ssn)
  return request_handler(ssn)

app.run()