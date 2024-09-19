import sys
import time
from datetime import datetime, timedelta
from playsound import playsound


class Timer:
    """
    Timer class to track a countdown based on user input in HH:MM:SS format.
    """

    def __init__(self, duration):
        """
        Initializes the Timer with a specific duration.
        The duration is provided in seconds.
        """
        self.duration = duration
        self.start_time = None

    def start(self):
        """
        Starts the timer and records the start time.
        """
        self.start_time = time.time()
        print(f"Timer started for {str(timedelta(seconds=self.duration))} (HH:MM:SS)")

    def stop(self):
        """
        Stops the timer and checks if the timer is up.
        If the time is up, it plays an alarm sound.
        """
        elapsed_time = 0
        while elapsed_time < self.duration:
            time.sleep(1)   # Wait 1 second between checks
            elapsed_time = time.time() - self.start_time
            remaining_time = self.duration - elapsed_time
            sys.stdout.write(f"\rTime left: {str(timedelta(seconds=int(remaining_time)))}")  # Updated countdown output
            sys.stdout.flush()

        print("\nTime is up! Playing alarm...")
        self.play_alarm()

    def play_alarm(self):
        """
        Plays an alarm sound when the timer is up.
        Uses the 'playsound' library to play alarm.mp3.
        """
        playsound('alarm.mp3')


def get_time_from_user():
    """
    Prompts the user to input time in HH:MM:SS format and converts it to seconds.

    Returns:
        int: Total duration in seconds.
    """
    while True:
        user_input = input("Enter the timer duration in HH:MM:SS format: ")
        try:
            time_obj = datetime.strptime(user_input, "%H:%M:%S")
            total_seconds = timedelta(hours=time_obj.hour, minutes=time_obj.minute,
                                      seconds=time_obj.second).total_seconds()
            return int(total_seconds)
        except ValueError:
            print("Invalid format! Please enter time in HH:MM:SS format.")


if __name__ == "__main__":
    # Get duration from the user
    duration_in_seconds = get_time_from_user()

    # Initialize and start the timer
    timer = Timer(duration_in_seconds)
    timer.start()

    # Stop the timer and play alarm when time is up
    timer.stop()
