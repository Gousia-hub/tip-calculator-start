#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python


print("welcome to the tip calculator")
tot = input("what was the total bill? $")

tb = float(tot)

perc = input("what percentage tip would u like to give? 10, 12, 15? ")
x = float(perc)/100 + 1
tt = tb * x
ppl = input("How many ppl to split the bill? ")
#print(type(ppl))
sp = tt / int(ppl)
rou = round(sp,2)
pay = print(f"each person shud pay: ${rou} ")
