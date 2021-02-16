import time
from sqlalchemy.exc import OperationalError
from database import create_tables, populate_db, engine


def wait_for_postgres_to_come_up(engine):
    while True:
        try:
            if engine.connect():
                create_tables()
                populate_db()
                print("POSTGRES IS UP")
                break
        except OperationalError:
            time.sleep(0.5)
            print("POSTGRES IS DOWN...")


if __name__ == "__main__":
    print("TRYING TO START POSTGRES ----------------------------")
    wait_for_postgres_to_come_up(engine)
