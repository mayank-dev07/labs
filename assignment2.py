#Reverse the contents of the file1.txt.
CODE:----
file_path = 'file1.txt'
with open(file_path, 'r') as file:
    content = file.read()
reversed_content = content[::-1]
with open(file_path, 'w') as file:
    file.write(reversed_content)
print("Contents of file1.txt have been reversed.")



#Convert all the numbers in the file2.txt to text. 
#Ex: This file has numbers 1,2
#Convert it to : This file has numbers one,two
CODE:----
import inflect
def convert_numbers_to_text(content):
    p = inflect.engine()
    words = content.split()
    for i, word in enumerate(words):
        if word.isdigit():
            words[i] = p.number_to_words(word)
    return ' '.join(words)
file_path = 'file2.txt'
with open(file_path, 'r') as file:
    content = file.read()
converted_content = convert_numbers_to_text(content)
with open(file_path, 'w') as file:
    file.write(converted_content)
print("Numbers in file2.txt have been converted to text.")



#Prepare a dictionary from file3.txt.
#Dataset: f1.txt , f2.txt, f3.txt
CODE:----
file_path = 'file3.txt'
def create_dictionary_from_file(file_path, delimiter=':'):
    result_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            key, value = map(str.strip, line.split(delimiter, 1))
            result_dict[key] = value
    return result_dict
my_dict = create_dictionary_from_file(file_path)
print("Dictionary from file3.txt:")
print(my_dict)

