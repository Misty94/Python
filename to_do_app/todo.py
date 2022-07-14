from mysqlconnection import connectToMySQL

class Todo:
    def __init__( self, data):
        # go to workbench & see columns inside of tables
        self.id = data['id']
        self.status = data['status']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def get_all ( cls ):
        query = "SELECT * "
        query += "FROM todos;"

        result = connectToMySQL('todos_db').query_db(query)# the data paramenter defaults to none

        # print(result)

        list_todos = []
        for todo in result:
            list_todos.append( cls(todo) )
        # print( list_todos )
        return list_todos

    @classmethod
    def create( cls, data ):
        query = "INSERT INTO todos( description, status, user_id ) "
        query += "VALUES( %(description)s, %(status)s, %(user_id)s );"

        result = connectToMySQL( 'todos_db' ).query_db(query, data)
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