class vehicle:

    def __init__(self,maxspeed,mileage):
        self.maxspeed=maxspeed
        self.mileage=mileage


ModelX = vehicle(551,74)

print("Max speed of ModelX is", ModelX.maxspeed ,"kmph.")
print("Mileage of ModelX is", ModelX.mileage, "km.")

