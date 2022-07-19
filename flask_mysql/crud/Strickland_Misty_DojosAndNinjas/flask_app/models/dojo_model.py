from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja_model import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all( cls ):
        query = "SELECT * "
        query += "FROM dojos;"

        result = connectToMySQL( 'dojos_and_ninjas_schema' ).query_db(query)
        return result

    @classmethod
    def save( cls, data ):
        query = "INSERT INTO dojos ( name, created_at, updated_at ) "
        query += "VALUES ( %(name)s, NOW(), NOW() );"

        result = connectToMySQL( 'dojos_and_ninjas_schema' ).query_db(query, data)
        return result

    @classmethod
    def get_one_with_ninjas( cls, data ):

        query = "SELECT * "
        query += "FROM dojos "
        query += "LEFT JOIN ninjas "
        query += "ON dojos.id = ninjas.dojo_id "
        query += "WHERE dojo_id = %(id)s;"
        # query = "SELECT ninjas.first_name, ninjas.last_name, ninjas.age "
        # query += "FROM ninjas "
        # query += "LEFT JOIN dojos "
        # query += "ON dojos.id = ninjas.dojo_id "
        # query += "WHERE dojo_id = %(id)s;"

        result = connectToMySQL( 'dojos_and_ninjas_schema' ).query_db(query, data)
        
        dojo = cls(result[0])

        for row_from_db in result:

            ninja_data = {
                "id": row_from_db["ninjas.id"],
                "first_name": row_from_db["first_name"],
                "last_name": row_from_db["last_name"],
                "age": row_from_db["age"],
                "created_at": row_from_db["ninjas.created_at"],
                "updated_at": row_from_db["ninjas.updated_at"]
            }

            dojo.ninjas.append( Ninja( ninja_data ) )

        return dojo