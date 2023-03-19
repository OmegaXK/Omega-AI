"""A module that uses functions to model the interface of an AI."""

import json
from pathlib import Path
from time import sleep as wait
from main import User, AI

def ai_interface():
    """The main interface for using the AI."""

    # Read the user's info from the path.
    path = Path('user.json')
    contents = path.read_text()
    user_info = json.loads(contents)

    # Set up the user with the correct info.
    user = User(user_info['first_name'], user_info['last_name'], 
                user_info['username'], user_info['email'], 
                user_info['password'])
    # Create an AI class to use later.
    ai = AI()

    while True:
        print("\nWhat would you like to do?")
        print('[1] Ask questions')
        print('[2] Enter information about yourself')
        print('[3] Recall user information')
        print('[4] Describe user')
        print('[5] Extra help')
        print('[q] Quit')
        
        # Loop until action is one of the options.
        action = ''
        while True:
            action = input('[?]: ')
            if action != '1' and action != '2' and action != '3' \
            and action != '4' and action != '5' and action != 'q':
                print('\nPlease enter 1, 2, 3, 4, 5 or q.\n')
            else:
                break 
        
        # If action is 1, it means the user wants to ask questions.
        if action == '1':
            ask_questions(user, ai)

        # If the action is 2, then the user wants to enter info.
        elif action == '2':
            enter_info(user, ai)

        # If action is 3, the user wants the ai to recall info.
        elif action == '3':
            recall_info()

        # If action is 4, the user wants to be described.
        elif action == '4':
            print('\n')
            user.describe_user()
            input('\nPress enter to move on: ')

        elif action == '5':
            print("\nI will give you the link to AI's page.")
            print("You can view the README file for additional help.")
            print("Control-click the link to go to it. (command-click for Mac)")
            print("\nhttps://github.com/OmegaXK/Omega-AI\n")

        elif action == 'q':
            # Return back to the login page.
            return
        

def ask_questions(user, ai):
    """Prompt the user to ask yes or no questions at the >>>."""

    print('\nPlease type your questions at the ">>>" prompt.')
    print('Make sure to ask yes or no questions.')
    print("Type 'q' to quit.")

    # Loop until the user enters 'q'.
    while True:
        question = input('\n>>> ')
        if question == 'q':
            break 
        else:
            # Get the AI's answer using the user and ai classes.
            user.get_answer(ai)


def enter_info(user, ai):
    """Let the user enter info about them."""

    print("\nFirst, enter the type of information you are giving.")
    print('Then, type the actual info.')
    print('Example - Info type: favorite color - Actual info: blue.')
    print("Enter 'q' to quit.")

    while True:
        info_type = input('\nInfo type: ')
        if info_type == 'q':
            break 
    
        info = input('Actual info: ')
        if info == 'q':
            break
                
        # Use the user class to feed the ai info.
        user.feed_info(info_type, info, ai)

        # Put the new info in the JSON file.
        user_interests_path = Path('user_interests.json')
        user_interests = json.dumps(ai.return_user_info())
        user_interests_path.write_text(user_interests)


def recall_info():
    """Recall the info the user has put in, if they have."""
    
    # Get the path and read the data in it.
    user_interests_path = Path('user_interests.json')
    if user_interests_path.exists():
        user_interests_contents = user_interests_path.read_text()
        user_interests = json.loads(user_interests_contents)
    else:
        print("\nYou haven't entered any info yet.")
        return
            
    # Loop over every key-value pair in the dictionary.
    for type_of_info, actual_info in user_interests.items():
        # Print the info type and info, then wait 0.7 seconds.
        print(f"\n{type_of_info}: {actual_info}")
        wait(0.7)