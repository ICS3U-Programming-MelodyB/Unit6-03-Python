#!/usr/bin/env python3

# Created by: Melody Berhane
# Created on: Jan. 29, 2022
# This program uses a for loop to generate and
# print random numbers in a list, then
# displays the smallest value

import constants
import random


# function calculates the max value in the list of elements
def find_min_value(random_nums):

    min = random_nums[0]

    # calculate the min value
    for counter in range(len(random_nums)):
        if min > random_nums[counter]:
            min = random_nums[counter]

    return min


def main():
    # initializing counter
    counter = 0

    # declaring variable
    random_nums_user = []

    # display opening message to console
    print("This program generates a list of random "
          "numbers between 0 and 100, then determines the smallest number.")
    print("")

    # displays random numbers and calculates average
    for counter in range(constants.MAX_ARRAY_SIZE):
        random_nums_user.append(random.randint(constants.MIN_NUM,
                                               constants.MAX_NUM))
        print("{} added to the list at "
              "position {}" .format(random_nums_user[counter], counter))

    min_user = find_min_value(random_nums_user)
    print("")
    print("The max value is: {}" .format(min_user))


if __name__ == "__main__":
    main()
