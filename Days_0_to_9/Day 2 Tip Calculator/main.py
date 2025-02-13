#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill = input("What is the bill?\n")
cbill = float(bill)

tip = input("What would you like to tip the tip?\n10%, 15%, 20%?\n")
ctip = float(tip)

people = input("How many people are splitting the bill?")
cpeople = int(people)

total_amount = cbill + (cbill*ctip/100)
amount_per_person = total_amount/cpeople
print(f"\nThe total amount is {total_amount}")
print(f"Each person should pay {amount_per_person}")
                                

      
