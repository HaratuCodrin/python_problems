
class Reservation:

    def __init__(self, id, start_date, end_date, room_number, name, number_of_guests):
        self.id = id
        self.start_date = start_date
        self.end_date = end_date
        self.room_number = room_number
        self.name = name
        self.number_of_guests = number_of_guests
    
    def get_row(self):
        return [str(self.start_date.day)+ "." + str(self.start_date.month) + " - " + str(self.end_date.day)+ "." + str(self.end_date.month), 
                self.name,
                str(self.number_of_guests) + " persons"]
