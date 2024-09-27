import random
from string import digits, ascii_lowercase, hexdigits
from datetime import datetime


class RandomInputBase:

    def __init__(self):
        self.base = {}

    def input_int(self, start=0, end=10):
        return ''.join([random.choice(digits) for _ in range(random.randint(start, end))])

    def input_str(self, start=8, end=20):
        return ''.join([random.choice(ascii_lowercase) for _ in range(random.randint(start, end))])

    def input_big_str(self, start=8, end=20):
        return ''.join([random.choice(hexdigits) for _ in range(random.randint(start, end))])

    def my_dict(self):
        return self.base


class RandomFirstName(RandomInputBase):
    def __init__(self):
        super().__init__()
        name = self.input_str(start=4, end=9)
        self.base = {
            "valid": name[0].upper() + name[1:],
            "non": '   ',
            "non2": '!!!!!!!!!!!!!!!!!!!!',
            "non3": '4'
        }


class RandomLastName(RandomInputBase):
    def __init__(self):
        super().__init__()
        name = self.input_str(start=6, end=14)
        self.base = {
            "valid": name[0].upper() + name[1:],
        }


class RandomEmail(RandomInputBase):
    def __init__(self):
        super().__init__()
        self.base = {
            "valid": self.valid_email(),
            "non_valid": self.non_valid_email()
        }

    def valid_email(self):
        return f"{self.input_big_str().lower()}@{self.input_str(start=2, end=10)}.com"

    def non_valid_email(self):
        return self.input_big_str()


class RandomMobile(RandomInputBase):

    def __init__(self):
        super().__init__()
        self.base = {
            "int": self.input_int(),
            "valid": self.valid_mobile(),
        }

    def valid_mobile(self):
        return self.input_int(start=10, end=11)


class RandomPicture(RandomInputBase):
    def __init__(self):
        super().__init__()

        self.photo = (
            "/Users/ivanlysikov/PycharmProjects/TestForm/fixtures/photo/27aa7456bc5926373ac26393b6627bd2.jpeg",
            "/Users/ivanlysikov/PycharmProjects/TestForm/fixtures/photo/329fbfff37cb49e16122c16195786e17.jpeg")

        self.base = {
            # "non_valid": f"{self.input_str(end=10)}/{self.valid_file()}",
            "valid": self.valid_file(),
        }

    def valid_file(self):
        return random.choice(self.photo)


class RandomDatetime(RandomInputBase):
    def __init__(self):
        super().__init__()
        self.end_date = datetime.now().date()
        self.base = {
            "non_valid": self.non_date(),
            "valid": self.valid_date(),
        }

    def valid_date(self):
        end = self.end_date
        random_date = list(
            map(str, (random.randint(1, 30), random.randint(0, 11), end.year - random.randint(7, 100))))
        return random_date

    def non_date(self):
        end = self.end_date
        random_date = list(map(str, (31, random.choice((2, 4, 6, 9, 11)), end.year - random.randint(7, 100))))
        return random_date


class RandomSubjects(RandomInputBase):
    def __init__(self):
        super().__init__()
        self.subject = ("Hindi", "English", "Maths", "Physics", "Chemistry", "Biology", "Computer Science",
                        "Commerce", "Accounting", "Economics", "Arts", "Social Studies", "History", "Civics")
        self.base = {
            "valid": self.valid_subject(),
        }

    def valid_subject(self):
        random_subject = [i for i in set([random.choice(self.subject) for _ in range(random.randint(1, 25))]) if
                          type(i) == str and i != ...]

        return random_subject


class RandomHobbies(RandomInputBase):
    def __init__(self):
        super().__init__()
        self.checkbox = ("hobbies-checkbox-1",
                         "hobbies-checkbox-2",
                         "hobbies-checkbox-3")

        self.base = {"valid": self.random_elements()}

    def random_elements(self):
        return tuple(set(random.choice(self.checkbox) for _ in range(random.randint(1, len(self.checkbox) + 1))))


class RandomStatesCity(RandomInputBase):
    def __init__(self):
        super().__init__()
        self.states_city = {"NCR": ["Delhi", "Gurgaon", "Noida"],
                            "Uttar Pradesh": ["Agra", "Lucknow", "Merrut"],
                            "Haryana": ["Karnal", "Panipat"],
                            "Rajasthan": ["Jaipur", "Jaiselmer"]}

        self.valid_ = self.valid_states_city()

        self.base = {
            "valid_states": self.valid_["valid_states"],
            "valid_city": self.valid_["valid_city"],

        }

    def valid_states_city(self, states=None):
        random_states = states if states else random.choice(tuple(self.states_city.keys()))
        random_city = random.choice(self.states_city[random_states])
        return {"valid_states": random_states, "valid_city": random_city}



class RandomCity(RandomStatesCity):

    def my_city(self, states):
        print(states)
        print(self.valid_states_city(states))
        return self.valid_states_city(states)


class RandomGender(RandomHobbies):
    def __init__(self):
        super().__init__()
        self.checkbox = ("gender-radio-1",
                         "gender-radio-2",
                         "gender-radio-3")
        self.base = {"valid": self.random_elements()}

    def random_elements(self):
        return random.choice(self.checkbox)


class RandomCurrentAddress(RandomStatesCity):
    def __init__(self):
        super().__init__()
        self.base = {
            "non_valid": self.input_int(end=40),
            "valid": self.valid_file(),
        }

    def valid_file(self):
        states_city = self.valid_states_city()
        return (f'{str(random.randint(1, 2345))}/{str(random.randint(1, 12))} {self.input_str(end=22)}'
                f'{states_city["valid_city"]} {states_city["valid_states"]}')
