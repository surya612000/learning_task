from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Table
from sqlalchemy.orm import relationship, backref

from database import Base


association_table = Table('association', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)

# Define the Student model
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    courses = relationship('Course', secondary=association_table, back_populates='students')

# Define the Course model
class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    students = relationship('Student', secondary=association_table, back_populates='courses')