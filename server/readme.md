A simple Flask REST API for managing Users, Posts, and Comments using Flask-SQLAlchemy and SQLite.

## Features

- CRUD operations for:
  - Users
  - Posts
  - Comments
- SQLite database
- Flask-SQLAlchemy ORM
- Faker seeding script

---

# Project Structure

```bash
.
├── app.py
├── models.py
├── routes.py
├── seed.py
├── Pipfile
├── README.md
└── instance/
    └── app.db
Installation
1. Clone the repository
git clone <your_repo_url>
cd <project_folder>
2. Install dependencies

Using pip:

pip install flask flask_sqlalchemy flask_migrate faker

OR using Pipenv:

pipenv install
pipenv shell
Database Setup
Initialize migration
flask db init
Create migration
flask db migrate -m "initial migration"
Apply migration
flask db upgrade
Seed the Database

Run the seed file:

python3 seed.py

This will create:

3 users
9 posts
9 comments
Run the Server
python3 app.py

Server runs at:

http://127.0.0.1:5555
API Endpoints
Users
Method	Endpoint	Description
GET	/users	Fetch all users
POST	/users	Create a user
GET	/users/<id>	Fetch one user
PUT	/users/<id>	Update user
DELETE	/users/<id>	Delete user
Posts
Method	Endpoint	Description
GET	/posts	Fetch all posts
POST	/posts	Create a post
GET	/posts/<id>	Fetch one post
PUT	/posts/<id>	Update post
DELETE	/posts/<id>	Delete post
Comments
Method	Endpoint	Description
GET	/comments	Fetch all comments
POST	/comments	Create a comment
GET	/comments/<id>	Fetch one comment
PUT	/comments/<id>	Update comment
DELETE	/comments/<id>	Delete comment
Example JSON Requests
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
Technologies Used
Python
Flask
Flask-SQLAlchemy
Flask-Migrate
SQLite
Faker
Author

Joseph Mokaya