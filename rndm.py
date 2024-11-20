#MIT License

#Copyright (c) 2024 Circunferencias

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import random  # Imports the random module to generate random numbers
import os  # Imports the os module to interact with the operating system files


def rndm(number, file):
    """
    Function that deletes a file if the provided number matches
    a randomly generated number between 1 and 6.
    """
    loser_number = random.randint(1, 6)  # Generates a random number between 1 and 6
    if 1 <= number <= 6:  # Checks if the entered number is between 1 and 6
        if loser_number == number:  # Compares the entered number with the random number
            os.remove(file)  # If they match, deletes the specified file
            return os.path.basename(file) + " has been removed."  # Returns a message indicating the file was deleted
        else:
            return "Your file still exists."  # Returns a message indicating the file was not deleted
    else:
        return "That number is not within the parameters"  # Returns a message if the number is out of range

if __name__ == "__main__":
    # Entry point of the program
    # Prompts the user to input a number between 1 and 6
    number = int(input("Introduce a number between 1 and 6: "))

    # Prompts the user to input a file path, an example Windows path is provided
    file = input(r"Example: C:\\Windows\\alex.txt" + "\nIntroduce a file: ")
    # Calls the rndm function and prints the result
    print(rndm(number, file))
