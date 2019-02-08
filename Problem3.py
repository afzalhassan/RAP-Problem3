# 3. Given an object/dictionary, containing names as keys and amount_paid by each of them as values, write a function that takes such an object as input and calculates the total sum paid by them together.
# Below is an example:
# Input: {"Rick": 85, "Amit": 42, "George": 53, "Tanya": 60, "Linda": 35}
# Output: 275 

dicti = {"Rick": 85, "Amit": 42, "George": 53, "Tanya": 60, "Linda": 35}
sum1 = 0
for k,v in dicti.items():
    sum1 += v

print (sum1)
