students = []
scores = []

# Read total number of students
for _ in range(int(input())):
    name = input()
    score = float(input())

    # Store data into respective lists
    students.append([name, score])
    scores.append(score)
    
# Get the second lowest unique grade
second_lowest_grade = sorted(set(scores))[1]

# Filter student names that match the second lowest grade
result_names = [name for name, score in students if score == second_lowest_grade]

# Print the names with 2nd lowest scores sorted alphabetically
for name in sorted(result_names):
    print(name)



