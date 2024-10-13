import threading
import time

class Counter:
    def __init__(self):
        self.count = 0
        self.condition = threading.Condition()

    def increment(self):
        with self.condition:
            for i in range(1, 6):
                self.count += 1
                print(f"Counter: {self.count}")
                time.sleep(1)
            # Notify that counting is done
            self.condition.notify_all()

    def wait_for_counting(self):
        with self.condition:
            print("Waiting for counting to finish...")
            self.condition.wait()  # Wait for the notification that counting is done
            print("Counting is finished. Proceeding...")

def main():
    counter = Counter()

    # Create threads for counting and waiting
    counting_thread = threading.Thread(target=counter.increment)
    waiting_thread = threading.Thread(target=counter.wait_for_counting)

    # Start the counting thread first
    counting_thread.start()
    # Start the waiting thread after
    waiting_thread.start()

    # Wait for both threads to finish
    counting_thread.join()
    waiting_thread.join()

if __name__ == "__main__":
    main()
