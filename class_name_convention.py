class CustomerApp:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added product to ",self.name,self.lastName,"'s cart")

        
customer1 = CustomerApp()
customer1.name = "Napath"
customer1.lastName = "S"
customer1.addCart()