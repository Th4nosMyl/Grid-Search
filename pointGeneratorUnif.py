import random  # Import the random module to generate random numbers

class PointGeneratorUnif:
    def __init__(self, filename):
        self.filename = filename  # Initialize the class with the filename where points will be saved

    # Method to generate a file with n random points
    def generate(self, n):
        try:
            with open(self.filename, 'w') as file:  # Open the file in write mode
                for i in range(1, n + 1):  # Loop from 1 to n (inclusive)
                    x = random.random()  # Generate a random x value between 0 and 1
                    y = random.random()  # Generate a random y value between 0 and 1
                    file.write(f"{i},{x},{y}\n")  # Write the point index and coordinates to the file
        except IOError as e:  # Handle any I/O errors that occur
            print(f"An error occurred: {e}")  # Print an error message if an exception is raised

# Entry point of the program
if __name__ == "__main__":
    filename = "data.txt"  # Define the filename where points will be saved
    generator = PointGeneratorUnif(filename)  # Create an instance of PointGeneratorUnif with the specified filename
    generator.generate(100000)  # Generate 100000 random points and save them to the file
