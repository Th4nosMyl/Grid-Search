import time  # Import the time module for measuring execution time
from MBR import *  # Import everything from the MBR module
from cell import *  # Import everything from the cell module
from utils import *  # Import everything from the utils module

class LinearScan:
    def __init__(self, filename):
        # Initialize the LinearScan class with the given filename
        self.filename = filename

    def range_query(self, qx, qy, r):
        # Perform a range query with center (qx, qy) and radius r
        results = []  # Initialize an empty list to store results
        try:
            with open(self.filename, 'r') as file:
                # Open the file in read mode
                for line in file:
                    # Iterate over each line in the file
                    ar_line = line.strip().split(',')
                    # Split the line by commas and strip whitespace
                    id = int(ar_line[0])
                    # Convert the first element to an integer (id)
                    x = float(ar_line[1])
                    # Convert the second element to a float (x-coordinate)
                    y = float(ar_line[2])
                    # Convert the third element to a float (y-coordinate)

                    # Check the distance using the distance function from the Utils class
                    if Utils.distance(qx, qy, x, y) <= r:
                        # If the distance is within the radius, add the MBR to results
                        results.append(MBR(x, y, x, y))
        except FileNotFoundError:
            # Handle the case where the file is not found
            print(f"File {self.filename} not found.")
        except IOError as e:
            # Handle other I/O errors
            print(f"An error occurred: {e}")
        return results  # Return the list of results

# Entry point of the program
if __name__ == "__main__":
    filename = "data.txt"  # Define the filename
    ls = LinearScan(filename)  # Create an instance of LinearScan with the filename
    qx, qy, r = 0.5, 0.5, 0.05  # Define the query center and radius

    # Measure the execution time
    start_time = time.time()  # Record the start time
    results = ls.range_query(qx, qy, r)  # Perform the range query
    end_time = time.time()  # Record the end time

    print(f"Linear scan took... {int((end_time - start_time) * 1000)} msec")
    # Print the execution time in milliseconds
    
    # Optionally, print the results
    # for mbr in results:
    #    mbr.print()
