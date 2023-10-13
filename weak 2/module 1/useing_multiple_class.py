""" 
1.class student 
2.class tcecher 
3.class 
"""

class Student:
    def __init__(self,name,current_class,id):
        self.name = name
        self.current_class = current_class
        self.id = id
        
    def __repr__(self) -> str:
        return f'Stuent with name : {self.name} and current class : {self.current_class} and id number : {self.id}'


class Techers:
    def __init__(self,name,subject,id):
        self.name = name
        self.subject = subject
        self.id = id
    
    def __repr__(self) -> str:
        return f"Teacher With name : {self.name} and Subject : {self.subject} and  id number : {self.id}"
    
class School:
    def __init__(self,name):
        self.name = name
        self.teachers = []
        self.stuednts = []
    

    def add_to_teacher(self,name,subject):
        id = len(self.teachers) + 100
        teacher = Techers(name,subject,id)
        self.teachers.append(teacher)

    def enrollment (self,name,fee):
        if fee < 6500:
            print(f"name : {name} No,engouh fee")
        else:

            id = len(self.stuednts) + 1
            student = Student(name,'c',id)
            self.stuednts.append(student)
            print(f"name : {name} is eroll and id : {id} extra menoy : {fee - 6500}")
    def __repr__(self) -> str:
        print('Welcome ',self.name)
        print("------ OUR TEACHER--------")

        for teacher in self.teachers:
            print(teacher)

        print("------OUR STUDENT------")
        for student in self.stuednts:
            print(student)
        return 'Almost erollment closed'



# Hero_almo = Student("Hero almo",9,1)
# Afran_Nisio = Techers('Afran Nisio','alog',101)
# print(Afran_Nisio)
# print(Hero_almo)

gk_high_school = School("Gridkalindia high school ")

gk_high_school.enrollment('Md: Hasan khan ',7000)
gk_high_school.enrollment('Md:sakib khan',9000)
gk_high_school.enrollment('Md:Akas hasan',5300)

gk_high_school.add_to_teacher('Md:Rubel khan','Pysices')
gk_high_school.add_to_teacher('Md:abdul kuddos','BGS')
gk_high_school.add_to_teacher('Md:Foysal saheb','bangla')

print(gk_high_school)