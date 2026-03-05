from flask import Flask
from routes import api_routes
from database import init_db
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

init_db()

app.register_blueprint(api_routes)

if __name__ == "__main__":
    app.run(debug=True)