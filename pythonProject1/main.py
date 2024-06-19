# this is the first answer
# Prompt the user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculate the sum
sumNum = num1 + num2

# Print the sum in a user-friendly format
print(f"The sum of {num1} and {num2} is {sumNum}.")


# this is the second answer
# Get the number as input
num3 = int(input("Enter a number: "))

# Check if the number is even using the modulo operator
if num3 % 2 == 0:
  print(f"{num3} is even.")
else:
  print(f"{num3} is odd.")

# this is third answer
def factorial(n):
  """Calculates the factorial of a non-negative integer n.

  Args:
      n: The non-negative integer for which to calculate the factorial.

  Returns:
      The factorial of n, or an error message if n is negative.
  """

  if n < 0:
    return "Factorial is not defined for negative numbers."
  elif n == 0:
    return 1
  else:
    return n * factorial(n - 1)

# Get the number as input
num4 = int(input("Enter a non-negative number: "))

# Calculate the factorial
factorial_result = factorial(num4)

# Print the result
print(f"The factorial of {num4} is {factorial_result}.")


# this is fourth answer
# Prompt the user for their name
name1 = input("What is your name? ")

# Create a greeting message
greeting = f"Hello, {name1}!"

# Print the greeting message
print(greeting)


# this is the fifth answer
# Prompt the user for input
user_string = input("Enter the string you want to write to the file: ")

# Specify the filename (replace 'my_file.txt' with your desired name)
filename1 = 'my_file.txt'

# Open the file in write mode ('w') with a context manager
with open(filename1, 'w') as file:
  # Write the user's string to the file
  file.write(user_string)

print(f"String successfully written to '{filename1}'.")

# this is the sixth answer
def read_file(filename1):

  try:
    # Open the file in read mode ('r') with a context manager
    with open(filename1, 'r') as file:
      # Read the entire content of the file
      file_contents = file.read()
      # Print the contents to the console
      print(file_contents)
  except FileNotFoundError:
    print(f"Error: File '{filename1}' not found.")

filename2 = input("Enter the name of the text file: ")

# Read the file contents
read_file(filename2)

# this is the seventh answer
def string_length(text1):
  """Calculates the length of a given string.

  Args:
      text: The string for which to calculate the length.

  Returns:
      The length of the input string.
  """

  return len(text1)

# Example usage
user_string = input("Enter a string: ")
string_len = string_length(user_string)
print(f"The length of the string '{user_string}' is {string_len}.")


# this is the eighth answer
def concatenate_strings(str1, str2):
  """Concatenates two strings and returns the combined string.

  Args:
      str1: The first string.
      str2: The second string.

  Returns:
      The combined string formed by concatenating str1 and str2.
  """

  return str1 + str2

# Example usage
string1 = "Hello, "
string2 = "world!"
concatenated_string = concatenate_strings(string1, string2)
print(f"The concatenated string is: '{concatenated_string}'")


# this is the ninth answer
def substring_check(full_string, substring):
  """Checks if a substring is present in a given string using the 'in' operator.

  Args:
      full_string: The full string to search within.
      substring: The substring to search for.

  Returns:
      True if the substring is found in the full string, False otherwise.
  """

  return substring in full_string

# Example usage
string1 = "This is a test string."
substring = "test"

if substring_check(string1, substring):
  print(f"The substring '{substring}' is present in '{string1}'.")
else:
  print(f"The substring '{substring}' is not present in '{string1}'.")


# this is the tenth answer
def substring_check(full_string, substring):
  """Checks if a substring is present in a given string using the 'in' operator.

  Args:
      full_string: The full string to search within.
      substring: The substring to search for.

  Returns:
      True if the substring is found in the full string, False otherwise.
  """

  return substring in full_string

# Example usage
string1 = "This is a test string."
substring = "test"

if substring_check(string1, substring):
  print(f"The substring '{substring}' is present in '{string1}'.")
else:
  print(f"The substring '{substring}' is not present in '{string1}'.")


