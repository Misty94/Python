
# a Method is a function inside a class
# Class is like the blueprint
class Student: # begin with an uppercase letter
    # Constructor
    def __init__( self, first_name, last_name, age, instructor, course ):
        # Attributs (characteristics)
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.instructor = instructor
        self.course = course
    #Method
    def print_info( self, message ):
        print( message )
        print( f"Name: {self.first_name} {self.last_name}")
        print ( f"Age: {self.age}")
        print ( f"Instructor: {self.instructor}")
        print ( f"Course: {self.course}")

class Course:
    def __init__( self, data ):
        self.name = data["name"]
        self.instructors = data["instructors"]
        self.program = data["program"]

    def print_instructor_list( self ):
        for instructor in self.instructors:
            print( instructor)

    def update_instructor( self, new_name, index ):
        if index < len( self.instructors ):
            self.instructors[index] = new_name
    
    def print_info( self ):
        print( f"Program: {self.program}")
        print( f"Name: {self.name}")
        self.print_instructor_list()

python = {
    "name": "Python/Flask",
    "instructors": ["Alfredo Salazar", "Spencer Rauch", "Tyler Tybault"],
    "program": "Full stack"
}

course_python = Course( python )

course_python.print_info()
course_python.update_instructor("Ryan Mendez", 2)
course_python.print_info()

# student_alex = __init__( )


# Creating an object / Making an instance of the Student class
student_alex = Student( "Alex", "Miller", 20, "Nichole", "Web Fundamentals" ) # now student_alex is an object
student_martha = Student( "Martha", "Smith", 25, "Spencer", "Python")

list_students = []
list_students.append( student_alex )
list_students.append( student_martha )

for student in list_students:
    student.print_info("Hey there!")

# print(student_alex)

student_alex.print_info("Hey there!")
student_martha.print_info( "Howdy!" )

print(student_alex.first_name, student_alex.last_name, student_alex.age)