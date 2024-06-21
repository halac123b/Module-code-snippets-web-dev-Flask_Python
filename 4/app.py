from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from datetime import datetime

app = Flask(__name__)

# Một config đc SQLAlchemy sử dụng để tìm path của file database (k phải builtin)
## "sqlite:///test.db": relative path đến file .db
## "sqlite:////": nếu có 4 dấu / là absolute path
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
# Create database instance from Flask app
db = SQLAlchemy(app)


# Declare database model (table) inherit từ Model của SQLAlchemy
class Todo(db.Model):
    # Lần lượt declare các column (data type, các option)
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    # Define respresent string for class
    def __repr__(self) -> str:
        return "<Task %r>" % self.id  # Format string


# Create database file with all table inherited from Model class
db.create_all()
