class ParkingGarage:
    def __init__(self):
        self.tickets = []
        self.parkingSpaces = list(range(10))
        self.currentTicket = {"paid": False}

    def takeTicket(self):
        while True:
            if self.parkingSpaces:
                self.parkingSpaces.pop()
                self.tickets.append({"paid": False})
                print("Ticket taken. Don't forget to pay before you.")
                user_input = input("Do you want to take another ticket, pay, leave, or quit? (take/pay/leave/quit): ")
                if user_input == "take":
                    self.takeTicket()
                elif user_input.lower() == "pay":
                    self.payTicket()
                elif user_input.lower() == "leave":
                    self.leaveGarage()
                elif user_input.lower() == "quit":
                    break
            else:
                print("Parking garage is full.")
                user_input = input("Do you want to pay a ticket, leave, or quit? (pay/leave/quit): ")
                if user_input == "pay":
                    self.payTicket()
                elif user_input.lower() == "leave":
                    self.leaveGarage()
                elif user_input.lower() == "quit":
                    break

    def payTicket(self):
        while True:
            if self.tickets:
                print("Current unpaid tickets:")
                for i, ticket in enumerate(self.tickets):
                    if not ticket["paid"]:
                        print(f"{i+1}. Ticket {i+1}")
                user_input = input("Enter the number of the ticket to pay: ")
                try:
                    ticket_number = int(user_input)
                    if ticket_number <= len(self.tickets) and not self.tickets[ticket_number-1]["paid"]:
                        amount_paid = float(input("Enter the amount to pay ($5 for ticket fee): "))
                        if amount_paid == 5:
                            self.tickets[ticket_number-1]["paid"] = True
                            print("Ticket paid.")
                        elif amount_paid > 5:
                            change = amount_paid - 5
                            print(f"Change: ${change:.2f}")
                            self.tickets[ticket_number-1]["paid"] = True
                            print("Ticket paid.")
                        else:
                            print("Insufficient payment. Please pay the full fee.")
                            continue
                        user_input = input("Do you want to pay another ticket, take another ticket, or leave or quit? (pay/leave/quit): ")
                        if user_input.lower() == "take":
                            self.takeTicket()
                        if user_input.lower() == "pay":
                            self.payTicket()
                        elif user_input.lower() == "leave":
                            self.leaveGarage()
                        elif user_input.lower() == "quit":
                            break
                except ValueError:
                    print("Invalid ticket number. Please enter a valid ticket number.")
            else:
                print("No unpaid tickets.")
                user_input = input("Do you want to take a ticket? (yes/no/quit): ")
                if user_input.lower() == "yes":
                    self.takeTicket()
                elif user_input.lower() == "no":
                    self.leaveGarage()
                if user_input.lower() == "quit":
                    break

    def leaveGarage(self):
        while True:
            if self.tickets:
                print("Current unpaid tickets:")
                paid_tickets = [ticket for ticket in self.tickets if ticket["paid"]]
                print(f"Number of paid tickets: {len(paid_tickets)}")
                for i, ticket in enumerate(self.tickets):
                    if not ticket["paid"]:
                        print(f"{i+1}. Ticket {i+1}")
                user_input = input("Enter the number of the ticket to leave: ")
                ticket_number = int(user_input)
                if ticket_number <= len(self.tickets):
                    ticket = self.tickets[ticket_number-1]
                    if not ticket["paid"]:
                        print("Please pay the ticket fee.")
                        self.payTicket()
                    else:
                        self.parkingSpaces.append(ticket_number-1)
                        self.tickets.pop(ticket_number-1)
                        print("Ticket left. Thank you for using the parking garage.")
                        print("Have a nice day!")
                        user_input = input("Do you want to take a ticket another ticket, or pay (take/pay/quit): ")
                        if user_input.lower() == "take":
                            self.takeTicket()
                        elif user_input.lower() == "pay":
                            self.payTicket()
                        elif user_input.lower() == "quit":
                            break
            else:
                print("No unpaid tickets.")
                user_input = input("Do you want to take a ticket or pay another ticket? (yes/no/quit): ")
                if user_input.lower() == "yes":
                    self.takeTicket()
                elif user_input.lower() == "no":
                    self.leaveGarage()
                elif user_input.lower() == "pay":
                    self.payTicket()
                elif user_input.lower() == "quit":
                    break

    def getUserInput(self):
        user_input = input("do you want to take a ticket, pay, or leave: ")
        if user_input == "take":
            self.takeTicket()
        elif user_input == "ticket":
            self.takeTicket()
        elif user_input == "pay":
            ticket_index = int(input("Enter the index of the ticket to pay: "))
            self.payTicket(ticket_index)
        elif user_input == "leave":
            ticket_index = int(input("Enter the index of the ticket to leave: "))
            self.leaveGarage(ticket_index)

# Example usage
parking_garage = ParkingGarage()
parking_garage.getUserInput()
