from UI import menu_instance 

if __name__ == "__main__":
    student_list = [
        {"P1":0, "P2":5, "P3":5},
        {"P1":4, "P2":6, "P3":10},
        {"P1":6, "P2":8, "P3":9},
        {"P1":4, "P2":10, "P3":5},
        {"P1":3, "P2":4, "P3":6},
        {"P1":8, "P2":4, "P3":4},
        {"P1":10, "P2":10, "P3":9},
        {"P1":3, "P2":9, "P3":10},
        {"P1":8, "P2":4, "P3":6},
        {"P1":9, "P2":6, "P3":8}
    ]
    
    while True:
        menu_instance(student_list)