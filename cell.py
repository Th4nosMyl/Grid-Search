from MBR import MBR  # Import the MBR class from the MBR module

class Cell:  # Define the Cell class
    def __init__(self, xL, yL, xU, yU):  # Initialize the Cell object with lower and upper bounds
        self.mbr = MBR(xL, yL, xU, yU)  # Create an MBR object with the given bounds and assign it to self.mbr
        self.objects = []  # Initialize an empty list to store objects within the cell

    def add_object(self, m):  # Define a method to add an object to the cell
        self.objects.append(m)  # Append the object to the objects list

    def get_objects(self):  # Define a method to retrieve all objects in the cell
        return self.objects  # Return the list of objects

    def get_mbr(self):  # Define a method to retrieve the MBR of the cell
        return self.mbr  # Return the MBR object
