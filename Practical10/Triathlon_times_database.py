class Triathlon:
    # Define a Triathlonclass that takes in the following parameters in its __init__ method:
    def __init__(self, first_name, last_name, location, swim_time, cycle_time, run_time):
        self.first_name = first_name  # the first name of the triathlete
        self.last_name = last_name  # the last name of the triathlete
        self.location = location  # the location of the triathlon competition
        self.swim_time = swim_time  # the time (in seconds) it took the triathlete to complete the swim discipline
        self.cycle_time = cycle_time  # the time (in seconds) it took the triathlete to complete the cycle discipline
        self.run_time = run_time  # the time (in seconds) it took the triathlete to complete the run discipline
        self.total_time = swim_time + cycle_time + run_time  # Then calculate the total_time by adding up the times for each discipline.

    # We've also defined a print_details method that prints out all the details of the triathlete's performance in a single line
    def print_details(self):
        print(
            f"{self.first_name} {self.last_name} completed the triathlon in {self.total_time} seconds with the following times for each discipline: swim - {self.swim_time}, cycle - {self.cycle_time}, run - {self.run_time}.")
   # Print out the result

# Example usage
# Create a Triathlon object for a triathlete named John Doe who completed the triathlon in New York with swim, cycle, and run times of 600, 1800, and 1200 seconds respectively.
triathlete = Triathlon("John", "Doe", "New York", 600, 1800, 1200)
# Call the print_details method on this object to print out all the details of John Doe's performance.
triathlete.print_details()