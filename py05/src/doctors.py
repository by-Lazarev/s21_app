import threading
import time
import random

class Screwdriver:
    def __init__(self):
        self.lock = threading.Lock()

class Doctor(threading.Thread):
    def __init__(self, number, left_screwdriver, right_screwdriver):
        super().__init__()
        self.number = number
        self.left_screwdriver = left_screwdriver
        self.right_screwdriver = right_screwdriver

    def run(self):
        while True:
            # Try to acquire both screwdrivers (locks)
            self.blast()

    def blast(self):
        # Ensure we always acquire the locks in a consistent order
        first, second = (self.left_screwdriver, self.right_screwdriver) if id(self.left_screwdriver) < id(self.right_screwdriver) else (self.right_screwdriver, self.left_screwdriver)
        
        with first.lock:
            with second.lock:
                print(f"Doctor {self.number}: BLAST!")
                time.sleep(random.uniform(0.1, 0.5))  # Simulate the time taken for the action

def main():
    # Initialize screwdrivers
    screwdrivers = [Screwdriver() for _ in range(5)]

    # Initialize doctors
    doctors = [
        Doctor(9, screwdrivers[0], screwdrivers[1]),
        Doctor(10, screwdrivers[1], screwdrivers[2]),
        Doctor(11, screwdrivers[2], screwdrivers[3]),
        Doctor(12, screwdrivers[3], screwdrivers[4]),
        Doctor(13, screwdrivers[4], screwdrivers[0]),
    ]

    # Start all doctor threads
    for doctor in doctors:
        doctor.start()

    # Let the threads run for a while
    time.sleep(5)

    # This would normally be where we signal the threads to stop in a real application,
    # but for this simple example, we'll just exit and let the threads die with the process.

if __name__ == "__main__":
    main()

