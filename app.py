from handlers.students import get_student_data, handle_students
from nab_dict import nab_dict
from providers.worksheet import get_worksheet
from datetime import datetime, timedelta
from flask import Flask
from config import google_config_file
import os

app = Flask(__name__)

with open(google_config_file, 'w') as f:
  f.write(os.environ.get('JSON_CONF_FILE'))
  f.close()

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

@app.route('/')
def main():
  return '<h1>The Great Grade Reporter</h1>'

@app.route('/<ssn>')
def get_grades(ssn):
  return request_handler(ssn)
