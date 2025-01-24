my_list = ["apple", "orange", "watermelon",3.14,]# Existing code
my_list = ["apple", "orange", "watermelon", 3.14]

# New code
students_scores = {
     "Ben": 90,
    "Anne": 95,
    "Frank": 100,
    "Alice": 95,
    "Ricardo": 100
}

# Calculate the average score
total_score = sum(students_scores.values())
number_of_students = len(students_scores)
average_score = total_score / number_of_students

print(f"The average score is: {average_score}")


total_score = 0
number_of_students = len(students_scores)

for score in students_scores.values():
    total_score += score

average_score = total_score / number_of_students

print(f"The average score is: {average_score}")


students_scores = {
    "Ben": 90,
    "Anne": 95,
    "Frank": 100,
    "Alice": 95,
    "Ricardo": 100
}

average_score = sum([score for score in students_scores.values()]) / len(students_scores)
print(f"The average score is: {average_score}")


# Using list comprehension
average_score = sum([score for score in students_scores.values()]) / len(students_scores)
print(f"The average score is: {average_score:.2f}")

# Find the highest score
highest_score = max(students_scores.values())

# Create a list of students who got the highest score
top_students = [student for student, score in students_scores.items() if score == highest_score]

print(f"The highest score is: {highest_score}")
print(f"Students who got the highest score: {top_students}")

# Find the highest score without using max function
highest_score = None
for score in students_scores.values():
    if highest_score is None or score > highest_score:
        highest_score = score

# Create a list of students who got the highest score without list comprehension
top_students = []
for student, score in students_scores.items():
    if score == highest_score:
        top_students.append(student)


print(f"The highest score is: {highest_score}")
print(f"Students who got the highest score: {top_students}")


# Find the highest score and create a list of students who got the highest score in a single iteration
highest_score = None
top_students = []

for student, score in students_scores.items():
    if highest_score is None or score > highest_score:
        highest_score = score
        top_students = [student]  # Start a new list with the current student
    elif score == highest_score:
        top_students.append(student)  # Add to the list of top students

print(f"The highest score is: {highest_score}")
print(f"Students who got the highest score: {top_students}")


# Create a list of students whose names start with 'A' using list comprehension
students_starting_with_A = [student for student in students_scores.keys() if student.startswith('A')]

print(f"Students whose names start with 'A': {students_starting_with_A}")


# Create a list of students whose names start with 'A' without using list comprehension
students_starting_with_A = []
for student in students_scores.keys():
    if student.startswith('A'):
        students_starting_with_A.append(student)

print(f"Students whose names start with 'A': {students_starting_with_A}")

fav_numbers = [1,2,3,4,5,-6,8]

fav_numbers = [1, 2, 3, 4, 5, -6, 8]

# Using list comprehension to create a list of positive and even numbers
positive_even_numbers = [num for num in fav_numbers if num > 0 and num % 2 == 0]

print(f"Positive and even numbers: {positive_even_numbers}")


word = "amazing"

# Count the occurrences of each letter
letter_counts = {letter: word.count(letter) for letter in set(word)}

# Find the maximum count
max_count = max(letter_counts.values())

# Identify the letter(s) with the maximum count
most_recurring_letters = [letter for letter, count in letter_counts.items() if count == max_count]

print(f"The most recurring letter(s): {most_recurring_letters}")


word = "amazing"

# Create a dictionary that finds the frequency of each letter
letter_frequency = {letter: word.count(letter) for letter in set(word)}

print(f"Letter frequency: {letter_frequency}")



word = "amazing"

# Create an empty dictionary
letter_frequency = {}

# Iterate through the word and add to the dictionary
for letter in word:
    if letter in letter_frequency:
        letter_frequency[letter] += 1
    else:
        letter_frequency[letter] = 1

print(f"Letter frequency: {letter_frequency}")