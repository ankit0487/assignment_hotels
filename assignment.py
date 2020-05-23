class Hotel:
    def __init__(self, hotel_name):
        self.hotel_name = hotel_name
        self.total_rooms = 0
        self.rooms = {}

    def addRoom(self, room):
        self.total_rooms += 1
        self.rooms[self.total_rooms] = room

class Room:
    def __init__(self, items):
        self.items = items
        self.price = sum(int(value) for key, value in items.items())

hotels = {}


def createHotel(hotel_name):
    hotels[hotel_name] = Hotel(hotel_name)
    print("hotel with name \"{0}\" created".format(hotel_name))


def createItem(items):
    print("item",len(items)+1)
    item_name = input("name: ")
    item_value = input("value: ")
    while item_value.isnumeric() == False:
        print("Value should be numeric!!")
        item_value = input("value: ")
    if item_name not in items.keys():
        items[item_name] = item_value
    else:
        print("Item already exists")
        createItem(items)


def addRoomToHotel():
    print("Select hotel: ")
    hotel_names = list(hotels.keys())
    for name in hotel_names:
        print("{0}-{1}".format(hotel_names.index(name), name))
    ch = input("Enter your choice: ")
    if (ch.isnumeric()) and int(ch) < len(hotels):
        hotel = hotels[hotel_names[int(ch)]]
        print("\nEnter five items along with its value in '$':\n")
        items = {}
        while len(items) < 5:
            createItem(items)
            print("\n")
        while input("do you want to add more item (y/n): ") == "y":
            createItem(items)
            print("\n")
        room = Room(items)
        hotel.addRoom(room)
        print("Room added to hotel \"{0}\"".format(hotel.hotel_name))
    else:
        print("\nInvalid Entry!! Try again\n")
        addRoomToHotel()
    

def printRooms():
    flag = 0
    for name, hotel in hotels.items():
        if len(hotel.rooms):
            flag=1
            print(name + " has following rooms:\n")
            for key, room in hotel.rooms.items():
                print(" Room"+repr(key)+"\nItems : values($)")
                for item, value in room.items.items():
                    print(item, " : ", value)
                print("\nPrice: $", room.price)
                print("-"*25)
    if flag == 0:
        print("---No rooms available---")


def searchRoomByBudget(budget):
    availablity = False
    printStatement = ""
    for name, hotel in hotels.items():
        printStatement += "\n\nHotel " + name + " has rooms :"
        for key, room in hotel.rooms.items():
            if room.price <= budget:
                availablity = True
                printStatement += "\nRoom{0} with items {1} and price: ${2}".format(key, ', '.join(room.items), room.price) 
    if availablity == False:
        print("---No rooms available under your budget---")
        return
    print(printStatement)  


def menu():
    while True:
        choice = input("*"*50+"\n Welcome, \n\n 1. Add a hotel \n 2. Add a room \n 3. Print rooms with item details"
         + " \n 4. Search room by budget \n 0. Exit\n\nEnter your choice: ")

        if choice == '0':
            return

        elif choice == '1':
            createHotel(input("Give name for the hotel: "))

        elif choice == '2':
            if len(hotels) == 0:
                print("No hotels created. Create atleast a hotel first")
                continue
            addRoomToHotel()

        elif choice == '3':
            printRooms()

        elif choice == '4':
            budget = input("Enter budget in '$': ")
            while budget.isnumeric() == False:
                print("budget value should be numeric!!")
                budget = input("Enter budget in '$': ")
            searchRoomByBudget(int(budget))
            
        else:
            print("Invalid choice!!! Try again")

menu()