# posts = [
#     {
#         'author': 'Surendra',
#         'title': 'The first post',
#         'content': 'This is the first post',
#         'date_posted': 'June 26, 2019'
#     },
#     {
#         'author': 'Surendra',
#         'title': 'Welcome',
#         'content': 'The flask demo app',
#         'date_posted': 'June 27, 2019'
#     }
# ]

# from flaskblog import db
# from models import User, Post
# import secrets

# db.create_all()

# u1 = User(username='Surendra', email='surendra@blog.com', password='password')
# u2 = User(username='Sim Dormy', email='sdor@blog.com', password='password')
#
# db.session.add(u1)
# db.session.add(u2)

# users = User.query.all()
# for u in users:
#     for i in range(1, 4):
#         p = Post(title=f'Post {i}', content=secrets.token_urlsafe(100), user_id=u.id)
#         db.session.add(p)
#
# db.session.commit()
