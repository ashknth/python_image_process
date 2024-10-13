# bank.py

from threadsafesavingsaccount import ThreadSafeSavingsAccount

class Bank:
    def __init__(self):
        # Each user has a ThreadSafeSavingsAccount object for thread-safe access.
        self.accounts = {
            "user1": {"pin": "1234", "account": ThreadSafeSavingsAccount(balance=1000)},
            "user2": {"pin": "5678", "account": ThreadSafeSavingsAccount(balance=2000)}
        }

    def verify_user(self, username, pin):
        """Check if the username and pin are correct."""
        if username in self.accounts and self.accounts[username]["pin"] == pin:
            return True
        return False

    def get_balance(self, username):
        """Return the account balance for a user using a thread-safe account."""
        if username in self.accounts:
            return self.accounts[username]["account"].get_balance()
        return None

    def deposit(self, username, amount):
        """Deposit the specified amount to the user's account in a thread-safe way."""
        if username in self.accounts:
            self.accounts[username]["account"].deposit(amount)

    def withdraw(self, username, amount):
        """Withdraw the specified amount from the user's account in a thread-safe way."""
        if username in self.accounts:
            return self.accounts[username]["account"].withdraw(amount)
        return False