# this is the eleventh answer
def fibonacci(n):
  """Generates the first n numbers in the Fibonacci sequence (iterative).

  Args:
      n: The number of terms to generate in the Fibonacci sequence.

  Returns:
      A list containing the first n numbers in the Fibonacci sequence.
  """

  if n <= 1:
    return [n]

  fib_sequence = [0, 1]
  for i in range(2, n):
    next_term = fib_sequence[i-1] + fib_sequence[i-2]
    fib_sequence.append(next_term)
  return fib_sequence

# Get the number of terms from the user
num_terms = int(input("Enter the number of terms in the Fibonacci sequence: "))

# Generate the Fibonacci sequence
fibonacci_sequence = fibonacci(num_terms)

# Print the sequence
print(f"The first {num_terms} numbers in the Fibonacci sequence are: {fibonacci_sequence}")

# this is the twelfth answer
def sum_of_digits(number1):
  """Calculates the sum of the digits in a non-negative integer.

  Args:
      number: The non-negative integer for which to calculate the sum of digits.

  Returns:
      The sum of the digits in the number.
  """

  if number1 < 0:
    return "Sum of digits is not defined for negative numbers."
  else:
    sum_of_digits = 0
    while number1 > 0:
      # Extract the last digit using the modulo operator (%)
      digit = number1 % 10
      # Add the digit to the sum
      sum_of_digits += digit
      # Remove the last digit by integer division (//)
      number1 //= 10
    return sum_of_digits

# Get the number as input
number1 = int(input("Enter a non-negative number: "))

# Calculate the sum of digits
sum_of_digits_result = sum_of_digits(number1)

# Print the result
print(f"The sum of digits in {number1} is {sum_of_digits_result}.")

# this is the thirteenth answer
import datetime

def calculate_age(birth_year):
  """Calculates the age based on the given birth year and current date.

  Args:
      birth_year: The birth year of the user.

  Returns:
      The age of the user.
  """

  today = datetime.date.today()
  age = today.year - birth_year
  return age

# Get the birth year from the user
birth_year = int(input("Enter your birth year: "))

# Calculate the age
age = calculate_age(birth_year)

# Print the result in a user-friendly format
print(f"You are {age} years old.")


#this is the fourteenth answer
lines = []
while True:
  # Prompt the user for input
  line = input("Enter a line (or leave blank to finish): ")

  # Break the loop if an empty line is entered
  if not line:
    break

  # Append the line to the list
  lines.append(line)

# Print all the lines
print("Here are the lines you entered:")
for line in lines:
  print(line)


# this is the fifteenth answer
import csv

def read_csv_and_print(filename):
  """Reads data from a CSV file and prints it to the console.

  Args:
      filename: The path to the CSV file to be read.
  """

  try:
    # Open the file in read mode ('r') with a context manager
    with open(filename, 'r') as csvfile:
      # Create a CSV reader object
      csv_reader = csv.reader(csvfile)

      # Print the column headers (optional)
      # print(next(csv_reader))  # Uncomment to print headers

      # Read the content row by row
      for row in csv_reader:
        # Print each row as a comma-separated string
        print(', '.join(row))

  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")

# Get the filename from the user (replace 'my_data.csv' with your actual filename)
filename = input("Enter the name of the CSV file: ")

# Read the CSV file
read_csv_and_print(filename)

#this is the sixteenth answer
def char_frequency(text):
  """Counts the frequency of each character in a string.

  Args:
      text: The string to analyze.

  Returns:
      A dictionary where keys are characters and values are their frequencies.
  """

  char_counts = {}
  for char in text:
    if char in char_counts:
      char_counts[char] += 1
    else:
      char_counts[char] = 1
  return char_counts

# Example usage
text = "This is a sample string."
char_freq = char_frequency(text)

# Print the character frequencies
for char, count in char_freq.items():
  print(f"Character '{char}': {count} occurrences")


#this is the seventeenth answer
def to_title_case(text):
  """Converts a string to title case (first letter of each word capitalized).

  Args:
      text: The string to convert.

  Returns:
      The string converted to title case.
  """

  # Split the string into words
  words = text.split()

  # Capitalize the first letter of each word
  title_case_words = [word.capitalize() for word in words]

  # Join the words back into a string with spaces
  return ' '.join(title_case_words)

