"""

Author: Jungwongsuk Jennrong
Student ID:12431964

"""

import sqlite3
from bottle import request, route, run, template

def enroll_course(student_id, course_code):
    db = sqlite3.connect('regsystem.db')
    db.execute("INSERT INTO courseenrollment (StudentID,CourseCode) VALUES (?, ?)", (student_id,course_code))
    db.commit()
    return True

def drop_course(student_id, course_code):
    db = sqlite3.connect('regsystem.db')
    db.execute("DELETE FROM courseenrollment WHERE StudentID = ? AND CourseCode = ?", (student_id,course_code))
    db.commit()
    return True

@route('/help')
def do_help():
    return template('help')

@route('/course_list')
def course_list():
    db = sqlite3.connect('regsystem.db')
    c = db.cursor()
    c.execute("SELECT CourseCode, CourseTitle, Credit FROM course ORDER BY CourseCode")
    data = c.fetchall()
    c.close()
    output = template('course_list', rows=data)
    return output

@route('/enrolled_course')
def enrolled_course():
    db = sqlite3.connect('regsystem.db')
    c = db.cursor()
    c.execute("SELECT courseenrollment.StudentID, courseenrollment.CourseCode, course.CourseTitle FROM courseenrollment INNER JOIN course ON courseenrollment.CourseCode = course.CourseCode ORDER BY StudentID ")
    data = c.fetchall()
    c.close()
    output = template('course_enrolled_record', rows=data)
    return output

@route('/enrolled_course/<mystudentid>')
def student_enrolled_course(mystudentid):
    db = sqlite3.connect('regsystem.db')
    c = db.cursor()
    c.execute("SELECT courseenrollment.CourseCode, course.CourseTitle, course.Credit FROM courseenrollment INNER JOIN course ON courseenrollment.CourseCode = course.CourseCode WHERE StudentID LIKE ?", (mystudentid,))
    data = c.fetchall()
    c.close()
    output = template('course_enrolled_student', rows=data, studentid_id=mystudentid)
    return output

@route('/enroll')
def enroll():
    return '''
        <title>Enroll</title>
        <h1>Enroll Course</h1>
        Please enter your student ID and the course code that you want to enroll.<br /><br />
        <form action="/enroll" method="post">
        Student ID: <input name="studentid" type="text" /> <br />
        Course Code: <input name="coursecode" type="text" /> <br />
        <input value="Enroll" type="submit" />
        </form>
    '''
    
@route('/enroll', method='POST')
def do_enroll():
    student_id  = request.forms.get('studentid')
    course_code = request.forms.get('coursecode')
    if enroll_course(student_id, course_code):
        return "<p>Student ID {0} enrolled to course {1} successfully.</p>".format(student_id, course_code)
    else:
        return "<p>Enrollment operation failed.</p>"
    
@route('/drop')
def drop():
    return '''
        <title>Drop</title>
        <h1>Drop Course</h1>
        Please enter your student ID and the course code that you want to drop.<br /><br />
        <form action="/drop" method="post">
        Student ID: <input name="studentid" type="text" /> <br />
        Course Code: <input name="coursecode" type="text" /> <br />
        <input value="Drop" type="submit" />
        </form>
    '''
    
@route('/drop', method='POST')
def do_drop():
    student_id  = request.forms.get('studentid')
    course_code = request.forms.get('coursecode')
    if drop_course(student_id, course_code):
        return "<p>Student ID {0} dropped course {1} successfully.</p>".format(student_id, course_code)
    else:
        return "<p>Course Drop operation failed.</p>"


run(host='0.0.0.0', port=8080)