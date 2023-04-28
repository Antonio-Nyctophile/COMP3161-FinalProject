
from flask import Flask, request, make_response
import psycopg2 

app = Flask(__name__)

@app.route('/Lecturers',methods=['GET'])
def lecturers():
    try:
        psql = psycopg2.connect(database='clonevle_db', user='postgres', password='3072001', host='localhost', port='5432' )
        cursor= psql.cursor()
        cursor.execute('SELECT * FROM lecturers')
        lecturerslist=[]
        for lecturerID, firstname,lastname, email, password in cursor:
            lecturers={}
            lecturers ['lecturerID'] = lecturerID
            lecturers ['Name'] = firstname
            lecturers ['Lastname'] = lastname
            lecturers ['Email'] = email
            lecturers ['Password'] = password
            lecturerslist.append(lecturers)
        cursor.close()
        psql.close()
        return make_response(lecturerslist, 200)
    except Exception as e:
        print(e)
        return make_response({'error': 'All lecturers were not found'}, 400)

# Display all students

@app.route('/Students', methods=['GET'])
def students():
    try:
        psql = psycopg2.connect(database='clonevle_db', user='postgres', password='3072001', host='localhost', port='5432' )
        cursor = psql.cursor()
        cursor.execute('SELECT * FROM Students')
        studentslist = []
        for userID, firstname, lastname, email, password in cursor:
            students = {}
            students['studentID'] = userID
            students['firstname'] = firstname
            students['lastname'] = lastname
            students['email'] = email
            students['password'] = password
            studentslist.append(students)
        cursor.close()
        psql.close()
        return make_response(studentslist, 200)
    except Exception as e:
        print(e)
        return make_response({'error': 'All students were not found'}, 400)

# Display all courses

@app.route('/Courses', methods=['GET'])
def courses():
    try:
        psql = psycopg2.connect(database='clonevle_db', user='postgres', password='3072001', host='localhost', port='5432' )
        cursor = psql.cursor()
        cursor.execute('SELECT * FROM courses')
        courseslist = []
        for ccode, courseName, startdate, enddate in cursor:
            courses = {}
            courses['ccode'] = ccode
            courses['courseName'] = courseName
            courses['startdate'] = startdate
            courses['enddate'] = enddate
            courseslist.append(courses)
        cursor.close()
        psql.close()
        return make_response(courseslist, 200)
    except Exception as e:
        print(e)
        return make_response({'error': 'All courses were not found'}, 400)

# Display all admins

@app.route('/Admin', methods=['GET'])
def admin():
    try:
        psql = psycopg2.connect(database='clonevle_db', user='postgres', password='3072001', host='localhost', port='5432' )
        cursor = psql.cursor()
        cursor.execute('SELECT * FROM admins')
        adminlist = []
        for userID, firstname, lastname, password in cursor:
            admin = {}
            admin['adminID'] = userID
            admin['firstname'] = firstname
            admin['lastname'] = lastname
            admin['password'] = password
            adminlist.append(admin)
        cursor.close()
        psql.close()
        return make_response(adminlist, 200)
    except Exception as e:
        print(e)
        return make_response({'error': 'All admins were not found'}, 400)
