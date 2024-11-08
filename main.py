# Programmers:  Donovan, Cameron
# Course:  CS151,
# Due Date: november 14th
# Lab Assignment:  lab09
# Problem Statement:  You are organizing a dinner party with assigned seats. Create a program to read in all the attendees and then output the seat assignments.
# Data In: file name
# Data Out:  table #, seat # and name from list
# Credits:
# Input Files: [description of the format of the input files you need for this program to work]

import os

# Purpose:  reading file
  # Parameters: none
  # Return: file
def read_file_name():
    name = input("Which txt file would you like to read? ")

    # Check if the file exists, and if not, ask again until a valid file is entered
    while not os.path.isfile(name):
        print('We currently do not have a file by that name. Try again.')
        name = input("Which txt file would you like to read? ")

    # Return the valid filename
    return name


# Purpose:  reading file to list
  # Parameters: file name
  # Return: data
def file_to_list(file_name):
    # Open the file
    file_data = open(file_name, 'r')

    # Read all lines from the file and store them as a list of strings
    data = file_data.readlines()

    # Close the file
    file_data.close()

    # Return the list of lines from the file
    return data


# Purpose: create the group
  # Parameters: lists
  # Return: formated groups
def table_groups(list_data):
    print('~'* 30)
    table = 1
    seat = 1
    for i in range(0, len(list_data) - 1):
        print(f'Table {table}, Seat {seat}  {list_data[i]}')
        seat += 1
        if seat > 6:
            table += 1
            seat = 1
    print('~' * 30)


# Purpose:  calling other functions
  # Parameters: none
  # Return: none
def main():
    print('\n'
          'This python program is designed to take names from a txt file and use them to create a seating chart.')
    file_name = read_file_name()
    list_data = ((file_to_list(file_name)))
    table_groups(list_data)
    print('Thank you for using our program.')


main()
