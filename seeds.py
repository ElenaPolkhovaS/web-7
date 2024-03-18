import random
import string
from connect_db import session
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Group, Student, Teacher, Subject, Grade
from random import randint, sample

# Підключення до бази даних
engine = create_engine('postgresql://postgres:mypass@localhost/test_bd')
Base.metadata.bind = engine

# Створення сесії
Session = sessionmaker(bind=engine)
session = Session()

# Ініціалізація Faker
fake = Faker()

# Заповнення груп
random_letters = [random.choice(string.ascii_uppercase) for _ in range(3)]
two_digit_numbers = [random.randint(10, 99) for _ in range(3)]
group_names = ["{}-{}".format(letter, number) for letter, number in zip(random_letters, two_digit_numbers)]
groups = [Group(id=i, name_gr=name) for i, name in zip(range(1, 4), group_names)]
session.add_all(groups)
session.commit()

# Заповнення викладачів
teachers = [Teacher(fullname=fake.name()) for _ in range(1, 6)]
session.add_all(teachers)
session.commit()

# Заповнення предметів
subjects = [Subject(name=fake.word(), teacher_id=randint(1, 5)) for _ in range(1, 9)]
session.add_all(subjects)
session.commit()

# Заповнення студентів
students = [Student(fullname=fake.name(), group_id=randint(1, 3)) for _ in range(1, 51)]
session.add_all(students)
session.commit()

# Заповнення оцінок
for student in students:
    for subject in subjects:
        grade = randint(1, 5)
        grade_date = fake.date_between(start_date='-1y', end_date='today')
        session.add(Grade(student_id=student.id, subject_id=subject.id, grade=grade, grade_date=grade_date))

session.commit()

# Закриття сесії
session.close()
