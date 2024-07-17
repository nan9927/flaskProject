from flask import Blueprint, request

from app.modles import Student
from app.plugins import db

blue = Blueprint('blue', __name__)


@blue.route('/student/search/<int:id>', methods=['GET'])
def serarch(id):
    student = Student.query.get(id)

    return f'姓名:{student.name},age:{student.age}'


@blue.route('/student/add', methods=['POST'])
def addStudent():
    db.session.add(Student(
        name=request.form.get('name'),
        age=request.form.get('age')
    ))
    db.session.commit()
    return '添加成功'


@blue.route('student/update', methods=['POST'])
def updateStudent():
    student = Student.query.get(request.form.get('id'))
    student.name = request.form.get('name')
    student.age = request.form.get('age')
    db.session.commit()
    return '修改成功'


@blue.route('/student/delete/<int:id>', methods=['GET'])
def deleteStudent(id):
    student = Student.query.get(id)
    db.session.delete(student)
    db.session.commit()
    return '删除成功'
