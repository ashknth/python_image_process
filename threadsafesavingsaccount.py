# threadsafesavingsaccount.py

import threading

class ThreadSafeSavingsAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.lock = threading.RLock()  # Reentrant lock for multiple readers and one writer
        self.readers = 0
        self.condition = threading.Condition(self.lock)

    def get_balance(self):
        """Allow concurrent reads if no writers are active."""
        with self.condition:
            while self.readers < 0:  # Wait if a writer is writing
                self.condition.wait()
            self.readers += 1  # Increment the number of active readers
        balance = self.balance
        with self.condition:
            self.readers -= 1  # Decrement the number of active readers
            if self.readers == 0:
                self.condition.notify_all()  # Notify waiting writers
        return balance

    def deposit(self, amount):
        """Only one writer can modify the balance at a time."""
        with self.condition:
            while self.readers != 0:  # Wait if any readers or writers are active
                self.condition.wait()
            self.readers = -1  # Mark a writer is active
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
            self.readers = 0  # Release the writer lock
            self.condition.notify_all()

    def withdraw(self, amount):
        """Only one writer can modify the balance at a time."""
        with self.condition:
            while self.readers != 0:  # Wait if any readers or writers are active
                self.condition.wait()
            self.readers = -1  # Mark a writer is active
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance: {self.balance}")
                success = True
            else:
                print(f"Failed to withdraw {amount}. Insufficient balance.")
                success = False
            self.readers = 0  # Release the writer lock
            self.condition.notify_all()
        return success
