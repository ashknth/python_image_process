import threading
import time
import random

class Counter:
    """A counter object that can be incremented and read by threads."""
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def increment(self):
        """Increment the counter value with lock protection."""
        with self.lock:
            print(f"Writer is done incrementing to {self.value + 1}")
            self.value += 1

    def get_value(self):
        """Get the current value of the counter."""
        with self.lock:
            value = self.value
        return value

class Reader(threading.Thread):
    """Reader thread that reads the value of the counter."""
    def __init__(self, counter, reader_id):
        threading.Thread.__init__(self)
        self.counter = counter
        self.reader_id = reader_id

    def run(self):
        print(f"Reader{self.reader_id} starting up")
        time.sleep(random.uniform(0.1, 0.5))  # Simulate reading delay
        value = self.counter.get_value()
        print(f"Reader{self.reader_id} is done getting {value}")

class Writer(threading.Thread):
    """Writer thread that increments the value of the counter."""
    def __init__(self, counter, writer_id):
        threading.Thread.__init__(self)
        self.counter = counter
        self.writer_id = writer_id

    def run(self):
        print(f"Writer{self.writer_id} starting up")
        time.sleep(random.uniform(0.1, 0.5))  # Simulate writing delay
        self.counter.increment()

def main():
    counter = Counter()

    # Create reader threads
    print("Creating reader threads.")
    readers = [Reader(counter, i) for i in range(1, 5)]

    # Create writer threads
    print("Creating writer threads.")
    writers = [Writer(counter, i) for i in range(1, 3)]

    # Start all threads
    print("Starting the threads.")
    for r in readers:
        r.start()
    for w in writers:
        w.start()

    # Join all threads
    for r in readers:
        r.join()
    for w in writers:
        w.join()

    print("All threads have finished.")

if __name__ == "__main__":
    main()
