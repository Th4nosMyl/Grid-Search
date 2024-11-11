import numpy as np
from MBR import *  
from cell import *
from utils import *
import time

# Η κλάση Grid διαχειρίζεται ένα πλέγμα (grid) χωρισμένο σε μικρότερα "cells".
class Grid:
    def __init__(self, xL, yL, xU, yU, m):
        # Αρχικοποίηση του πλέγματος με το ελάχιστο και μέγιστο x, y όριο και το μέγεθος m x m.
        # Δημιουργεί ένα MBR που περιβάλλει το πλέγμα και υπολογίζει τα διαστήματα x και y για τα κελιά.
        self.mbr = MBR(xL, yL, xU, yU)  # Το MBR ορίζει τα όρια του πλέγματος.
        self.m = m                      # m ορίζει πόσα κελιά θα υπάρχουν σε κάθε διάσταση του πλέγματος.
        self.deltax = (self.mbr.xmax - self.mbr.xmin) / m  # Το εύρος κάθε κελιού στον άξονα x.
        self.deltay = (self.mbr.ymax - self.mbr.ymin) / m  # Το εύρος κάθε κελιού στον άξονα y.
        # Δημιουργία πλέγματος m x m από κελιά (αρχικά None, τα κελιά θα οριστούν στην init).
        self.cells = [[None for _ in range(m)] for _ in range(m)]

    def init(self):
        # Αρχικοποιεί τα κελιά με βάση τις συντεταγμένες τους στο πλέγμα.
        # Το κάθε κελί αποθηκεύει τις συντεταγμένες των ορίων του.
        for i in range(self.m):
            for j in range(self.m):
                # Υπολογισμός των ορίων για το κελί [i][j]
                xmin = j * self.deltax
                ymin = i * self.deltay
                xmax = (j + 1) * self.deltax
                ymax = (i + 1) * self.deltay
                # Δημιουργία του κελιού και προσθήκη στο πλέγμα
                self.cells[i][j] = Cell(xmin, ymin, xmax, ymax)

    def findCell(self, x, y):
        # Βρίσκει σε ποιο κελί ανήκει ένα σημείο (x, y).
        # Ελέγχει πρώτα αν το σημείο βρίσκεται εντός των ορίων του πλέγματος.
        if x > self.mbr.xmax or x < self.mbr.xmin:
            return None  # Αν το x είναι εκτός ορίων επιστρέφει None
        if y > self.mbr.ymax or y < self.mbr.ymin:
            return None  # Αν το y είναι εκτός ορίων επιστρέφει None

        # Υπολογισμός των δεικτών (i, j) του κελιού όπου ανήκει το σημείο (x, y)
        i = int(np.floor((y - self.mbr.ymin) / self.deltay))
        j = int(np.floor((x - self.mbr.xmin) / self.deltax))

        # Έλεγχος για περιπτώσεις όπου i ή j είναι ίσο με m και διόρθωση
        if i == self.m:
            i -= 1
        if j == self.m:
            j -= 1
        # Επιστροφή του κελιού στο οποίο ανήκει το σημείο
        return self.cells[i][j]

    def load(self, filename):
        # Φορτώνει σημεία από ένα αρχείο και τα προσθέτει στο κατάλληλο κελί
        try:
            with open(filename, 'r') as br:
                for line in br:
                    arLine = line.strip().split(",")  # Διάσπαση γραμμής σε στοιχεία
                    id = int(arLine[0])               # Αποθηκεύουμε το id του σημείου
                    x = float(arLine[1])              # Συντεταγμένη x
                    y = float(arLine[2])              # Συντεταγμένη y
                    c = self.findCell(x, y)           # Βρίσκουμε το κελί όπου ανήκει το σημείο
                    if c:
                        # Προσθήκη του σημείου ως MBR (ελάχιστο ορθογώνιο που το περικλείει)
                        c.add_object(MBR(x, y, x, y))
        except FileNotFoundError as e:
            print(e)
        except IOError as e:
            print(e)

    def rangeQuery(self, qx, qy, r):
        # Εκτελεί αναζήτηση εύρους, δηλαδή βρίσκει όλα τα σημεία σε απόσταση r από (qx, qy)
        res = []
        # Υπολογισμός των κελιών που είναι εντός του κύκλου ακτίνας r με κέντρο (qx, qy)
        imin = int(np.floor(((qy - r) - self.mbr.ymin) / self.deltay))
        imax = int(np.floor(((qy + r) - self.mbr.ymin) / self.deltay))
        jmin = int(np.floor(((qx - r) - self.mbr.xmin) / self.deltax))
        jmax = int(np.floor(((qx + r) - self.mbr.xmin) / self.deltax))

        # Ελέγχει όλα τα κελιά που είναι εντός της περιοχής
        for i in range(imin, imax + 1):
            for j in range(jmin, jmax + 1):
                candidates = self.cells[i][j].get_objects()  # Λίστα των σημείων του κελιού
                for k in range(len(candidates)):
                    m = candidates[k]
                    # Υπολογισμός της απόστασης του σημείου από το (qx, qy)
                    dis = Utils.distance(qx, qy, m.xmin, m.ymin)
                    # Αν το σημείο είναι εντός απόστασης r, το προσθέτουμε στο αποτέλεσμα
                    if dis <= r:
                        res.append(m)
        return res  # Επιστρέφει τη λίστα των σημείων που πληρούν την απόσταση

if __name__ == "__main__":
    filename = "data.txt"   # Το αρχείο δεδομένων που περιέχει τα σημεία
    g = Grid(0, 0, 1, 1, 10)  # Δημιουργία ενός Grid με όρια [0,1] και 10x10 κελιά
    g.init()                 # Αρχικοποίηση των κελιών του πλέγματος
    g.load(filename)         # Φόρτωση σημείων από το αρχείο και τοποθέτησή τους στα κελιά
    lStart = time.time()     # Καταγραφή αρχικού χρόνου
    res = g.rangeQuery(0.5, 0.5, 0.05)  # Εκτέλεση αναζήτησης για σημεία κοντά στο (0.5, 0.5)
    lEnd = time.time()       # Καταγραφή τελικού χρόνου
    # Εμφάνιση του χρόνου που πήρε η αναζήτηση
    print("Grid range query took ...{} msec".format((lEnd - lStart) * 1000))
    # Εμφάνιση του πλήθους των σημείων που βρέθηκαν και ποιά ήταν αυτά
    print(f"Found {len(res)} points:")
    for mbr in res:
        mbr.print()