class Star_cinema:

    hall_list = []
    
    def entry_hall(self,entry):
        self.hall_list.append(entry)

class Hall(Star_cinema):

    def __init__(self,r,c,hall_no) -> None:
        self.seats = {}
        self.show_list = []
        self.r = r
        self.c = c
        self.hall_no = hall_no
        super().__init__()
    
    def entry_show(self,id,movie_name,movie_time):
        show_information = (id,movie_name,movie_time)
        self.show_list.append(show_information)

        self.seats[id] = {}
        for i in range(self.r):
            for j in range(self.c):
                self.seats[id][(i,j)] = False
    
    def booking_cinema_seat(self,id,seat_list):

        if id not in self.seats:
            print("Sorry ,ID Don,t match !!!!!")
            return
        

        
        for r,c in seat_list:
        
            if (r, c) in self.seats[id]: 
                if not self.seats[id][(r, c)]:
                    self.seats[id][(r,c)] = True
                    print(f"{r} row and {c} colum is booking successfully !!!")
                else:
            
                    print(f"{r} row and {c} colum is already booking !!!")
            else:
                print("Sorry ,Our cinema Hall seats is Housefull !!!")  

            for i in range(self.r):
                for j in range(self.c):
                    if not self.seats[id][(i,j)]:
                        print("0",end=" ")
                    else:
                        print("1",end=" ")
                print()      






print("!!!----WELCOME  FOR YOU COMING TO OUR CINEMA HALL-----!!! \n\n")


hall = Hall(20,20 ,1)
hall.entry_show(111, 'Adventure movie ', '12:00 PM 10-12-2023')
hall.entry_show(222, 'Ms dhoni movie ', '12:00 PM 10-12-2023')


print("---------------------------------")
print("Option 1 : Currently Running Movie !!")
print("Option 2 : Booking Cinema Seat !!")
print("Option 3 : Currently available Seat !!")
print("Exit Your Progam !!")
print("-----------------------------------")




while True:
    op = int(input("Please Choose Your option : "))
    print("\n")
    if op == 1:
        for id, movie_name, movie_time in hall.show_list:
            print(f"Movie id: '{id}' Movie Name : '{movie_name}' Movie Time : '{movie_time}' \n")
    elif op == 2:
        id = int(input("Movie id above plase watch : "))
        row = int(input("Enter You row number (0-19): "))
        col = int(input("Enter You colum number (0-19): "))
        hall.booking_cinema_seat(id,[(row,col)])
    
    elif op == 3:
        id = int(input("Enter Your show  Movie  id and available seats : "))
        for i in range(hall.r):
            for j in range(hall.c):
                if not hall.seats[id][(i,j)]:
                    print(f"current available seat {i} {j}")
    elif op == 4:
        print("bhai abar amader ei cinema hall e !!!")
        break






