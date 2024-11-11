import random

class PointGeneratorUnif:
    def __init__(self, filename):
        self.filename = filename

    # Δημιουργία αρχείου με n τυχαία σημεία
    def generate(self, n):
        try:
            with open(self.filename, 'w') as file:
                for i in range(1, n + 1):
                    x = random.random()  # Τυχαία τιμή x μεταξύ 0 και 1
                    y = random.random()  # Τυχαία τιμή y μεταξύ 0 και 1
                    file.write(f"{i},{x},{y}\n")
        except IOError as e:
            print(f"An error occurred: {e}")

# Είσοδος στο πρόγραμμα
if __name__ == "__main__":
    filename = "data.txt"
    generator = PointGeneratorUnif(filename)
    generator.generate(100000)
