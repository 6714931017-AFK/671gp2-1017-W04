from Program import Program

class Lecturer:
    def __init__(self, academic_position, firstname, lastname, program: Program):
        self.academic_position = academic_position  
        self.firstname = firstname                
        self.lastname = lastname                    
        self.program = program                    
        
    def __str__(self) -> str:
        return f"{self.academic_position}{self.firstname} {self.lastname} (สาขา{self.program.name_th})"
    