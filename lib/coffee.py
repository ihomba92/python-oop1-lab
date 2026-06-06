#!/usr/bin/env python3

class Coffee:
    def __init__ (self, size, price):
        self.size = size
        self.price = price
        
    @property
    def size (self):
        return self._size
        
    @size.setter
    def size (self, coffee_input):
        if coffee_input not in ["Small", "Medium", "Large"]:
            print ("size must be Small, Medium, or Large")
        else:
            self._size = coffee_input
            
    def tip (self):
        print("This coffee is great, here’s a tip!")
        self.price += 1