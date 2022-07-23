from flask_app.models.recipe_model import Recipe
from flask import json, jsonify, request
from flask_app import app

# You must install flask-cors in the server: python -m pipenv install flask-cors
from flask_cors import cross_origin

@app.route('/api/recipes')
@cross_origin( origins = ['http://127.0.0.1:5500'] )
def api_get_recipes():
    # recipe = {
    #     "name": "Cookies"
    # }
    list_of_recipes = Recipe.api_get_all #not finished/not right!
    # you cannot send an object or a list of objects when using jsonify
    return jsonify( list_of_recipes ), 200
    # return jsonify( recipe ), 200 #this number is the status code / by default the status code is set to 200
    #200 means success

@app.route('/api/delete/recipe/<int:id>', methods=['DELETE'])
@cross_origin( origins = ['http://127.0.0.1:5500'] )
def api_delete_one(id):
    data = {
        "id": id
    }
    Recipe.delete_one(data)
    return jsonify ({}), 204
    # 204 means delete/no content

@app.route( '/api/add/todo', methods = ['POST'] )
@cross_origin( origins = ['http://127.0.0.1:5500'], headers = ['Content-type'] )
def api_add_one():
    new_recipe = json.loads( request.data.decode( 'UTF-8' ) ) 
    recipe_id = Recipe.create( new_recipe )
    data = {
        "id" : recipe_id,
        "message" : "recipe added successfully"
    }
    return jsonify( data ), 201