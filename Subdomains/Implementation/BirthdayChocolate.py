
# Complete the birthday function below.
def fun(array, date, length):
    count = 0
    for i in range(len(array)-length+1):
        if sum(array[i:i+length]) is date:
            count+=1
    return count

    
