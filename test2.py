# Read the contents of file3.txt
file_path = 'f3.txt'
student_data = []

with open(file_path, 'r') as file:
    lines = file.readlines()

# Process the lines to create a dictionary
current_student = {}
for line in lines:
    line = line.strip()
    if line:
        key, value = line.split(': ')
        current_student[key] = value
    else:
        student_data.append(current_student)
        current_student = {}

# Append the last student record
if current_student:
    student_data.append(current_student)

# Construct a dictionary using Roll numbers as keys
student_dict = {}
for student in student_data:
    roll_number = student.get('Roll')
    if roll_number:
        student_dict[roll_number] = {
            'Name': student.get('Name'),
            'Section': student.get('Section'),
            'Semester': student.get('Semester')
        }

# Display the dictionary
print(student_dict)

# Read the contents of file1.txt
with open('file1.txt', 'r') as file:
    content = file.read()

# Reverse the content
reversed_content = content[::-1]

# Write the reversed content back to file1.txt
with open('file1.txt', 'w') as file:
    file.write(reversed_content)