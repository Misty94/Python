from mysqlconnection import connectToMySQL

class User:
    def __init__( self, data):
        # go to workbench & see columns inside of tables
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all ( cls ):
        query = "SELECT * "
        query += "FROM users;"

        result = connectToMySQL('users_cr_schema').query_db(query)# the data paramenter defaults to none
        return result

        # print(result)

        # list_todos = []
        # for todo in result:
        #     list_todos.append( cls(todo) )
        # # print( list_todos )
        # return list_todos

    @classmethod
    def save( cls, data ):
        query = "INSERT INTO users( first_name, last_name, email, created_at, updated_at ) "
        query += "VALUES( %(first_name)s, %(last_name)s, %(email)s, NOW(), NOW() );"

        result = connectToMySQL( 'users_cr_schema' ).query_db(query, data)
        return result

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
