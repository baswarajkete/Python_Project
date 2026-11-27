##Pydantic

class Student:
    def __init__(self,name: str,age: int,gpa:float):
        self.name = name
        self.age = age
        self.gpa = gpa
s = Student("Ram",'Twenty',10)
print(s.name, s.age, s.gpa)

