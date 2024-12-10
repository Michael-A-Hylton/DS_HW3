from Course import Course
from Student import Student

course1=Course("CS 365", "Data Science", 3.0, 1)
course1.printCourseInfo()
student1=Student("2788154","Michael Hylton")
student1.printStudentInfo()
student1.assignCourseGrade("CS 365", 4.0)
