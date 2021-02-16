import os
from flask import Flask, render_template
from sqlalchemy.orm import sessionmaker

from database import Customers, engine

session = sessionmaker(bind=engine)()

app = Flask(__name__)


@app.route("/")
def home():
    app_name = os.environ.get("APP_NAME", "VIRUS")
    costumers = session.query(Customers).all()

    return render_template('home.html', costumers=costumers, app_name=app_name)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
