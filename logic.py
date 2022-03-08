def is_prime(n):
    temp=0
    for i in range(2,n):
        if(n%i==0):
            temp=1
    if(temp==1 or n==1):
        return False
    else:
        return True

def calculate_prime(start,finish):
    list_prime=[]
    for i in range(start,finish+1):
        if is_prime(i)==True:
            list_prime.append(i)
    return list_prime

