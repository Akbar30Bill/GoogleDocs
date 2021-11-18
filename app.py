from handlers.students import get_student_data, handle_students
from nab_dict import nab_dict
from providers.worksheet import get_worksheet
from datetime import datetime, timedelta
from flask import Flask

app = Flask(__name__)

students_grades = nab_dict()
students = []
last_update_timestamp = datetime.now() - timedelta(minutes=10)

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
  return request_handler(ssn)
  