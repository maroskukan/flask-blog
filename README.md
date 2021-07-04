# Flask Blog Application

- [Flask Blog Application](#flask-blog-application)
  - [Introduction](#introduction)
  - [Secret Generation](#secret-generation)
  - [Database](#database)
    - [Database File Creation](#database-file-creation)
    - [Database Record Creation](#database-record-creation)
    - [Database Record Cleanup](#database-record-cleanup)
    - [Secret key and Database URI Configuration](#secret-key-and-database-uri-configuration)
  - [Messaging](#messaging)
    - [Email Support](#email-support)

## Introduction

This repository contains code for building a basic blog application using Flask.

## Secret Generation

You can leverage the `secrets` library to generate a secret.

```bash
echo -e "import secrets\nprint(secrets.token_hex(16))" | python
6f303dff8c5bc7c4c32870f598d2dfe9
```

## Database 

### Database File Creation

You can leverage the python shell to generate a SQLite Database file. No output (*except the FSADeprecationWarning*) means there were no errors during creation and a new `site.db` should be present on the filesystem.

```bash
echo -e "from flaskblog import db\ndb.create_all()" | python
```

### Database Record Creation

Create 2 records in `User` table.

```bash
echo -e "from flaskblog import db, User, Post\nuser_1 = User(username='Maros',email='maros@example.com', password='password')\ndb.session.add(user_1)\ndb.session.commit()" | python
echo -e "from flaskblog import db, User, Post\nuser_2 = User(username='Corey',email='corey@example.com', password='password')\ndb.session.add(user_2)\ndb.session.commit()" | python
```

Retrieve records from `User` table.

```bash
# Retrieve all users
echo -e "from flaskblog import db, User, Post\nprint(User.query.all())" | python
[User('Maros', 'maros@example.com', 'default.jpg'), User('Corey', 'corey@example.com', 'default.jpg')]

# Retrieves first user
echo -e "from flaskblog import db, User, Post\nprint(User.query.first())" | python
User('Maros', 'maros@example.com', 'default.jpg')

echo -e "from flaskblog import db, User, Post\nprint(User.query.filter_by(username='Corey').all())" | python
[User('Corey', 'corey@example.com', 'default.jpg')]

echo -e "from flaskblog import db, User, Post\nprint(User.query.filter_by(username='Corey').first())" | python
User('Corey', 'corey@example.com', 'default.jpg')
```

Storing record in variables for processing.

```bash
# Filter by username and retrieve id
echo -e "from flaskblog import db, User, Post\nuser = User.query.filter_by(username='Corey').first()\nprint(f'User id is {user.id}')" | python
User id is 2

# Filter by id and retrieve id
echo -e "from flaskblog import db, User, Post\nuser = User.query.get(1)\nprint(f'User id is {user.id}')" | python
User id is 1

# Retrieve posts for user 1
echo -e "from flaskblog import db, User, Post\nuser = User.query.get(1)\nprint(f'User posts are {user.posts}')" | python
User posts are []
```

Create 2 records in `Post` table.

```bash
# Create first post
echo -e "from flaskblog import db, User, Post\nuser = User.query.get(1)\npost_1 = Post(title='Blog 1', content='First Post Content!', user_id=user.id)\ndb.session.add(post_1)\ndb.session.commit()" | python

# Create second post
echo -e "from flaskblog import db, User, Post\nuser = User.query.get(1)\npost_2 = Post(title='Blog 2', content='Second Post Content!', user_id=user.id)\ndb.session.add(post_2)\ndb.session.commit()" | python

# Retrieve posts for user 1
echo -e "from flaskblog import db, User, Post\nuser = User.query.get(1)\nprint(f'User posts are {user.posts}')" | python
User posts are [Post('Blog 1', '2021-06-27 19:28:42.600415'), Post('Blog 2', '2021-06-27 19:28:49.772034')]

echo -e "from flaskblog import db, User, Post\nuser = User.query.get(1)\nfor post in user.posts:\n   print(post.title)" | python
Blog 1
Blog 2

# Query post table directly
echo -e "from flaskblog import db, User, Post\npost = Post.query.first()\nprint(f'Post content is {post}')\nprint(f'User id of the post is {post.user_id}')" | python
Post content is Post('Blog 1', '2021-06-27 19:28:42.600415')
User id of the post is 1
```

### Database Record Cleanup

```bash
# Delete and recreate all tables
echo -e "from flaskblog import db\ndb.drop_all()" | python
echo -e "from flaskblog import db\ndb.create_all()" | python

# Verify table contents
echo -e "from flaskblog import db, User, Post\nprint(f'User Table Contents: {User.query.all()}')\nprint(f'Post Table Contents: {Post.query.all()}')" | python
User Table Contents: []
Post Table Contents: []
```

### Secret key and Database URI Configuration

The values for `SECRET_KEY` and `SQLALCHEMY_DATABASE_URI` have been moved from `config.py` file to environmental variables. In order to properly set the local database file and secret key, you need to make sure that the following system variables exists and are valid.

```bash
export SECRET_KEY='82e30eb9a16c095d5b504b44266b4d64'
export SQLALCHEMY_DATABASE_URI='sqlite:///site.db'
```


## Messaging

### Email Support

In order to use the **Forgot Password** feature, you need to make sure the following system variables exists and are valid.

```bash
# Example credentials
export EMAIL_USER=0foap20rsflakf
export EMAIL_PASS=opgkapojsgiwoa
```

These are being used to send outgoing email to SMTP server hosted at [mailtrap.io](https://mailtrap.io/)