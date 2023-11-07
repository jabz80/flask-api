from application import db, app

app.app_context().push()

class FriendsCharacter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    catch_phrase = db.Column(db.String(200), nullable=False)

    def __init__(self, name, age, catch_phrase):
        self.name = name
        self.age = age
        self.catch_phrase = catch_phrase

    def __repr__(self):
        return f'My name is {self.name} and my catch phrase is {self.catch_phrase}'
    



# from application import db, app - import the app and db instances from __init__.py from application module.
# app.app_context().push() - This is necessary when working with SQLAlchemy models. It allows you to access/interact with the database.
# class FriendsCharacter(db.Model): - creates a class that inherits from db.model.
# id, name, age and catch_phrase - represent the columns in the database table.
# nullable=False) - means that the columns cannot have null values.
# def __init__(self, name, age, catch_phrase): - constructor of the class

# The purpose of this code is to define a database model for storing information about "Friends" characters, such as their name, age, and catch phrase. use this model to create, read, update, and delete records in the database, allowing you to store and retrieve data related to "Friends" characters within your Flask application.

