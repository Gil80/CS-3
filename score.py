#  Exercise 3: Write a program to prompt for a score between 0.0 and 1.0.
#  If the score is out of range, print an error message.
#  If the score is between 0.0 and 1.0,
#  print a grade using the following table:
#  Score   Grade
#  >= 0.9     A
#  >= 0.8     B
#  >= 0.7     C
#  >= 0.6     D
#  < 0.6      F

type_score = input("Enter Score Between 0.0 and 1.0: ")
try:
    score = float(type_score)
except:
    print('Bad Score')
    exit()
if score >= 0.9 and score < 1.1:
    print('A')
elif score >= 0.8 and score < 0.9:
    print('B')
elif score >= 0.7 and score < 0.8:
    print('C')
elif score >= 0.6 and score < 0.7:
    print('D')
elif score >= 0.0 and score < 0.6:
    print('F')
else:
    print("Bad Score")
