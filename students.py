class Students:
    def __init__(self, name, student_id, registered_courses):
        self.name = name
        self.student_id = student_id
        self.registered_courses = registered_courses
    
    def register_for_course(self, course_code):
        if course_code not in self.registered_courses:
            self.registered_courses.append(course_code)
            return self.registered_courses
        return f"Student {self.name} is already registered for {course_code}"
    
    def drop_course(self, course_code):
        if course_code in self.registered_courses:
            self.registered_courses.remove(course_code)
            return f"Student {self.name} dropped {course_code}"
        return f"Student {self.name} is not registered for {course_code}"
    
    def get_registered_courses(self):
        return self.registered_courses

    def __str__(self):
        return f"Student: {self.name} (Student ID: {self.student_id})"
    