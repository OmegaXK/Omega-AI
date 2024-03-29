"""
A module that uses the "init" function to start the AI.
It can also be run directly to start the AI.
"""

from main import AI

def init():
    """
    Initialize the AI by making an instance of the class and calling the
    init() method.
    """
    ai = AI()
    ai.init()


# Start the AI
init()