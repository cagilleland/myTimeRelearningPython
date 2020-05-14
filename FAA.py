#Frequency Analysis App

from collections import Counter

print("Welcome to the frequency analysis app")

non_letters = ['1','2','3','4','5','6','7','8','9','0',' ',',','"','.','<','>','?','!']

kp1 = input("What phrase would you like an analysis on? ").lower().strip()

for i in non_letters:
    kp1 = kp1.replace(i, '')

total_letters = len(kp1)

letter_count = Counter(kp1)

print("\nHere is the frequency of letters in your phrase: \n\n\tLetter\tNumber\tPercentage")
for key,value in letter_count.items():
    print("\t" +key + "\t" + str(value) + "\t" + str(round((value/total_letters)*100,2)) + "%")

ordered_letters = letter_count.most_common()
kp1_ordered = []
for pair in ordered_letters:
    kp1_ordered.append(pair[0])

for letter in kp1_ordered:
    print(letter, end=" ")
