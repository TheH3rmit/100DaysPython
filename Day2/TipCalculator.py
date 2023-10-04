print("Welcom to tip calculator")
print("What was the total of the bill: $")
bill = float(input())
print("Between how many people split the bill?")
people = int(input())
print("What precentage of the bill should be tip? ")
tip_procent = float(input())/100
tip = bill*tip_procent
total = bill+tip
split = (total/people)
print(f"Each person must pay {round(split,2)}")
