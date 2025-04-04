def factorial(x):
    if(x<0):
        print("Factorial doesnt exist")
        return None
    if(x==0) or (x==1) :
        return 1
    else :
        return x * factorial(x-1)
    
def power(x,y):
    if y==0:
        return 1 
    if y==1:
        return x
    else : 
        return x * power(x,y-1)