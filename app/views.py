"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app
from flask import render_template, request, jsonify, send_file
#from app.models import User
from app.forms import RegisterForm
#from app.forms import LoginForm
import os
from flask_wtf.csrf import generate_csrf

###
# The functions below should be applicable to all Flask apps.
#               ADD API FOR FORMS
###

#Register API
@app.route('/register', methods=['POST'])
def register():
    form = RegisterForm(request.form)
    if form.validate():
        user = User(
            firstname=form.firstname.data,
            lastname=form.lastname.data,
            studentId=form.studentID.data,
            studentemail=form.studentemail.data,
            password=form.PasswordField.data
        )
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully.'}), 201
    else:
        return jsonify({'errors': form.errors}), 400


# LOGIN API







@app.route('/courses', methods=['POST'])
def create_course():
    form = CreateCourse(request.form)
    if form.validate():
        course = Course(
            ccode=form.ccode.data,
            name=form.CourseName.data,
            start_date=form.StartDate.data,
            end_date=form.EndDate.data
        )
        db.session.add(course)
        db.session.commit()
        return jsonify({'message': 'Course created successfully.'}), 201
    else:
        return jsonify({'errors': form.errors}), 400

    

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