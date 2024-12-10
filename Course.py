class Course:

    instances =[]
    instances2=[]

    def __init__(self,courseID:str, courseName:str, creditHours:float, period:int):
        self.courseID=courseID
        self.courseName=courseName
        self.creditHours=creditHours
        self.period=period
        Course.instances2.append(self)
        Course.instances.append(courseID)
        Course.instances.append(courseName)
        Course.instances.append(creditHours)
        Course.instances.append(period)

    def printCourseInfo(self):
        print(self.courseID)
        print(self.courseName)
        print(self.creditHours)
        print(self.period)
        #print(''.join(str(Course.instances)))
        
