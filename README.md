Flask REST API – Users, Posts & Comments

A simple REST API built with Flask, Flask-SQLAlchemy, and SQLite for managing Users, Posts, and Comments. The project includes full CRUD operations and database seeding using Faker.

🚀 Features
CRUD operations for:
Users
Posts
Comments
SQLite database
Flask-SQLAlchemy ORM
Flask-Migrate for database migrations
Faker-based database seeding
📁 Project Structure
.
├── app.py
├── models.py
├── routes.py
├── seed.py
├── Pipfile
├── README.md
└── instance/
    └── app.db
⚙️ Installation
1. Clone the Repository
git clone <your_repo_url>
cd <project_folder>
2. Install Dependencies
Using pip:
pip install flask flask_sqlalchemy flask_migrate faker
OR using Pipenv:
pipenv install
pipenv shell
🗄️ Database Setup
Initialize migrations
flask db init
Create migration
flask db migrate -m "initial migration"
Apply migration
flask db upgrade
🌱 Seed the Database

Run the seed script:

python3 seed.py
This will create:
3 users
9 posts
9 comments
▶️ Run the Server
python3 app.py

Server will run at:

http://127.0.0.1:5555
📡 API Endpoints
👤 Users
Method	Endpoint	Description
GET	/users	Fetch all users
POST	/users	Create a user
GET	/users/<id>	Fetch one user
PUT	/users/<id>	Update a user
DELETE	/users/<id>	Delete a user
📝 Posts
Method	Endpoint	Description
GET	/posts	Fetch all posts
POST	/posts	Create a post
GET	/posts/<id>	Fetch one post
PUT	/posts/<id>	Update a post
DELETE	/posts/<id>	Delete a post
💬 Comments
Method	Endpoint	Description
GET	/comments	Fetch all comments
POST	/comments	Create a comment
GET	/comments/<id>	Fetch one comment
PUT	/comments/<id>	Update a comment
DELETE	/comments/<id>	Delete a comment
📦 Example JSON Requests
Create User
{
  "username": "john"
}
Create Post
{
  "title": "My First Post",
  "content": "Hello Flask!",
  "user_id": 1
}
Create Comment
{
  "message": "Great post!",
  "post_id": 1
}
🛠️ Technologies Used
Python
Flask
Flask-SQLAlchemy
Flask-Migrate
SQLite
Faker
👨‍💻 Author

Joseph Mokaya
