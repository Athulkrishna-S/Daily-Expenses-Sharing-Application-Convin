from flask import Flask
from pymongo import MongoClient
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)


#JWT setup
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")  # Set this in your .env file
jwt = JWTManager(app)

# MongoDB setup
client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("DB_NAME")]




from app.user_routes import user_bp
from app.expense_routes import expense_bp

app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(expense_bp,url_prefix='/expense')