# Example usage
text = "this is a sample string."
title_case_text = to_title_case(text)

print(title_case_text)  # Output: This Is A Sample String.


#this is the eighteenth answer
def is_anagram(str1, str2):
  """Checks if two strings are anagrams (have the same characters with different order).

  Args:
      str1: The first string.
      str2: The second string.

  Returns:
      True if the strings are anagrams, False otherwise.
  """

  # Convert both strings to lowercase and remove whitespaces
  str1 = str1.lower().replace(" ", "")
  str2 = str2.lower().replace(" ", "")

  # Check if the lengths are equal (anagrams must have the same length)
  if len(str1) != len(str2):
    return False

  # Create a character count dictionary for str1
  char_counts = {}
  for char in str1:
    if char in char_counts:
      char_counts[char] += 1
    else:
      char_counts[char] = 1

  # Check if each character in str2 exists in str1 with the same frequency
  for char in str2:
    if char not in char_counts or char_counts[char] == 0:
      return False
    char_counts[char] -= 1

  # If all characters in str2 are found in str1 with matching frequencies, they are anagrams
  return True

# Example usage
string3 = "silent"
string4 = "listen"

if is_anagram(string3, string4):
  print(f"'{string3}' and '{string4}' are anagrams.")
else:
  print(f"'{string3}' and '{string4}' are not anagrams.")

# this is the nineteenth answer
def remove_punctuation(text):
  """Removes all punctuation characters from a string using a loop.

  Args:
      text: The string from which to remove punctuation.

  Returns:
      The string with all punctuation characters removed.
  """

  punctuation = "!\"#$%&()*+,/:;<=>?@[]\\^_`{|}~"
  no_punct_text = ""
  for char in text:
    if char not in punctuation:
      no_punct_text += char
  return no_punct_text

# Example usage
text = "This is a string! with punctuation?"
text_without_punct = remove_punctuation(text)
print(f"Original text: '{text}'")
print(f"Text without punctuation: '{text_without_punct}'")

#this is the twenteeth answer
def sum_of_numbers(numbers):
  """Calculates the sum of all numbers in a list.

  Args:
      numbers: A list of numbers.

  Returns:
      The sum of all numbers in the list.
  """

  return sum(numbers)

# Example usage
number_list = [1, 2, 3, 4, 5]
total_sum = sum_of_numbers(number_list)
print(f"The sum of the numbers in the list is: {total_sum}")

#this is the twenty first answer
def count_occurrences(list1, element):
  """Counts the occurrences of a specific element in a list using the 'count' method.

  Args:
      list1: The list to search within.
      element: The element to count occurrences of.

  Returns:
      The number of times the element appears in the list.
  """

  return list1.count(element)

# Example usage
my_list = [1, 2, 3, 2, 1, 4, 2]
element_to_count = 2
number_of_occurrences = count_occurrences(my_list, element_to_count)
print(f"The element {element_to_count} appears {number_of_occurrences} times in the list.")

# this is the twenty second answer
def get_min_max(numbers):
  """Returns the minimum and maximum values in a list using built-in functions.

  Args:
      numbers: A list of numbers.

  Returns:
      A tuple containing the minimum and maximum values in the list.
  """

  # Check for empty list to avoid errors
  if not numbers:
      return None, None

  minimum_value = min(numbers)
  maximum_value = max(numbers)
  return minimum_value, maximum_value

# Example usage
number_list = [5, 1, 8, 3, 9]
min_value, max_value = get_min_max(number_list)

print(f"Minimum value: {min_value}")
print(f"Maximum value: {max_value}")

# this is the twenty third answer
def convert_temperature(temperature, scale):
  """Converts temperature between Celsius and Fahrenheit based on user input.

  Args:
      temperature: The temperature value to convert.
      scale: The temperature scale ("C" for Celsius, "F" for Fahrenheit).

  Returns:
      The converted temperature value.
  """

  if scale.upper() == "C":
    # Convert Celsius to Fahrenheit
    return (temperature * 9/5) + 32
  elif scale.upper() == "F":
    # Convert Fahrenheit to Celsius
    return (temperature - 32) * 5/9
  else:
    print("Invalid temperature scale. Please enter 'C' or 'F'.")
    return None

