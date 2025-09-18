class India():
    def capital(self):
        print("New Delhi is the capital of India.")
    def language(self):
        print("Hindi is widely spoken in India.")
    def type(self):
        print("India is a developing country.")
class USA():
    def capital(self):
        print("Washington D.C is the capital of USA.")
    def language(self):
        print("English is widely spoken in USA.")
    def type(self):
        print("USA is a developed country.")

ind = India()
usa = USA()

for country in (ind,usa):
    country.capital()
    country.language()
    country.type()