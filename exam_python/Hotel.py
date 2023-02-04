from prettytable import PrettyTable
from datetime import date, datetime, timedelta
from random import choice, random, randint
from reservation_class import Reservation

class Hotel:
    reservations = []
    configuration = {}
    id_counter = 0
    first_names = ["Cezar", "Paula", "Rares", "Codrin", "Cosmin", "Radu", "Iulia", "Amalia", "Ioana", "Andrei", "Iustin", "Marta", "Ines", "Rakan"]
    last_names = ["Popescu", "Colesa", "Donisanu", "Ciocoiu", "Mihu", "Marginean", "Pristavu", "Acatincai", "Gomez", "Ciolac", "DiCaprio"]

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
        return True
    
    def make_reservation(self, name, number_of_guests, start_date, end_date):
        room_number = 0
        possible_room_numbers = []
        if number_of_guests >= 3:
            possible_room_numbers.append("3")
        elif number_of_guests > 0 and number_of_guests < 3:
            possible_room_numbers.append("1")
            possible_room_numbers.append("2")
            possible_room_numbers.append("4")
            possible_room_numbers.append("5")
        
        for number in possible_room_numbers:
            available = self.check_if_room_available(number, start_date, end_date)
            if available:
                room_number = number
                break
        
        if available:
            reservation = Reservation(self.id_counter, start_date, end_date, room_number, name, number_of_guests)
            self.reservations.append(reservation)
            self.id_counter += 1
            return reservation
        else:
            return False
        

    def generate_reservations(self):
        fichier = open("generated_reservations.txt", "w")
        full_names = []
        for i in range(0, 100):
            first_name = choice(self.first_names)
            last_name = choice(self.last_names)
            full_names.append(first_name + " " + last_name)
        start = date(2023, 1, 1)
        end = date(2023, 12, 29)
       
        for name in full_names:
            day = randint(1,28)
            month = randint(1,12)
            random_date = date(2023, month, day)
            delta = timedelta(days=3)
            end_date = random_date + delta
            res = self.make_reservation(name, randint(1,4), random_date, end_date)

            while not res:
                day = randint(1,28)
                month = randint(1,12)
                random_date = date(2023, month, day)
                delta = timedelta(days=3)
                end_date = random_date + delta
                res = self.make_reservation(name, randint(1,4), random_date, end_date)
            
            fichier.write(str(res.id) + " " + str(res.name) + " " +
                            res.room_number + " " + str(res.number_of_guests) + " " +
                            str(res.start_date) + " " + str(res.end_date) + "\n")

    def read_reservations(self):
        file = open("generated_reservations.txt", "r")

        for line in file.readlines():
            data = line.split()
            date1 = data[5].split("-")
            date2 = data[6].split("-")
            self.make_reservation(data[1] + " " + data[2], int(data[4]), date(int(date1[0]), int(date1[1]), int(date1[2])),
             date(int(date1[0]), int(date2[1]), int(date2[2])))
            
            
    def display_month(self, month):
        table = PrettyTable([month, "Name", "Guests"])
        for reservation in self.reservations:
            if reservation.start_date.month == int(month):
                table.add_row(reservation.get_row())
        print(table)



    def __init__(self):
        self.read_room_conf()
        self.read_reservations()
        self.display_month("2")