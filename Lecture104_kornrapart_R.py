class Customer:
    name = ""
    lastName = ""
    age = 0
    def addCart(self):
        print("Added to",self.name,self.lastName,"'s cart")

customer1 = Customer()
customer1.name = "Kornrapart"
customer1.lastName = "Rungsiwattana"
customer1.addCart()

customer2 = Customer()
customer2.name = "Pisit"
customer2.lastName = "Rungsiwattana"
customer2.addCart()

customer3 = Customer()
customer3.name = "Woranit"
customer3.lastName = "Rungsiwattana"
customer3.addCart()

customer4 = Customer()
customer4.name = "Nisarat"
customer4.lastName = "Rungsiwattana"
customer4.addCart()