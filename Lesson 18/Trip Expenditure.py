def hotelcost(days):
    return 9899*days

def planeridecost(city):
    if "raipur" == city:
        return 10000
    elif "bhopal" == city:
        return 12000
    elif "indore" == city:
        return 15000
    elif "bhubhneshwar" == city:
        return 14000

def rentalcarcost(days):
    if days >= 7:
        return 1000 * days - 100
    elif days >= 3:
        return 1000 * days - 50
    else:
        return 1000 * days

def tripcost(city, car, hotel, spendingmoney):
    return rentalcarcost(car) + planeridecost(city) + hotelcost(hotel) + spendingmoney

city = input("Indore, Bhopal, Raipur, Bhubhneshwar \nEnter the city:").lower()
car = int(input("For how many days do you want to book a car:"))
hotel = int(input("For how many days do you want to stay in hotel:"))

print("Cost of Rented Car:", rentalcarcost(car))
print("Cost of Aeroplane tickets:", planeridecost(city))
print("Cost of Hotel Room:", hotelcost(hotel))
print("The total cost is:", tripcost(city, car, hotel, 50000))