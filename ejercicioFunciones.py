

#diccionario de usuarios
users = {"admin" : "12345"}

#diccionario para almacenar motos
store_bike = {}

def login():
    print("Welcome store bike")
    user = input("User: : ")
    password = input("password: ")
    if user in users and password == users[user]:
        print("welcome " + user)
        return True
    else:
        print("User or pasword invalid")
        return False
    

def see_options():
    print("************OPTIONS************")
    print("1. Add Bike")
    print("2. see all Bike")
    print("3. search Bike")
    print("4. delete Bike")
    print("5. exit")

def add_Bike():
    print("************Add Bike*************")
    id_bike = input("ID Bike: ")
    brand = input("brand: ")
    ref = input("ref: ")
    year = input("year: ")
    store_bike[id_bike] = {"brand": brand, "ref": ref, "year": year}
    print("Motorcycle successfully added")

def see_bike():
    print("************See all Bike*************")
    for id_bike in store_bike:
        """print(store_bike.items)"""
        print("ID Bike: " + id_bike)
        print("brand: " + store_bike[id_bike]["brand"])
        print("ref: " + store_bike[id_bike]["ref"])
        print("year: " + store_bike[id_bike]["year"])
        print("**********************************")


def search_bike():
    print("************Search Bike*************")
    id_bike = input("ID Bike: ")
    if id_bike in store_bike:
        details = store_bike[id_bike]
        print("ID Bike: " + id_bike)
        print("brand: " + details["brand"])
        print("ref: " + details["ref"])
        print("year: " + details["year"])
    else:
        print("ID Bike not found")

def delete_bike():
    print("************Delete Bike*************")
    id_bike = input("ID Bike: ")
    if id_bike in store_bike:
        del store_bike[id_bike]
        print("ID Bike deleted")
    else:
        print("ID Bike not found")

def main():
    if login():
        while True:
            see_options()
            option = input("Enter your option: ")
            if option == "1":
                add_Bike()
            elif option == "2":
                see_bike()
            elif option == "3":
                search_bike()
            elif option == "4":
                delete_bike()
            elif option == "5":
                print("Bye")
                break
            else:
                print("Invalid option")

          

main()



        







    

