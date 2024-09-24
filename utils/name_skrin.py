import os
from fixtures.random_data import RandomFirstName


class NamePhoto:
    directory = "/Users/ivanlysikov/PycharmProjects/TestForm/fixtures/photo"
    format = "png"
    name_file = os.listdir(directory)
    _name = RandomFirstName()
    first_name = _name.my_dict()

    def new_file(self, element):
        self.new_file = f"{self.directory}{self.first_name['str'] + str(element)}.{self.format}"
        count = 0
        while self.new_file in self.name_file:
            count += 1
            self.new_file = f"/{self.directory}{self.first_name['str'] + str(element)}{str(count)}.{self.format}"
        return self.new_file
