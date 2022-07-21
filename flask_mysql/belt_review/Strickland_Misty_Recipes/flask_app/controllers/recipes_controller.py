from pydoc import render_doc
from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.recipe_model import Recipe

@app.route('/recipes')
def display_all_recipes():

    if 'email' not in session:
        return redirect('/')

    list_of_recipes = Recipe.get_all_with_users()

    return render_template("all_recipes.html", list_of_recipes = list_of_recipes)


@app.route('/recipes/new')
def display_new_recipe():

    if 'email' not in session:
        return redirect('/')

    return render_template("new_recipe.html")

@app.route('/create/recipe', methods=['POST'])
def process_new_recipe():
    if Recipe.validate_recipe(request.form) == False:
        return redirect('/recipes/new')
    
    data = {
        **request.form,
        "user_id": session['user_id']
    }
    Recipe.save(data)
    return redirect('/recipes')


@app.route('/recipes/<int:id>')
def display_one_recipe(id):

    if 'email' not in session:
        return redirect('/')
    
    data = {
        "id": id
    }
    current_recipe = Recipe.get_one_with_users(data)
    return render_template("one_recipe.html", current_recipe = current_recipe)


@app.route('/recipes/edit/<int:id>')
def display_edit_page(id):

    if 'email' not in session:
        return redirect('/')

    data = {
        "id": id
    }
    current_recipe = Recipe.get_one_with_users(data)
    return render_template("edit_recipe.html", current_recipe = current_recipe)


@app.route('/update/recipe/<int:id>', methods=['POST'])
def process_update(id):
    if Recipe.validate_recipe(request.form) == False:
        return redirect(f'/recipes/edit/{id}')

    recipe_data = {
        **request.form,
        "id": id
    }
    Recipe.update_one(recipe_data)
    return redirect('/recipes')


@app.route('/recipes/<int:id>/delete')
def delete_one(id):
    data = {
        "id": id
    }
    Recipe.delete_one(data)
    return redirect('/recipes')
