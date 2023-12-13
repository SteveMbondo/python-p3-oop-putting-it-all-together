#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self._size = size
        self.brand = brand
        
    
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            print("size must be an integer")
        else:
            return self._size
        
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = 'New'

shoe = Shoe("Adidas", 9)
shoe.brand
shoe.size
shoe.cobble()
shoe.condition