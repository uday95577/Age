x = int(input("Please enter your age: "))
if(x < 18):
    print(" You are a minor")
elif(x>=18 and x<65):
    print("You are an adult")
elif(x>=65):
    print("You are a senior")
