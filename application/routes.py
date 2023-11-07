from application import app, db
from flask import request, jsonify # request module allows you get data from http requests.jsonify used for json responses to convert.
from application.models import FriendsCharacter # import the class from models

def format_character(character):
    return {
        'name': character.name,
        'age': character.age,
        'catch_phrase': character.catch_phrase
    }

@app.route('/')
def hello_world():
    return '<p>Hello Welcome to the API dedicated to friends!</p>'


@app.route('/characters', methods=['POST']) # decorator
def create_character(): # this function is executed when a post request is made to '/characters' url
    data = request.json # this code retrieves the json data from the body. it parses it and stores it in data variable.
    character = FriendsCharacter(data['name'], data['age'], data['catch_phrase']) # new character object is created using the data variable
    db.session.add(character) # add the newly created character to the database.
    db.session.commit() # commit the newly created character to database.
    return jsonify(id=character.id, name=character.name, age=character.age, catch_phrase=character.catch_phrase) #return json response


@app.route('/characters', methods=['GET'])
def get_characters():
    characters = FriendsCharacter.query.all()
    character_list = []
    for character in characters:
        character_list.append(format_character(character))
    return {'characters': character_list}


@app.route('/characters/<id>', methods=['GET'])
def get_character(id):
    character = FriendsCharacter.query.filter_by(id=id).first()
    return jsonify(id=character.id, name=character.name, age=character.age, catch_phrase=character.catch_phrase)


@app.route('/characters/<id>', methods=['DELETE'])
def delete_character(id):
    character = FriendsCharacter.query.get(id)
    if character is None:
        return jsonify({'message': 'Character not found'}), 404
    db.session.delete(character)
    db.session.commit()
    return jsonify({'message': 'Character deleted'})
    
    

@app.route('/characters/<id>', methods=['PATCH'])
def update_character(id):
    character = FriendsCharacter.query.get(id) # get character with matching id
    if character is None:
        return jsonify({'message': 'Character not found'}), 404 # return an error if not found
    data = request.json # get the data from JSON request
    character.name = data.get('name', character.name) # update data
    character.age = data.get('age', character.age)
    character.catch_phrase = data.get('catch_phrase', character.catch_phrase)
    db.session.commit() # commit changes to database
    return jsonify({
        'id': character.id,
        'name': character.name,
        'age': character.age,
        'catch_phrase': character.catch_phrase
    }) # return JSON response



