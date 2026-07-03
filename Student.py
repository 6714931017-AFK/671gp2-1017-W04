from Program import Program

class Student:
    def __init__(self, std_id, firstname, lastname, program: Program):
        self.std_id = std_id              
        self.firstname = firstname        
        self.lastname = lastname         
        self.program = program              
        
    def __str__(self) -> str:
        return f"รหัส {self.std_id}: {self.firstname} {self.lastname} - สาขา {self.program.name_th}"