
class Student:
    from Course import Course
    courseGrades: list[tuple[str,float]]
    def __init__(self,studentID:str, studentName:str):
        self.studentID=studentID
        self.studentName=studentName
        self.courseGrades=[]

    def printStudentInfo(self):
        print(self.studentID)
        print(self.studentName)

    def assignCourseGrade(self, courseID:str, grade:float):
        gradeAndId=(courseID,grade)
        self.courseGrades.append(gradeAndId)
