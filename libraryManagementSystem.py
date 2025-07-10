class LibraryItem:
     #constructor
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.available=True
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def check_out(self):
        if self.available:
            print(f"Checked out: {self}")
            self.available=False
        else:
            print(f"{self} is not available for checkout!")
    def check_in(self):
        print(f"Checked in : {self}")
        self.available=True






#child class of libray item
class Book(LibraryItem):





class User: