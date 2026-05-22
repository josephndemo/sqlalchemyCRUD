<<<<<<< HEAD
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
=======
from faker import Faker

from app import app, db
from models import Comment, Post, User

fake = Faker()

# add comments
with app.app_context():#remove all data before seeding
    Comment.query.delete()
    Post.query.delete()
    User.query.delete()
    # create 3 users, 9 post, 9 comments
    users = [User(username=fake.unique.user_name()) for _ in range(3)]
    db.session.add_all(users) # add all users to the session
    db.session.flush() # flush to get the ids of the users
    
    # -- create 9 posts, each post is assigned to a user in a round-robin fashion
    posts = [
        Post(
            title=fake.sentence(nb_words=5),  # generate a random title with 5 words    
            content=fake.paragraph(nb_sentences=5), # generate a random content with 5 sentences
            user_id=users[index % len(users)].id,# assign user_id in a round-robin fashion 
        )
        for index in range(9) # create 9 posts
    ]
    db.session.add_all(posts) # add all posts to the session
    db.session.flush() # flush to get theids of the posts
    
    #-- create 9 comments, each comment is assigned to a post in a round-robin fashion
    db.session.add_all(
        Comment(message=fake.sentence(nb_words=12), post_id=post.id)
        for post in posts
    )
    db.session.commit() # commit all changes to the database, this will save the users, posts, and comments to the database tables all at once




>>>>>>> upstream/master
