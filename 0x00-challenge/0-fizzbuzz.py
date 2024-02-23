#!/usr/bin/python3
""" FizzBuzz
"""
import sys


def fizzbuzz(n):
    """
    So basically this is a FizzBuzz function that prints numbers from 1 to n
    separated by a space.

    - For multiples of three print "Fizz" instead of the number and for
      multiples of five print "Buzz".
    - For numbers which are multiples of both three and five print "FizzBuzz".
    """
    if n < 1:
        return

    ephem_output = []
    for x in range(1, n + 1):
        if (x % 3) == 0 and (x % 5) == 0:
            ephem_output.append("FizzBuzz")
        elif (x % 3) == 0:
            ephem_output.append("Fizz")
        elif (x % 5) == 0:
            ephem_output.append("Buzz")
        else:
            ephem_output.append(str(x))
    print(" ".join(ephem_output))


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Missing number")
        print("Usage: ./0-fizzbuzz.py <number>")
        print("Example: ./0-fizzbuzz.py 89")
        sys.exit(1)

    number = int(sys.argv[1])
    fizzbuzz(number)
