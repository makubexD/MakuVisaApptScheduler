from auth import login
from scheduler.scheduler import schedule

if __name__ == "__main__":
    print("Starting...")
    login()
    schedule()
    print("End block...")