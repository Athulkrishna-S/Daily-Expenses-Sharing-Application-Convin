from flask import Flask
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# MongoDB setup
client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("DB_NAME")]




from app.user_routes import user_bp
#from app.expense_routes import expense_bp

app.register_blueprint(user_bp, url_prefix='/user')
#app.register_blueprint(expense_bp)




