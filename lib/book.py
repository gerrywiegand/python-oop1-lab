#!/usr/bin/env python3


class Book:
    ## Book class with title and page_count attributes
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    # Getter and setter for page_count with validation
    def get_page_count(self):
        return self._page_count

    def set_page_count(self, value):
        if isinstance(value, int) and value >= 0:
            self._page_count = value
        else:
            print("page_count must be an integer")

    # Define page_count as a property
    page_count = property(get_page_count, set_page_count)

    # Method to simulate turning a page
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")


if __name__ == "__main__":
    Meditations = Book("Meditations", 254)
    print(Meditations.title)
    print(Meditations.page_count)
