class ParkingGarage():
    # Constant
    current_ticket = { 'paid' : False, 'parking_number' : 0 }

    def __init__(self, tickets, parking_spaces):
        self.tickets = tickets
        self.parking_spaces = parking_spaces
        
    def takeTicket(self):
        if self.tickets and self.current_ticket['parking_number'] == 0:
            self.current_ticket['parking_number'] = self.tickets.pop(0)
            self.parking_spaces.pop(0)
            print("Parking spot claimed!")
        elif self.current_ticket['parking_number'] != 0:
            print("You already claimed a parking spot!")
        else:
            print("Sorry, the parking lot is full")

    def freeUpSpace(self):
        self.tickets.append(self.current_ticket['parking_number'])
        self.parking_spaces.append(self.current_ticket['parking_number'])
        self.current_ticket['parking_number'] = 0
        self.current_ticket['paid'] = False

    def payForParking(self):
        while self.current_ticket['paid'] == False and self.current_ticket['parking_number']:
            amount = input('Enter amount to pay (or type "back" to exit): ')
            if amount.isdigit():
                self.current_ticket['paid'] = True
                print("Ticket paid and you can park for 15 minutes!")
                break
            elif amount.lower() == 'back':
                break
            else:
                print('Please enter a valid ammount')
        else:
            if self.current_ticket['parking_number'] == 0:
                print("You have to park first before paying")
            else:
                print("You already paid for parking!")

    def leaveGarage(self):
        if self.current_ticket['paid'] == True:
            self.freeUpSpace()
            print("Thank you, have a nice day!")
        elif self.current_ticket['parking_number']:
            while True:
                amount = input('You have not yet paid for parking\nEnter amount to pay (or type "back" to exit): ')
                if amount.isdigit():
                    self.freeUpSpace()
                    print("Thank you, have a nice day!")
                    break
                elif amount.lower() == 'back':
                    break
        else:
            print("Thank you, have a nice day!")

tix_and_spaces = [i for i in range(1,101)]
my_parking_garage = ParkingGarage(tix_and_spaces, tix_and_spaces)

def parkCar():
    while True:
        user_input = input('\nHi, what do you want to do? (type "park", "pay", or "leave") ')
        if user_input.lower() == 'park':
            my_parking_garage.takeTicket()
            my_parking_garage.payForParking()
        elif user_input.lower() == 'pay':
            my_parking_garage.payForParking()
        elif user_input.lower() == 'leave':
            my_parking_garage.leaveGarage()
        else:
            print('Please enter a valid command')

parkCar()