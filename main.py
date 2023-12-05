# random problem selector

import csv
import os
import random

def clear_console():
  os.system('clear')

def start_over():
  clear_console()

  while True:
    # ask user for min max
    min_val = int(input("Enter mininum value: "))
    max_val = int(input("Enter max value: "))

    if min_val > max_val:
      print("\nPlease enter correct min/max value.")
    else:
      break

  max_num_question = max_val - (min_val - 1)
  print(f"\nYou can get up to {max_num_question} questions.")

  while True:
    num_questions = int(input("Enter number of questions you want: "))

    if num_questions > max_num_question:
      print("\nPlease enter correct number of questions.")
      print(f"Maximum number of question is {max_num_question}.")
    else:
      break

  question_list = []
  while len(question_list) < num_questions:
    random_question = random.randint(min_val, max_val)
    if random_question not in question_list:
      question_list.append(random_question)

  print(f"\nHere is your {num_questions} random questions:\n{question_list}\n")

  save_to_csv_file = input("Would you like to save the questions in a csv file? (y/n): ").lower()

  if save_to_csv_file == 'y':
    with open('random_question_list.csv', mode='w', newline='') as file:
      writer = csv.writer(file)
      writer.writerow(['Questions']) 
      for question in question_list:
          writer.writerow([question])  
    print(f"\nYour {num_questions} questions were successfully saved.")

  restart_option = input("Do you want to restart the program? (y/n): ").lower()
  if restart_option == 'y':
    start()
  else:
    print("\nHave a great day 👋")

def continue_():

  clear_console()
  print("👉 Type 'done' when you're done 👈\n")

  wrong_questions_list = []
  csv_questions_list = []

  with open('random_question_list.csv', newline='') as file:
    reader = csv.reader(file)
    next(reader)
    for question in reader:
      csv_questions_list.append(int(question[0]))

  print(f"Here is your list of questions:\n{csv_questions_list}\n")

  while True:
    wrong_question = input("Enter questions you missed one at a time: ")
    if wrong_question.lower() == 'done':
      print(f"\nYour {len(wrong_questions_list)} questions were saved.")
      break
    else:
      if int(wrong_question) in csv_questions_list: 
        wrong_questions_list.append(int(wrong_question))
      else:
        print(f"{wrong_question} is not in the list.\n")

  with open('random_question_list.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Questions'])
    for question in csv_questions_list:
      if question in wrong_questions_list:
        writer.writerow([question])

def start():
  clear_console()
  print("🎲 Random Problem Selector 🎲\n")

  while True:
    select_mode = input("Type 🅰️  to start or 🅱️  to continue: ").upper()
    if select_mode == 'A':
      start_over()
      break 
    elif select_mode == 'B':
      continue_()
      break
    else:
      print("\nPlease Enter correct value.")

start()
