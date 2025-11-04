#!/usr/bin/env python3


class Coffee:
    def __init__(self, price, size=None):
        self.price = price
        self.size = size

    def get_size(self):
        return self._size

    def set_size(self, value):
        if isinstance(value, str) and value.lower() in [
            "small",
            "medium",
            "large",
        ]:
            self._size = value.capitalize()
        else:
            print("size must be Small, Medium, or Large")

    size = property(get_size, set_size)


if __name__ == "__main__":
    my_coffee = Coffee(
        2.50,
        "medium",
    )
    print(my_coffee.size)
