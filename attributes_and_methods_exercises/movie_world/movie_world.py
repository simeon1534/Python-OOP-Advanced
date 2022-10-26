from movie_world.customer import Customer
from movie_world.dvd import DVD


class MovieWorld:

    def __init__(self, name):
        self.name = name
        self.customers = []  # LIST WITH CUSTOMER INSTANCES
        self.dvds = []  # LIST WITH DVD INSTANCES

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        the_customer = ''
        for customer_obj in self.customers:
            if customer_obj.id == customer_id:
                the_customer = customer_obj
                break

        the_dvd = ''
        for dvd_obj in self.dvds:
            if dvd_obj.id == dvd_id:
                the_dvd = dvd_obj
                break

        if the_dvd in the_customer.rented_dvds and the_dvd.is_rented:
            return f"{the_customer.name} has already rented {the_dvd.name}"

        elif the_dvd not in the_customer.rented_dvds and the_dvd.is_rented:
            return f"DVD is already rented"

        if the_customer.age < the_dvd.age_restriction:
            return f"{the_customer.name} should be at least {the_dvd.age_restriction} to rent this movie"
        else:
            the_dvd.is_rented = True
            the_customer.rented_dvds.append(the_dvd)
            return f"{the_customer.name} has successfully rented {the_dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        the_customer = ''
        for customer_obj in self.customers:
            if customer_obj.id == customer_id:
                the_customer = customer_obj
                break

        the_dvd = ''
        for dvd_obj in self.dvds:
            if dvd_obj.id == dvd_id:
                the_dvd = dvd_obj
                break

        if the_dvd in the_customer.rented_dvds:
            the_dvd.is_rented = False
            the_customer.rented_dvds.remove(the_dvd)
            return f"{the_customer.name} has successfully returned {the_dvd.name}"
        else:
            return f"{the_customer.name} does not have that DVD"

    def __repr__(self):
        res = []
        for customer in self.customers:
            res.append(customer.__repr__())

        for dvd in self.dvds:
            res.append(dvd.__repr__())

        return '\n'.join(res)

