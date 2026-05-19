from app import app, db
from models import User, Post, Comment

with app.app_context():

    # clear old data
    Comment.query.delete()
    Post.query.delete()
    User.query.delete()

    db.session.commit()

    # ================= USERS =================
    user1 = User(username="john")
    user2 = User(username="mary")
    user3 = User(username="kevin")

    db.session.add_all([user1, user2, user3])
    db.session.commit()

    # ================= POSTS =================
    posts = [
        Post(title="Post 1", content="Content 1", user_id=user1.id),
        Post(title="Post 2", content="Content 2", user_id=user1.id),
        Post(title="Post 3", content="Content 3", user_id=user1.id),

        Post(title="Post 4", content="Content 4", user_id=user2.id),
        Post(title="Post 5", content="Content 5", user_id=user2.id),
        Post(title="Post 6", content="Content 6", user_id=user2.id),

        Post(title="Post 7", content="Content 7", user_id=user3.id),
        Post(title="Post 8", content="Content 8", user_id=user3.id),
        Post(title="Post 9", content="Content 9", user_id=user3.id),
    ]

    db.session.add_all(posts)
    db.session.commit()

    # ================= COMMENTS =================
    comments = []

    for post in posts:
        comment = Comment(
            message=f"Comment for {post.title}",
            post_id=post.id
        )
        comments.append(comment)

    db.session.add_all(comments)
    db.session.commit()

    print("Database seeded successfully!")