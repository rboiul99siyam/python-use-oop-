# """ 
# 1.air port mangement system 
# 2.fight
# 3.passanger
# 4.terminal
# 5.airport
# """

class Passenger:
    def __init__(self, name, passport_number) -> None:
        self.name = name
        self.passport_number = passport_number
    
    # def __repr__(self) -> str:
    #     return f"name: {self.name} and passport number: {self.passport_number}\n"

class Flight:
    def __init__(self, flight_name, destination, departure_time) -> None:
        self.flight_name = flight_name
        self.destination = destination
        self.departure_time = departure_time
        self.passengers = []
    
    def add_passenger(self, passenger):
        self.passengers.append(passenger)
    
    # def __repr__(self) -> str:
    #     return f'flight name: {self.flight_name}, destination: {self.destination}, departure time: {self.departure_time}\n'

class Terminal:
    def __init__(self, name) -> None:
        self.name = name
        self.flights = []
    
    def add_flight(self, flight):
        self.flights.append(flight)

class Airport:
    def __init__(self, name) -> None:
        self.name = name
        self.terminals = []
    
    def add_terminal(self, terminal):
        self.terminals.append(terminal)

passenger1 = Passenger("Md hasan", 2303489238)
passenger2 = Passenger("Md garbij khan", 9873348792)

flight1 = Flight("F2329", 'New York', '20-12-2023 10:00 PM')
flight2 = Flight('F879', 'Oman', '24-12-2023 10:20 PM')

flight1.add_passenger(passenger1)
flight2.add_passenger(passenger2)

terminal1 = Terminal("Terminal 1")
terminal2 = Terminal("Terminal 2")

airport1 = Airport("My Airport")

airport1.add_terminal(terminal1)
airport1.add_terminal(terminal2)

print(f'{airport1.name} Airport')

for terminal in airport1.terminals:
    print(f"{terminal}")
    