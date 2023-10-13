class Family:
    def __init__(self,name,address) -> None:
        self.name = name
        self.address = address

class school:
    def __init__(self,id,current_class) -> None:
        self.id = id
        self.current_class = current_class

class Sports:
    def __init__(self,game) -> None:
       self.game =game


class Student(Family,school,Sports):
    def __init__(self, name, address,id,current_class,game) -> None:
        school.__init__(self,id,current_class)
        Sports.__init__(self,game)
        super().__init__(name, address)
    
    def __repr__(self) -> str:
        
        return (f'Name : {self.name} address : {self.address} id : {self.id} class : {self.current_class} game : {self.game}')


My_student = Student('Md : hasan mia','chandpur',12,7,'criket')
print(My_student)