# Get user input for temperature and scale
while True:
  try:
    temperature = float(input("Enter a temperature value: "))
    scale = input("Enter the temperature scale (C or F): ").upper()
    break  # Exit the loop if valid input is entered
  except ValueError:
    print("Invalid input. Please enter a numerical temperature value.")

# Convert the temperature and print the result
converted_temperature = convert_temperature(temperature, scale)

if converted_temperature is not None:
  print(f"{temperature:.2f} degrees {scale} is equal to {converted_temperature:.2f} degrees {'F' if scale == 'C' else 'C'}")

#this is the twenty fourth answer
def calculate(num1, num2, operator):
  """Performs basic arithmetic operations on two numbers.

  Args:
      num1: The first number.
      num2: The second number.
      operator: The arithmetic operator (+, -, *, /).

  Returns:
      The result of the operation, or None if an error occurs.
  """

  if operator == "+":
    return num1 + num2
  elif operator == "-":
    return num1 - num2
  elif operator == "*":
    return num1 * num2
  elif operator == "/":
    if num2 == 0:
      print("Error: Division by zero is not allowed.")
      return None
    else:
      return num1 / num2
  else:
    print("Invalid operator. Please use +, -, *, or /.")
    return None

while True:
  try:
    # Get user input for numbers and operator
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter an operator (+, -, *, /): ")

    # Perform the calculation and print the result
    result = calculate(num1, num2, operator)
    if result is not None:
      print(f"{num1} {operator} {num2} = {result:.2f}")  # Format result with 2 decimal places
      break  # Exit the loop after successful calculation

  except ValueError:
    print("Invalid input. Please enter numbers and a valid operator.")

print("Thanks for using the calculator!")

# this is the twenty fifth answer
def copy_text_file(source_file, destination_file):
  """Copies the contents of a text file to another text file.

  Args:
      source_file: The path to the source text file.
      destination_file: The path to the destination text file.

  Raises:
      FileNotFoundError: If the source file is not found.
      IOError: If there's an error while reading or writing the files.
  """

  try:
    # Open the source file in read mode with a context manager
    with open(source_file, 'r') as source:
      # Read the entire content of the source file
      source_data = source.read()

    # Open the destination file in write mode with a context manager
    with open(destination_file, 'w') as destination:
      # Write the source file content to the destination file
      destination.write(source_data)

    print(f"Successfully copied '{source_file}' to '{destination_file}'.")

  except FileNotFoundError as e:
    print(f"Error: Source file '{source_file}' not found.")
    raise  # Re-raise the exception for further handling (optional)
  except IOError as e:
    print(f"Error: An error occurred while copying the file. {e}")

# Get the filenames from the user
source_file = input("Enter the name of the source text file: ")
destination_file = input("Enter the name of the destination text file: ")

# Copy the file content
copy_text_file(source_file, destination_file)


# this is the twenty sixth answer
def check_prefix_suffix(text, prefix, suffix):
  """Checks if a string starts with a prefix and/or ends with a suffix.

  Args:
      text: The string to check.
      prefix: The prefix to compare with (optional).
      suffix: The suffix to compare with (optional).

  Returns:
      A dictionary indicating if the prefix and/or suffix match.
  """

  results = {}
  if prefix:
    results["starts_with_prefix"] = text.startswith(prefix)
  if suffix:
    results["ends_with_suffix"] = text.endswith(suffix)
  return results

# Example usage
text = "This is a sample text."
prefix = "This"
suffix = "text."

check_results = check_prefix_suffix(text, prefix, suffix)

if check_results:
  print("Text check results:")
  for key, value in check_results.items():
    print(f" - {key}: {value}")
else:
  print("No prefix or suffix checks were performed.")


# this is the twenty seventh answer
def convert_to_char_list(text):
  """Converts a string into a list of its characters using a loop.

  Args:
      text: The string to convert.

  Returns:
      A list of characters from the string.
  """

  char_list = []
  for char in text:
    char_list.append(char)
  return char_list

# Example usage
text = "Hello, world!"
char_list = convert_to_char_list(text)
print(char_list)







