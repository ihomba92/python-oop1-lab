#!/usr/bin/env python3

class Book:
    def __init__ (self, title, page_count):
        self.title = title
        self.page_count = page_count
        self.current_page = 1
    
    #use a decorator
    @property
    def page_count(self):
        return self._page_count
    #the setter controls what happens when someine modifies the value
    @page_count.setter
    def page_count (self, value):
        if not isinstance (value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value
    def turn_page (self):
        if self.current_page < self.page_count:
            self.current_page += 1
            print("Flipping the page...wow, you read fast!")

book1 = Book("The River Between", 150)

print(book1.page_count)
book1.turn_page()

        