class student:
    def __init__(self, student_name, student_id, age, course):
        self.student_name = student_name
        self.student_id = student_id
        self.age = age
        self.course = []

    def __str__(self):
        message = (f"NAME: {self.name}\n ")
        (f"ID: {self.student_id}\n")
        (f"AGE: {self.age}\n")
        (f"COURSES: {self.course}") 
        return message
    
    def enroll(self, course):
        self.course.append(course)
        print(f"{self.name}, with ID, {self.student_id}, has been enrolled in {course}")
    
    def view_course(self):
        return self.course
        

class teacher:
    def __init__(self, teacher_name, teacher_id, subject, course):
        self.teacher_name = teacher_name
        self.teacher_id = teacher_id
        self.subject = subject
        self.course = []
    
    def assign_course(self, course):
        self.course.append(course)
        print(f"{self.name} with ID {self.teacher_id} has been assigned to the following courses {self.course}")
        
    def view_course(self):
        return self.course 
        

class course:
    def __init__(self, course_name, course_code, teacher):
        self.course_name = course_name
        self.course_code = course_code
        self.teacher = teacher
        self.student = []
    
    def add_student(self, student):
        self.student.append(student)
        print(f"{self.student} has been added to the following course {self.course_name} with course code {self.course_code}")
        
    def view_student(self):
        return self.student 
    

class school:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []
        self.courses = []
        
    def add_student(self, student):
        self.students.append(student)
        print(f"{student.name} has been added to the school students")
    
    def add_teacher(self, teacher):
        self.teachers.append(teacher)
        print(f"{teacher.name} has been added to the school teachers ")
    
    def add_course(self, course):
        self.courses.append(course)
        print(f"{course.name} has been added to the school courses")
        
    def view_all_student(self, student):
        return self.student
    
    def view_all_teacher(self, teacher):
        return self.teacher
    
    def view_all_course(self, course):
        return self.course