"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app
from flask import render_template, request, jsonify, send_file,make_response
from app.forms import RegisterForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app.models import Course, Student, Lecturer, Admin
import os
from flask_wtf.csrf import generate_csrf
from . import db

#import psycopg2
#from app.models import User
#from app.forms import LoginForm
#from forms import CreateCourse
#from forms import RegisterCourse###
#from flask_marshmallow import Marshmallow
#from flask_cors import CORS
# # The functions below should be applicable to all Flask apps.
#               ADD API FOR FORMS
###

#Register API
# from flask import Flask, request, jsonify
# from flask_wtf import CSRFProtect
# from forms import RegisterForm
# from forms import LoginForm

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secretkey'
# csrf = CSRFProtect(app)

# @app.route('/register', methods=['POST'])
# def register():
#     form = RegisterForm()
#     if form.validate_on_submit():
#         # create user in the database
#         user = {
#             'firstname': form.firstname.data,
#             'lastname': form.lastname.data,
#             'studentID': form.studentID.data,
#             'studentemail': form.studentemail.data,
#             'password': form.password.data
#         }
#         # add the user to the database
#         # return success message
#         return jsonify({'message': 'User registered successfully'})
#     else:
#         # return error message and validation errors
#         return jsonify({'message': 'Error registering user', 'errors': form.errors}), 400

# if __name__ == '__main__':
#     app.run(debug=True)



# LOGIN API

# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         # check if user exists in database
#         # if user exists and password matches, log them in
#         # else return error message
#         return jsonify({'message': 'User logged in successfully'})
#     else:
#         # return error message and validation errors
#         return jsonify({'message': 'Error logging in', 'errors': form.errors}), 400

# if __name__ == '__main__':
#     app.run(debug=True)


# CREATE COURSE 

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secretkey'
# csrf = CSRFProtect(app)

# @app.route('/create_course', methods=['POST'])
# def create_course():
#     form = CreateCourse()
#     if form.validate_on_submit():
#         # add course details to database
#         # return success message
#         return jsonify({'message': 'Course created successfully'})
#     else:
#         # return error message and validation errors
#         return jsonify({'message': 'Error creating course', 'errors': form.errors}), 400

# if __name__ == '__main__':
#     app.run(debug=True)


# Retrive course 

# @app.route('/get_course', methods=['GET'])
# def get_course():
#     ccode = request.args.get('ccode')
#     course = next((c for c in courses if c['ccode'] == ccode), None)
#     if course:
#         return jsonify(course)
#     else:
#         return jsonify({'message': 'Course not found'}), 404

# if __name__ == '__main__':
#     app.run(debug=True)    

# Register Course 

# @app.route('/register_course', methods=['POST'])
# def register_course():
#     form = RegisterCourse()
#     if form.validate_on_submit():
#         ccode = form.ccode.data
#         studentID = form.studentID.data
#         course = next((c for c in courses if c['ccode'] == ccode), None)
#         student = next((s for s in students if s['studentID'] == studentID), None)
#         if course and student:
#             if studentID not in course['students']:
#                 course['students'].append(studentID)
#                 return jsonify({'message': 'Student registered successfully'})
#             else:
#                 return jsonify({'message': 'Student already registered for the course'})
#         else:
#             return jsonify({'message': 'Course or student not found'}), 404
#     else:
#         return jsonify({'message': 'Validation error'}), 400

# if __name__ == '__main__':
#     app.run(debug=True)

#Retrives members for a course 

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
# ma = Marshmallow(app)
# CORS(app)


# class CourseSchema(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model = Course
#         load_instance = True


# class StudentSchema(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model = Student
#         load_instance = True


# @app.route('/courses/<string:course_code>/members', methods=['GET'])
# def get_course_members(course_code):
#     course = Course.query.filter_by(code=course_code).first()

#     if not course:
#         return jsonify({'error': 'Course not found'}), 404

#     registrations = Registration.query.filter_by(course_id=course.id).all()

#     if not registrations:
#         return jsonify({'error': 'No registrations found for course'}), 404

#     student_ids = [r.student_id for r in registrations]
#     students = Student.query.filter(Student.id.in_(student_ids)).all()

#     course_schema = CourseSchema()
#     student_schema = StudentSchema(many=True)

#     return jsonify({'course': course_schema.dump(course),
#                     'students': student_schema.dump(students)})

#from flask_wtf.csrf import generate_csrf
@app.route('/api/v1/csrf-token', methods=['GET'])
def get_csrf():
    return jsonify({'csrf_token': generate_csrf()})
#from werkzeug.utils import secure_filename

###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")

# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


# API's to query database
