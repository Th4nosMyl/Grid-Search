import time
from MBR import *  
from cell import *
from utils import *

class LinearScan:
    def __init__(self, filename):
        self.filename = filename

    def range_query(self, qx, qy, r):
        results = []
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    ar_line = line.strip().split(',')
                    id = int(ar_line[0])
                    x = float(ar_line[1])
                    y = float(ar_line[2])

                    # Έλεγχος απόστασης μέσω της συνάρτησης από την κλάση Utils
                    if Utils.distance(qx, qy, x, y) <= r:
                        results.append(MBR(x, y, x, y))
        except FileNotFoundError:
            print(f"File {self.filename} not found.")
        except IOError as e:
            print(f"An error occurred: {e}")
        return results

# Είσοδος στο πρόγραμμα
if __name__ == "__main__":
    filename = "data.txt"
    ls = LinearScan(filename)
    qx, qy, r = 0.5, 0.5, 0.05

    # Υπολογισμός χρόνου εκτέλεσης
    start_time = time.time()
    results = ls.range_query(qx, qy, r)
    end_time = time.time()

    print(f"Linear scan took... {int((end_time - start_time) * 1000)} msec")
    
    # Προαιρετικά, εκτύπωση των αποτελεσμάτων
    #for mbr in results:
    #   mbr.print()
