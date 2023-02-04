

class UI:

    options = [
        ["################## Hotel Transilvania ###################",
        "1. Make a new Reservation",
        "2. Quit"],

        ["################## Hotel Transilvania ###################",
        "1. Input your reservation data.",
        "2. Go Back to Main Menu",
        "3. Quit."],

        ["################## Hotel Transilvania ###################",
        "1. Yellow",
        "2. Red",
        ],

    ]

    def __init__(self, hotel, state = 0):
        self.state = state
        self.hotel = hotel

    def loop(self):
        while True:
            for option in self.options[self.state]:
                print(option)
        
            if self.state < 3:
                pass

