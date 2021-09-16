#p203 Q8
def food_cost(a,b):
    kgs=a/1000
    cost=kgs*b

while True:
    try:
        animal=input("what type of animal are you feeding(h for hampster or c for cat)")
        food=int(input("what do number do you need to count?"))
        
    except ValueError:
        print("Invalid Input")
    else:
if animal=="h":
    