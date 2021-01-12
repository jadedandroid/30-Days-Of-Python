
# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
# 3. Declare a variable named company and assign it to an initial value "Coding For All".
# 4. Print the variable company using _print()_.
# 5. Print the length of the company string using _len()_ method and _print()_.
# 6. Change all the characters to capital letters using _upper()_ method.
# 7. Change all the characters to lowercase letters using _lower()_ method.
# 8. Use capitalize(), title(), swapcase() methods to format the value of the string _Coding For All_.
# 9. Cut(slice) out the first word of _Coding For All_ string.
# 10. Check if _Coding For All_ string contains a word Coding using the method index, find or other methods.
# 11. Replace the word coding in the string 'Coding For All' to Python.
# 12. Change Python for Everyone to Python for All using the replace method or other methods.
# 13. Split the string 'Coding For All' using space as the separator (split()) .
# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
# 15. What is the character at index 0 in the string _Coding For All_.
# 16. What is the last index of the string _Coding For All_.
# 17. What character is at index 10 in "Coding For All" string.
# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
# 19. Create an acronym or an abbreviation for the name 'Coding For All'.
# 20. Use index to determine the position of the first occurrence of C in Coding For All.
# 21. Use index to determine the position of the first occurrence of F in Coding For All.
# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
# 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# 24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# 25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# 26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# 27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# 28. Does '\'Coding For All' start with a substring _Coding_?
# 29. Does 'Coding For All' end with a substring _coding_?
# 30. '&nbsp;&nbsp; company For All &nbsp;&nbsp;&nbsp; &nbsp;' &nbsp;, remove the left and right trailing spaces in the given string.
# 31. Which one of the following variables return True when we use the method isidentifier():
#     - 30DaysOfPython
#     - thirty_days_of_python
# 32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
# 33. Use the new line escape sequence to separate the following sentences.
#     ```py
#     I am enjoying this challenge.
#     I just wonder what is next.
#     ```
# 34. Use a tab escape sequence to write the following lines.
#     ```py
#     Name      Age     Country
#     Asabeneh  250     Finland
#     ```
print("Name\tAge\tCountry\nAsabene\t250\tFinland")

# 35. Use the string formating method to display the following:

# ```sh
# radius = 10
# area = 3.14 * radius ** 2
# The area of a cricle with radius 10 is 314 meters square.
# ```
radius = 10
area = 3.14 * radius ** 2
print(f'The area of a cricle with radius 10 is {area} meters square.')



# 36. Make the following using string formating methods:

# ```sh
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144
# ```


# string = 'Thirty ' + 'Days '+ 'Of ' + 'Python '
# print(string)
# company = 'Python '+ 'For ' + 'Everyone'
# name = 'Coding For All'
# name1 = 'Coding For All people'
# # print(company)
# # len(company)
# # print(company.upper())
# # print(company.lower())
# # print(company.capitalize())
# # print(company.title())
# # print(company.swapcase())
# # print(company.split(" ")[0])

# # print(company[::-1])
# # print(company.index('Coding', 5))
# # print(company.replace("Coding", "Python"))
# # print("Python for Everyone".replace("Everyone", "All"))
# # print(company.split())
# # org = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 
# # # print(org.split(","))
# # print(company[0])
# # print(company[-1])
# # print(company[10])
# def abbreviation(s):
#     final = ''
#     for i in s:
#         if i.isupper():
#             final+= i
#     return final
# print(abbreviation(name))
# print(abbreviation(company))
# print(name.index('C'))
# print(name.index('F'))
# # print(name1.index('l', -1))
# sentence = 'You cannot end a sentence with because because because is a conjunction'
# print(sentence.find("because"))
# print(sentence.rfind("because"))
# print(sentence.replace("because because because","bc bc bc"))

# print(name.startswith("Coding"))
# print(name.endswith("Coding"))
# random = '&nbsp;&nbsp; company For All &nbsp;&nbsp;&nbsp; &nbsp;'
# print(random.strip())
# newline = 'py \n I am enjoying this challenge.\n I just wonder what is next.'
# print(newline)
# challenge = '30-thirty_days_of_python'
# print(challenge.isidentifier())

# 34.
num_1 = 8
num_2 = 6
num_3 = num_1**num_2
print(f'{num_1}^{num_2}={num_3}')
