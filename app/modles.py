from app.plugins import db


class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    age = db.Column(db.Integer, nullable=True)
