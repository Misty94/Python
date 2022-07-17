from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__( self, data):
        # go to workbench & see columns inside of tables
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def get_all ( cls ):
        query = "SELECT * "
        query += "FROM users;"

        result = connectToMySQL('users_cr_schema').query_db(query)# the data paramenter defaults to none
        return result

    @classmethod
    def save( cls, data ):
        query = "INSERT INTO users( first_name, last_name, email, created_at, updated_at ) "
        query += "VALUES( %(first_name)s, %(last_name)s, %(email)s, NOW(), NOW() );"

        result = connectToMySQL( 'users_cr_schema' ).query_db(query, data)
        return result

    @classmethod
    def update_one( cls, data ):
        query = "UPDATE users "
        query += "SET first_name =%(first_name)s,last_name =%(last_name)s,email =%(email)s "
        query += "WHERE id = %(id)s;"

        return connectToMySQL( 'users_cr_schema' ).query_db(query, data)

    @classmethod
    def delete_one( cls, data ):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('users_cr_schema').query_db(query, data)

    @classmethod
    def get_one( cls, data ):
        query = "SELECT * "
        query += "FROM users "
        query += "WHERE id = %(id)s;"

        result = connectToMySQL( 'users_cr_schema' ).query_db(query, data)

        # if len(result) > 0:
        #     update_user = cls(result[0])

        return cls(result[0]) # result is a list

"""
SELECT
get_one()
get_all()

INSERT
create()
save()

UPDATE
update_one()
edit_one()

DELECT 
delete_one()
remove_one()
"""
