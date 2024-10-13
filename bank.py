# bank.py

class Bank:
    def __init__(self):
        self.accounts = {
            "user1": {"pin": "1234", "balance": 1000},
            "user2": {"pin": "5678", "balance": 2000}
        }

    def verify_user(self, username, pin):
        """Check if the username and pin are correct."""
        if username in self.accounts and self.accounts[username]["pin"] == pin:
            return True
        return False

    def get_balance(self, username):
        """Return the account balance for a user."""
        if username in self.accounts:
            return self.accounts[username]["balance"]
        return None

    def withdraw(self, username, amount):
        """Withdraw the specified amount from the user's account."""
        if username in self.accounts:
            if self.accounts[username]["balance"] >= amount:
                self.accounts[username]["balance"] -= amount
                return True
            return False
        return None
