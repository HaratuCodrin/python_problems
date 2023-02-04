

class UI:

    options = [
        ["################## Game Name ###################",
        "1. Start new game.",
        "2. Quit"],

        ["################## Game Name ###################",
        "1. Pick a color.",
        "2. Go Back to Main Menu",
        "3. Quit."],

        ["################## Game Name ###################",
        "1. Yellow",
        "2. Red",
        ],

    ]

    def __init__(self, state = 0):
        self.state = state

    def loop(self):
        while True:
            for option in self.options[self.state]:
                print(option)
        
            if self.state < 3:
                pass

