
# 1. Declare an empty list
empty_list = []
emptylist = list()
# 2. Declare a list with more than 5 items
list_of_5 = [1,2,3,4,5]
# 3. Find the length of your list
len(list_of_5)
# 4. Get the first item, the middle item and the last item of the list
first = list_of_5[0]
last = list_of_5[-1]
middle = list_of_5[len(list_of_5)//2]
# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Jade", 23, "6.0'", "single", "Mind your Business ave"]
# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# 7. Print the list using _print()_
print(it_companies)
# 8. Print the number of companies in the list
print(len(it_companies))
# 9. Print the first, middle and last company
first = it_companies[0]
last = it_companies[-1]
middle = it_companies[len(list_of_5)//2]
# 10. Print the list after modifying one of the companies
it_companies[2]="Shopify"
# print(it_companies)
# 11. Add an IT company to it_companies
it_companies.append("Microsoft")

# 12. Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies)//2, "Netflix")
# print(it_companies)
# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0]=it_companies[0].upper()
# print(it_companies)
# 14. Join the it_companies with a string '#;&nbsp; '
it_companies.extend("#")
# print(it_companies)
# 15. Check if a certain company exists in the it_companies list.
# print("Apple" in it_companies)
# 16. Sort the list using sort() method
it_companies.sort()
# print(it_companies)
# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)
# 18. Slice out the first 3 companies from the list
print(it_companies[:3])

# 19. Slice out the last 3 companies from the list
print(it_companies[-3:])
# 20. Slice out the middle IT company or companies from the list
middle = it_companies[len(it_companies)//2:len(it_companies)//2+2]
print(middle)
# 21. Remove the first IT company from the list
del it_companies[0]
print(it_companies)
# 22. Remove the middle IT company or companies from the list
del it_companies[len(it_companies)//2:len(it_companies)//2+2]
print(it_companies)
# 23. Remove the last IT company from the list
it_companies.pop()
# 24. Remove all IT companies from the list
it_companies.clear()
# 25. Destroy the IT companies list
del it_companies
# 26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']  
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
full_stack = front_end.copy()
# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
print(full_stack)

redux_index = full_stack.index("Redux")
print(redux_index)
full_stack.insert(redux_index+1, "SQL")
full_stack.insert(redux_index+1, "Python")
print(full_stack)

# 1. The following is a list of 10 students ages:

# ```sh
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# ```

# - Sort the list and find the min and max age
ages.sort()
min_age = min(ages)
max_age = max(ages)
# - Add the min age and the max age again to the list
ages.extend([min_age, max_age])
print(ages)
# - Find the median age (one middle item or two middle items divided by two)
if len(ages)%2==0:
   median = sum(ages[len(ages)//2:len(ages)//2+2])/2
else:
    median = ages[len(ages)//2]

print(median)
# - Find the average age (sum of all items divided by their number 
average = sum(ages)/len(ages)
print(average)
# - Find the range of the ages (max minus min)
age_range = max_age - min_age
print(age_range)
# - Compare the value of (min - average) and (max - average), use _abs()_ method
comparison =abs(abs(min_age - average) - abs(max_age - average)) 
print(comparison)

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zimbabwe',
]

# 1. Find the middle country(ies) in the [countries list](https://github.com/Asabeneh/30-Days-Of-Python/tree/master/data/countries.py)
country = countries[len(countries)//2]
print(country)
# 1. Divide the countries list into two equal lists if it is even if not one more country for the first half.
if len(countries)%2==0:
    first_half = countries[:len(countries)//2]
    second_half = countries[len(countries)//2:]
else:
    first_half = countries[:len(countries)//2+1]
    second_half = countries[len(countries)//2+1:]

print(len(first_half))
print(len(second_half))
# 1. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
list_of_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
china, russia, usa, *rest = list_of_countries
print(rest)