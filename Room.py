from Building import Building

class Room:
    def __init__(self, room_id, room_name, building: Building):
        self.room_id = room_id          
        self.room_name = room_name        
        self.building = building         

    def __str__(self) -> str:
        return f"ห้อง {self.room_id} ({self.room_name}) ณ {self.building}"