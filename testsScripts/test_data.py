from faker import Faker

class TestData:
    """
    Test Data generator
    """
    def __init__(self):
        fake = Faker(locale='pl')
        self.searched_phrase_existing = "lawenda nasiona"
        self.searched_phrase_nonexistent = "afghsdfyuf"
        self.market_location = "Katowice"
        self.email = fake.email()
        self.first_name = fake.first_name()
        self.last_name = fake.last_name()
        self.postal_code = fake.postcode()
        self.city = fake.city()
        self.street = fake.street_name()
        self.building_number = fake.building_number()
        self.phone_number = fake.phone_number()