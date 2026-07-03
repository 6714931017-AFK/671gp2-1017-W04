class Building:
    def __init__(self, b_id, b_name):
        self.b_id = b_id                 
        self.b_name = b_name              

    def __str__(self) -> str:
        return f"{self.b_name} (อาคาร {self.b_id})"