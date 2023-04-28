from . import db 
from datetime import datetime



class Admin(db.Model):
    __tablename__ = 'admins'

    adminID = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    password = db.Column(db.String(255))

    def __init__(self, firstname, lastname, password):
        self.firstname = firstname
        self.lastname = lastname
        self.password = password

class Lecturer(db.Model):
    __tablename__ = 'lecturers'

    lecturerID = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))

    def __init__(self, firstname, lastname, email, password):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password

class Student(db.Model):
    __tablename__ = 'students'

    studentID = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))

    def __init__(self, firstname, lastname, email, password):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password



class Course(db.Model):
    __tablename__ = 'courses'

    ccode = db.Column(db.String(10), primary_key=True)
    courseName = db.Column(db.String(100))
    startdate = db.Column(db.String(10))
    enddate = db.Column(db.String(10))

    def __init__(self, ccode, courseName, startdate, enddate):
        self.ccode = ccode
        self.courseName = courseName
        self.startdate = startdate
        self.enddate = enddate
#lecturers,students,courses and admin 









#class User(db.Model):
   # id = db.Column(db.Integer, primary_key=True)
   # first_name = db.Column(db.String(50), nullable=False)
   # last_name = db.Column(db.String(50), nullable=False)
  #  student_id = db.Column(db.String(20), unique=True, nullable=False)
  #  student_email = db.Column(db.String(120), unique=True, nullable=False)
   # password = db.Column(db.String(128), nullable=False)

# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# class Course(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     code = db.Column(db.String(10), unique=True, nullable=False)
#     name = db.Column(db.String(100), nullable=False)
#     start_date = db.Column(db.DateTime, nullable=False)
#     end_date = db.Column(db.DateTime, nullable=False)
#     registrations = db.relationship('Registration', backref='course', lazy=True)

# class Student(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String(50), nullable=False)
#     last_name = db.Column(db.String(50), nullable=False)
#     student_id = db.Column(db.String(10), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(128), nullable=False)
#     registrations = db.relationship('Registration', backref='student', lazy=True)

# class Registration(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
#     student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)


