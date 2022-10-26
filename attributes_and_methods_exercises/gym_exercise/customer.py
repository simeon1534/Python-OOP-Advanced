class Customer:
    customer_id = 0

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        Customer.customer_id += 1
        self.customer_instance_id = Customer.customer_id

    def __repr__(self):
        return f"Customer <{Customer.customer_id}> {self.name}; Address: {self.address}; Email: {self.email}"

    @staticmethod
    def get_next_id():
        return Customer.customer_id + 1


