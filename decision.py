#1.take an input year from user and decide whether it is a leap year or not

yr = int(input("enter a year:"))
if (yr%4 == 0):
    
    if (yr % 100 == 0):
        
        if (yr % 400 == 0):
            print("%d is leap year" %yr)

        else:
            print("%d is not a leap year" %yr)

    else:
        print("%d is leap year" %yr)

else:
    print("%d is not a leap year" %yr)

print("\n")
    
#2.take length and breadth input from user and check whether the dimensions are of square or rectangle


ln = int(input("enter the length"))
br = int(input("enter the breadth"))

if (ln == br):
    print("Thde dimensions are of a SQUARE")

elif (ln != br):
    print("Thde dimensions are of a RECTANGLE")

else:
    print("INVALID INPUT")

print("\n")
       
#3.take the input age of 3 people and determine oldest and youngest among them.

age_p1 = int(input("enter the age of first person"))
age_p2 = int(input("enter the age of second person"))
age_p3 = int(input("enter the age of third person"))
if (age_p1 != age_p2 != age_p3):
    if(age_p1 > age_p2 and age_p1 > age_p3):
        print("FIRST PERSON having age :%d is OLDEST" %age_p1)

        if(age_p2 > age_p3):
            print("THIRD PERSON having age:%d is YOUNGEST" %age_p3)

        else:
            print("SECOND PERSON having age:%d is YOUNGEST" %age_p2)

    elif(age_p2 > age_p1 and age_p2 > age_p3):
        print("SECOND PERSON having age :%d is OLDEST" %age_p2)

        if(age_p1 > age_p3):
            print("THIRD PERSON having age:%d is YOUNGEST" %age_p3)

        else:
            print("FIRST PERSON having age:%d is YOUNGEST" %age_p1)

    elif(age_p3 > age_p1 and age_p3 > age_p2):
        print("THIRD PERSON having age :%d is OLDEST" %age_p3)

        if(age_p1 > age_p2):
            print("SECOND PERSON having age:%d is YOUNGEST" %age_p2)

        else:
            print("FIRST PERSON having age:%d is YOUNGEST" %age_p1)

    else:
        print("INVALID INPUT")

else:
    print("Ages of the three persons are NOT DIFFERENT")

print("\n")

#4. Write an if statement that lets a competitor know which of these prizes they won based on the number of points they scored, which is stored in the integer variable points(your input). points can only take on positive integer values up to 200. 
#If they've won a prize, the message should state "Congratulations! You won a [prize name]!" with the prize name. If there's no prize, the message should state "Sorry! No prize this time."

#Points	        Prize
#1-50	        No Prize
#51-150 	Wooden Dog
#151-180	Book
#181-200	Chocolates

pt = int(input("enter the point scored by the candidate"))

if(0 < pt <= 200):

    if(181 <= pt <= 200):
        print("CONGRATULATIONS! You won a pack of CHOCOLATES")

    elif(151 <= pt <= 180):
        print("CONGRATULATIONS! You won a BOOK")

    elif(51 <= pt <= 150):
        print("CONGRATULATIONS! You won a WOODEN DOG")

    elif(1 <= pt <= 50):
        print("SORRY! No prize this time")

    else:
        print("INVALID INPUT")

else:
    print("POINTS OUT OF RANGE-Maximun points that can be scored by a candidate are 200")

print("\n")

#5.A shop will give discount of 10% if the cost of purchased quantity is more than 1000.Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user. 
    
quant = (int(input("enter the quantity of the item purchased")))
#if one unit costs 100 then amount would be calculated as :
amount = (quant*100)

if(amount > 1000):
       dis = 0.1*amount
       bill = amount-dis
       print("TOTAL AMOUNT \t %f" %amount)
       print("DISCOUNT \t %f " %dis)
       print("TOTAL COST \t %f" %bill)

else:
       dis = 0.0
       bill = amount
       print("TOTAL AMOUNT \t %f" %amount)
       print("DISCOUNT \t %f " %dis)
       print("TOTAL COST \t %f" %amount)
