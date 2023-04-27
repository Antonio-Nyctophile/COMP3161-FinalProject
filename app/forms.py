# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired
from wtforms import FileField
from flask_wtf.file import FileRequired, FileAllowed



class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class RegisterForm(FlaskForm):

    firstname = StringField('First Name', validators=[InputRequired()])
    lastname = StringField('Last Name', validators=[InputRequired()])
    studentID = StringField('Student ID', validators=[InputRequired()])
    studentemail = StringField('Student Email', validators=[InputRequired()])
    password = StringField('Password', validators=[InputRequired()])

class CreateCourse(FlaskForm):
    ccode = StringField('Course Code', validators=[InputRequired()])
    CourseName = StringField('Course Name', validators=[InputRequired()])
    StartDate = StringField ('Start Date', validators=[InputRequired()])
    EndDate = StringField ('End Date', validators=[InputRequired()])

class RegisterCourse(FlaskForm):
    ccode = StringField('Course Code', validators=[InputRequired()])
    studentID = StringField('Student ID', validators=[InputRequired()])

#add Uploadform, eventform, forums, discusionthread

class UploadForm(FlaskForm):
    file = FileField('File', validators=[FileRequired(), FileAllowed(['pdf', 'doc', 'docx', 'txt', 'xlsx', 'csv'], 'Only files with PDF, DOC, DOCX, TXT, XLSX or CSV extensions are allowed.')])
    description = StringField('Description', validators=[InputRequired()])

class EventForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    description = StringField('Description', validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    start_time = StringField('Start Time', validators=[InputRequired()])
    end_time = StringField('End Time', validators=[InputRequired()])

class Forums(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    description = StringField('Description', validators=[InputRequired()])

class DiscussionThreadForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    content = StringField('Content', validators=[InputRequired()])
