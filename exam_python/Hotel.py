from prettytable import PrettyTable
from datetime import date
from random import choice
from reservation_class import Reservation

class Hotel:
    reservations = []
    configuration = {}
    id_counter = 0
    first_names = ["Cezar", "Paula", "Rares", "Codrin", "Cosmin", "Radu", "Iulia", "Amalia", "Ioana", "Andrei", "Iustin"]
    last_names = ["Popescu", "Colesa", "Donisanu", "Ciocoiu", "Mihu", "Marginean", "Pristavu", "Acatincai", "Gomez", "Ciolac"]

    def read_room_conf(self):
        file = open("rooms.txt", "r")
        lines = file.readlines()
        for line in lines:
            data = line.split()
            self.configuration[data[0]] = data[1]

    def check_if_room_available(self, room_number, start_date, end_date):
        for reservation in self.reservations:
            if reservation.room_number == room_number:
                if start_date >= reservation.start_date and start_date <= reservation.end_date:
                    return False
                if end_date >= reservation.start_date and end_date <= reservation.end_date:
                    return False
    
    def make_reservation(self, room_number, name, number_of_guests, start_date, end_date):
        available = self.check_if_room_available(room_number, start_date, end_date)
        if available:
            self.reservations.append(Reservation(self.id_counter, start_date, end_date, room_number, name, number_of_guests))
            self.id_counter += 1
            return True
        else:
            return False
        

    def generate_reservations(self):
        full_names = " ".join(choice(self.first_names)+" "+choice(self.last_names) for _ in range(100)) 
        



    def __init__(self):
        self.read_room_conf()
        self.generate_reservations()
        pass