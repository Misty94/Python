from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE
from flask_app.models.user_model import User

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_cooked = data['date_cooked']
        self.under_30 = data['under_30']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO recipes ( name, description, instructions, date_cooked, under_30, user_id, created_at, updated_at ) "
        query += "VALUES ( %(name)s, %(description)s, %(instructions)s, %(date_cooked)s, %(under_30)s, %(user_id)s, NOW(), NOW() );"

        return connectToMySQL( DATABASE ).query_db(query, data)

    @classmethod
    def get_all_with_users(cls):
        query = "SELECT * "
        query += "FROM recipes "
        query += "JOIN users "
        query += "ON recipes.user_id = users.id;"

        results = connectToMySQL( DATABASE ).query_db(query)
        print(results)

        list_of_recipes = []

        for row in results:
            current_recipe = cls(row)
            user_data = {
                **row,
                "created_at": row['users.created_at'],
                "updated_at": row['users.updated_at'],
                "id": row['users.id']
            }
            current_user = User(user_data)
            current_recipe.user = current_user #this attaches the user to the recipe
            list_of_recipes.append(current_recipe)

        return list_of_recipes

    @classmethod
    def get_one_with_users(cls, data):
        query = "SELECT * "
        query += "FROM recipes "
        query += "JOIN users "
        query += "ON recipes.user_id = users.id "
        query += "WHERE recipes.id = %(id)s;"

        results = connectToMySQL( DATABASE ).query_db(query, data)
        current_recipe = cls(results[0])
        user_data = {
            **results[0],
            "created_at": results[0]['users.created_at'],
            "updated_at": results[0]['users.updated_at'],
            "id": results[0]['users.id']
        }
        current_recipe.user = User(user_data)
        return current_recipe

    @classmethod
    def update_one(cls, data):
        query = "UPDATE recipes "
        query += "SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, "
        query += "date_cooked = %(date_cooked)s, under_30 = %(under_30)s, updated_at = NOW() "
        query += "WHERE id = %(id)s;"

        return connectToMySQL( DATABASE ).query_db(query, data)

    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM recipes "
        query += "WHERE id = %(id)s;"

        return connectToMySQL( DATABASE ).query_db(query, data)

    @staticmethod
    def validate_recipe(data):
        is_valid = True

        if len(data['name']) < 3:
            flash("Your name needs to be at least 3 characters long.", "error_recipe_name")
            is_valid = False
        if len(data['description']) < 3:
            flash("Your description needs to be at least 3 characters long.", "error_recipe_description")
            is_valid = False
        if len(data['instructions']) < 3:
            flash("Your instructions need to be at least 3 characters long.", "error_recipe_instruction")
            is_valid = False
        if data['date_cooked'] == "":
            flash("Date must not be blank.", "error_recipe_date_cooked")
            is_valid = False
        
        return is_valid