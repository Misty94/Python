import random

#get a rounded integer
random_int = random.random_int(1, 100)
print(random_int)


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

    def enroll(self,course):
        self.course = course
        instructor = random.choice(course.instructors)
        self.instructor = instructor
        return self

class Course:
    # next line is a class attribute - to keep track of 
    all_courses = []

    @classmethod
    def print_all_courses(cls):
        for course in cls.all_courses:
            print(course)


    def __init__( self, data ):
        self.name = data["name"]
        self.instructors = data["instructors"]
        self.program = data["program"]
        Course.all_courses.append(self)

    def print_instructor_list( self ):
        for instructor in self.instructors:
            print( instructor)
        #return self to enable chaining
        return self

    def update_instructor( self, new_name, index ):
        if index < len( self.instructors ):
            self.instructors[index] = new_name
        return self
    
    def print_info( self ):
        print( f"Program: {self.program}")
        print( f"Name: {self.name}")
        self.print_instructor_list()
    return self

    @staticmethod
    def determine_eligibility(age):
        if age >= 18:
            return True
        return False

# for debugging = string representation of our instance
    def __repr__(self):
        return f"{self.name} is a {self.program} program" 

python = {
    "name": "Python/Flask",
    "instructors": ["Alfredo Salazar", "Spencer Rauch", "Tyler Tybault"],
    "program": "Full stack"
}

java = {
    "name": "Java",
    "instructors": ["Alfredo Salazar", "Spencer Rauch", "Tyler Tybault"],
    "program": "Full stack"
}

mern = {
    "name": "MERN",
    "instructors": ["Alfredo Salazar", "Spencer Rauch", "Tyler Tybault"],
    "program": "Full stack"
}

course_python = Course( python )
course_python = Course( java )
course_python = Course( mern )

Course.print_all_courses()
print(Course.all_courses)

# Chaining
course_python.print_info().update_instructor("Ryan Mendez", 2).print_info()

# course_python.print_info()
# course_python.update_instructor("Ryan Mendez", 2)
# course_python.print_info()

# student_alex = __init__( )


# Creating an object / Making an instance of the Student class
student_alex = Student( "Alex", "Miller", 20, "Nichole", "Web Fundamentals" ) # now student_alex is an object
# student_martha = Student( "Martha", "Smith", 25, "Spencer", "Python")
student_martha = Student( "Martha", "Smith", 25, "Spencer", course_python)

if Course.determine_eligibility(student_alex.age):
    student_alex.enroll(course_java)
    print("Welcome to Java!")
else:
    print("I'm sorry, you're not quite old enough")

student_alex_print_info("After enrollment")

student_martha.course.print_instructor_list()

list_students = []
list_students.append( student_alex )
list_students.append( student_martha )

for student in list_students:
    student.print_info("Hey there!")

# print(student_alex)

student_alex.print_info("Hey there!")
student_martha.print_info( "Howdy!" )

print(student_alex.first_name, student_alex.last_name, student_alex.age)

student_martha.print_info("*****************").enroll.print_info(course_python).print_info("****After Enrollment*****")