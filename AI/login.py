import json
from os import remove
from pathlib import Path 
from ai_interface import ai_interface

def log_in(path):
    """Let the user log in to the AI."""
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print("\nSorry, you don't have an account.")
        return False
    else:
        # Load in the contents of the file.
        user_info = json.loads(contents)

        for i in range(3):
            # Give the user three chances to enter the correct info.
            username = input('\nPlease enter your username: ')
            password = input('Please enter your password: ')
            if username == user_info['username'] and \
            password == user_info['password']:
                # If info is correct, set correct to true and break.
                correct = True
                break
            else:
                # If the info is not correct, set correct to false.
                print('\nIncorrect username or password.')
                correct = False

        if not correct:
            # The user has failed three times.
            print('After three failed attampts, we have to kick you.')
            return False
        else:
            print('You can now start using the AI.')
            return True
        

def delete_account():
    """Delete all of the files storing the user's info."""
    # Loop over the two files storing info.
    for file in ['user.json', 'user_interests.json']:
        # Create the path object, and if it exists, delete it.
        path = Path(file)
        if path.exists():
            remove(file)
        

def sign_up(path):
        """Let the user sign up to make an account."""
        # Start by overriding the old data.
        delete_account()

        username = input('\nPlease enter your username: ')
        first_name = input('Please enter your first name: ')
        last_name = input('Please enter your last name: ')
        email = input('Please enter your email: ')
        password = input('Please enter a password: ')

        # Set up a dictionary with the user's info to write to the file.
        user_info = {
            'first_name': first_name,
            'last_name': last_name,
            'username': username,
            'email': email,
            'password': password
            }
        
        contents = json.dumps(user_info)
        path.write_text(contents)


# Main loop.
while True:
    print('\nWould you like to sign up, login, delete your account, or quit?')
    print('[1] Sign up')
    print('[2] Login')
    print('[3] Delete Acount')
    print('[q] Quit')

    sign_or_log = ''
    while True:
        sign_or_log = input('[?]: ')
        if sign_or_log != '1' and sign_or_log != '2' and sign_or_log != '3' \
        and sign_or_log != 'q':
            # The user didn't enter 1, 2, or 3.
            print('\nPlease enter 1, 2, 3, or q.')
        else:
            # The user entered a correct response.
            break

    # Once out of the loop, sign_or_log has to be 1, 2, or 3.

    path = Path('user.json')

    if sign_or_log == '1':
        # The user wants to sign up for an account.
        sign_up(path)

    elif sign_or_log == '2':
        # The user wants to log in to their account.
        if log_in(path):
            ai_interface()
    
    # If sign_or_log is 3, the user wants their account to be deleted.
    elif sign_or_log == '3':
        delete_account()
                    
    elif sign_or_log == 'q':
        break

# Exit out of the terminal after the user quits.
exit()
