
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


# 1. Find the length of the set it_companies
print(len(it_companies))
# 2. Add 'Twitter' to it_companies
it_companies.add("Twitter")
# 3. Insert multiple IT companies at once to the set it_companies

# 4. Remove one of the companies from the set it_companies
it_companies.discard('Google')
# it_companies.remove('Google')

print(it_companies)
# 5. What is the difference between remove and discard
print("discard doesnt raise error if element not found")
# 6. Join A and B
c = A.union(B)
print(c)
# 7. Find A intersection B
d = A.intersection(B)
print(d)
# 8. Is A subset of B
print(A.issubset(B))
# 9. Are A and B disjoint sets
print(A.isdisjoint(B))
# 10. Join A with B and B with A
c = A.union(B)
d = B.union(A)
print("c", c, "d", d )
# 11. What is the symmetric difference between A and B
print(A.symmetric_difference(B))
# 12. Delete the sets completely
del A
# 13. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
ages = set(age)
print(len(ages), len(age))
# 14. Explain the difference between the following data types: string, list, tuple and set

# 15. _I am a teacher and I love to inspire and teach people._ How many unique words have been used in the sentence? You did not learn loops yet you can do it manually.
sent = "I am a teacher and I love to inspire and teach people"
sent = sent.split(' ')
sent = set(sent)
print(len(sent))
print(sent)
# 🎉 CONGRATULATIONS ! 🎉