# This is a simple Python script

def greet(name):
    """
    Function to greet a user by their name.
    """
    return f"Hello, {name}! Welcome to Apna Doctor."

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet(user_name))