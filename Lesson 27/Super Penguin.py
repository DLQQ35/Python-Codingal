class bird:
    def __init__(self):
        print("Bird is Ready.")
    def whoisthis(self):
        print("Bird.")
    def swim(self):
        print("Swim faster.")

class Penguin(bird):
    def __init__(self):
        super().__init__()
        print("Penguin is Ready.")
    def whoisthis(self):
        super().whoisthis()
        print("Penguin.")
    def run(self):
        print("Run faster.")

Peggy = Penguin()
Peggy.whoisthis()
Peggy.swim()
Peggy.run()