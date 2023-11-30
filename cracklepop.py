"""Write a program that prints out the numbers 1 to 100 (inclusive).
 If the number is divisible by 3, print Crackle instead of the number. 
 If it's divisible by 5, print Pop. 
 If it's divisible by both 3 and 5, print CracklePop. You can use any language.
"""

i = 1
while i <= 100:
    print(i)
    if i/3:
        print("Crackle")
    if i/5:
        print("Pop")
    if  i/3 and i/5:
        print("CracklePop")

    i += 1
    