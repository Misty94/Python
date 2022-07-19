from flask_app.config.mysqlconnection import connectToMySQL
# from flask_bcrypt import Bcrypt
# bcrypt = Bcrypt(app)

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save( cls, data ):
        query = "INSERT INTO users ( first_name, last_name, email, password, created_at, updated_at ) "
        query += "VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW() )"

        result = connectToMySQL( 'login_and_registration' ).query_db(query, data)
        return result