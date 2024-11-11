class Star_Cinema:
    hall_list = []

    def entry_hall(self):
        Star_Cinema.hall_list.append(self)

class Hall(Star_Cinema):
   
    def __init__(self,rows,cols,hall_no):
        self.__seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.entry_hall()

    def book_seats(self,id,rows,cols):
        if id in self.__seats:
            if rows<=self.rows and cols<=self.cols:
                if self.__seats[id][rows-1][cols-1]=='0':
                    self.__seats[id][rows-1][cols-1]='1'
                    print('Ok, seat is booked for you.')  
                else:
                    print('Seat is already booked')
            else: 
                print('Invalid seat number.')
        else:
            print('Show ID is not found.')

    def entry_show(self,id,movie_name,time):
        self.id=id
        self.movie_name=movie_name
        self.time=time
        show=(id,movie_name, time)
        self.show_list.append(show)
        self.__seats[id]=[['0' for _ in range(self.cols)] for _ in range(self.rows)]

    def view_show_list(self):
        for i in self.show_list:
            print(f'ID: {i[0]}, Movie name: {i[1]}, Time: {i[2]}')

    def view_available_seats(self,id):
        if id in self.__seats:
            print(f'Available seats for show ID {id}: ')
            for i in self.__seats[id]:
                print(i)
        else:
            print('Show ID not found.')

    def _repr_(self):
        return f'Hall No: {self.hall_no},Rows: {self.rows},Cols: {self.cols}'

cinema = Star_Cinema()
ccnema = Hall(20,20,1)

ccnema.entry_show(1,'Spider Man No Way Home','7:00PM')
ccnema.entry_show(2,'The Batman','9:00PM')

run=True
while run:
    print('1. View all shows today')
    print('2. View available seats')
    print('3. Book a ticket')
    print('4. Exit')
    
    x=int(input('Enter option: '))
    
    if x==1:
        print('-------------------------------------------------------')
        ccnema.view_show_list()
        print('-------------------------------------------------------')
    
    elif x==2:
        xx=int(input('Enter show ID to view available seats: '))
        ccnema.view_available_seats(xx)
    
    elif x==3:
        x1=int(input('Enter show ID to book a ticket: '))
        r=int(input('Enter row number: '))
        c=int(input('Enter col number: '))
        ccnema.book_seats(x1,r,c)
    
    elif x==4:
        run=False
        print('Exit.')
    
    else:
        print('Invalid.')
