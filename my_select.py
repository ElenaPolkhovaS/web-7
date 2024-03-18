from sqlalchemy import create_engine, func, select, desc
from sqlalchemy.orm import sessionmaker
from models import Group, Student, Teacher, Subject, Grade


def select_1():
    with DBSession() as session:
        result = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
                .select_from(Grade)\
                .join(Student)\
                .group_by(Student.id)\
                .order_by(desc('avg_grade'))\
                .limit(5).all()
        for row in result:
            print(row)

def select_2():
    with DBSession() as session:
        result = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
                .select_from(Grade)\
                .join(Student)\
                .join(Subject)\
                .filter(Subject.id == 5)\
                .group_by(Student.id)\
                .order_by(desc('avg_grade'))\
                .limit(1).first()
        for row in result:
            print(row)

def select_3():
    with DBSession() as session:
        result = session.query(Group.name_gr, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
                .select_from(Grade)\
                .join(Student)\
                .join(Subject)\
                .join(Group)\
                .filter(Subject.id == 3)\
                .group_by(Group.id)\
                .all()
        for row in result:
            print(row)

def select_4():
    with DBSession() as session:
        result = session.query(func.round(func.avg(Grade.grade), 2)).scalar()
        print(result)

def select_5():
    with DBSession() as session:
        result = session.query(Subject.name)\
                .join(Teacher)\
                .filter(Teacher.id == 5)\
                .all()
        for row in result:
            print(row)

def select_6():
    with DBSession() as session:
        result = session.query(Student.fullname)\
                .select_from(Student)\
                .join(Group)\
                .filter(Group.id == 2)\
                .all()
        for row in result:
            print(row)       

def select_7():
    with DBSession() as session:
        result = session.query(Student.fullname, Subject.name, Grade.grade)\
                .select_from(Grade)\
                .join(Subject)\
                .filter(Student.group_id == 3, Subject.id == 5)\
                .all()
        for row in result:
            print(row)

def select_8():
    with DBSession() as session:
        result = session.query(func.round(func.avg(Grade.grade), 2))\
                .join(Subject)\
                .join(Teacher)\
                .filter(Teacher.id == 4)\
                .scalar()
        print(result)

def select_9():
    with DBSession() as session:
        result = session.query(Student.fullname, Subject.name)\
                .select_from(Subject)\
                .join(Grade)\
                .filter(Student.id == 12)\
                .distinct()\
                .all()
        for row in result:
            print(row)

def select_10():
    with DBSession() as session:
        result = session.query(Student.fullname, Teacher.fullname, Subject.name)\
                .select_from(Subject)\
                .join(Grade)\
                .join(Student)\
                .join(Teacher)\
                .distinct()\
                .all()
        for row in result:
            print(row)


def select_dod1():
    with DBSession() as session:
        result = session.query(func.round(func.avg(Grade.grade), 2))\
            .join(Subject, Subject.id == Grade.subject_id)\
            .join(Teacher, Teacher.id == Subject.teacher_id)\
            .filter(Subject.teacher_id == 5, Grade.student_id == 27)\
            .scalar()
        print(result)


if __name__ == '__main__':

    engine = create_engine('postgresql://postgres:mypass@localhost/test_bd')
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    
    select_1()
    select_2()
    select_3()
    select_4()
    select_5()
    select_6()
    select_7()
    select_8()
    select_9()
    select_10()
    select_dod1()
