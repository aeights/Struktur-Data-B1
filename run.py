import os
from flask import Flask
from dotenv import load_dotenv
from flask_session import Session

load_dotenv()  # read env file
app = Flask(__name__)  # init flask app

# Import Blueprint
from routes.Home import Home
from routes.Auth import Auth

# Register Blueprint
app.register_blueprint(Home)
app.register_blueprint(Auth)


if __name__ == "__main__":
    app.secret_key = 'qwerty'
    app.run(debug=True, port=os.getenv("PORT"))