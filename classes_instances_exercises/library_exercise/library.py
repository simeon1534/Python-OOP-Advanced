

class Library:
    def __init__(self):
        self.user_records = []  # store user objects
        self.books_available = {}  # key:str value:list of strings
        self.rented_books = {}  # {username: {book name: days left}}

    def add_user(self, user: 'User'):
        if user not in self.user_records:
            self.user_records.append(user)
        else:
            return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user: 'User'):
        if user not in self.user_records:
            return f"We could not find such user to remove!"
        else:
            self.user_records.remove(user)

    def change_username(self, user_id: int, new_username: str):
        for user_obj in self.user_records:
            if user_obj.user_id == user_id:
                if user_obj.username == new_username:
                    return f"Please check again the provided username - it should be different than the username used " \
                           f"so far! "
                else:
                    self.user_records.remove(user_obj)
                    user_obj.username=new_username
                    self.user_records.append(user_obj)
                    return  f"Username successfully changed to: {new_username} for userid: {user_obj.user_id}"


                    # rented_books?

        return f"There is no user with id = {user_id}!"

