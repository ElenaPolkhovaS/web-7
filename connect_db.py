from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://postgres:mypass@localhost/test_bd")
Session = sessionmaker(bind=engine)
session = Session()