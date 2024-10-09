"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE

class Account:
    """Creating an Account class with methods"""
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest

    # This method sets the balance of the account.
    def set_balance(self, balance):
        """Sets the balance for the for the account"""
        self.balance = balance

    # The method sets the interest gained for the account.
    def set_interest(self, interest):
        """Sets the interest gained for the the account"""
        self.interest = interest

balance = 1000
interest_rate = 5 
months = 12


# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest emontharned.
        And returns the interest earned.
    """


    # Create an instance of the `Account` class and pass in the balance and interest parameters.

    savings_account = Account(balance, 1000)


    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE

    # Calculate interest earned
     # ADD YOUR CODE HERE

    interest_earned = balance * (interest_rate / 100) * (months / 12)

    # Update the savings account balance by adding the interest earned
    # ADD YOUR CODE HERE

    updated_balance = balance + interest_earned    

    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE

    savings_account.set_balance(updated_balance)

    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    # ADD YOUR CODE HERE

    savings_account.set_interest(interest_earned)

