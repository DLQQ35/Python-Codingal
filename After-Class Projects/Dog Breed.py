class dogs:

    species ="Dog"
    def __init__(self,name,color,height):
        self.name=name
        self.color=color
        self.height=height

German_Shephard = dogs("German Shephard","Brown","2 feet")
Pitbull = dogs("Pitbull","white","1 feet 8 inches")

print("German Shephard is a",German_Shephard.species)
print("Pitbull is a",Pitbull.species)

print(German_Shephard.name," is ",German_Shephard.color," and is ",German_Shephard.height," tall.")
print(Pitbull.name," is ",Pitbull.color," and is ",Pitbull.height," tall.")