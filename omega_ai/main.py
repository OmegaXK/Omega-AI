"""The main classes and functions to model a simple AI using Python."""

import random

class AI:
    """The main class to model a simple AI."""

    def __init__(self):
        """Initialize the attributes of the AI."""
        self.user_info = {} 

    def recieve_info(self, info, info_name):
        """Recieve the info provided and add it to the dictionary."""
        self.user_info[info_name] = info

    def recieve_question(self):
        """Return a random answer with random punctuation."""
        if random.randint(1, 2) == 2:
            punctuation = '.'
        else:
            punctuation = '!'

        random_number = random.randint(1, 3)
        if random_number == 1:
            answer = 'No'
        elif random_number == 2:
            answer = 'Yes'
        else:
            answer = "I'm not sure"

        return f"{answer}{punctuation}"
    
    def return_user_info(self):
        """Return the user's info so it can be worked with."""
        return self.user_info
    
    def init(self):
        """Starts up the AI easily by importing login.py's code."""
        import static_files.ai.seperated_files.login as login


class User:
    """The main class to model a user using the AI."""

    def __init__(self, first_name, last_name, username, email, password):
        """Initialize the attributes of the user."""
        self.first_name = first_name 
        self.last_name = last_name 
        self.username = username 
        self.email = email
        self.password = password

    def describe_user(self):
        """Print the user's info."""
        print(f"Full name: {self.first_name.title()} {self.last_name.title()}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Password: {self.password}") 

    def feed_info(self, info_name, info, ai):
        """Feed info to the AI."""
        ai.recieve_info(info, info_name)

    def get_answer(self, ai):
        """Get the answer from the AI and display it."""
        answer = ai.recieve_question()
        print(answer)