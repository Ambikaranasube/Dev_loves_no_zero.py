'''Dev loves the number zero. Dev gives Andrew two integers X and Y and asks him to 
perform the steps below on X and Y. until the value of Y has been reduced to zero. 
The below steps should be followed sequentially:
1. If X<="" p="" style="box-sizing: inherit;">
2. If Y=0. then return X
3. Otherwise, let T =X-Y.
4. Set X=Y and then set Y=T
5. Repeat from step 1.
Your task is to help Andrew find and return an integer value, representing the value of 
X, when the value of Y has been reduced to zero.
Note: At least one of the X or Y will be a non-zero integer
Input Specification:
input1: An integer value X. representing the first number.
Input2: An integer value Y, representing the second number
Sample input:
48
18
Sample Output:
6'''

'''if Y is already 0, you should immediately return X because there's no need for further operations.
Otherwise, compute T as the difference between X and Y (i.e., T = X - Y).
Update X to be Y (X = Y).
Update Y to be T (Y = T).
Repeat the above steps until Y becomes 0.
Output: Once Y becomes 0, return the current value of X.'''
X=int(input("enter the x value "))
Y=int(input("enter the y value"))
while(Y>0):
    if (Y>X):
        X,Y=X,Y
    else:
        X,Y=Y,X-Y
print(X)
