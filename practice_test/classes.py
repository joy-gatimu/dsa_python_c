class Product: 
    #constructor
    def __init__(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price
    
    def get_name(self):
        return self.product_name
    
    def get_name(self,name):
         self.product_name=name
        
p1= Product("laptop",90000)
print(p1.product_name)
print(p1.get_name)
p1.set_name("Tablet")
print(p1.get_name())

p2=Product("Phone",135000)

        