# 4.Task
# 	Given an integer, , perform the following conditional actions:

# 		If n is odd, print Weird
# 		If n is even and in the inclusive range of 2 to 5, print Not Weird
# 		If n is even and in the inclusive range of 6 to 20, print Weird
# 		If n is even and greater than 10, print Not Weird
# 		Input Format
# 	1

# 		Output Format

# 		Print Weird if the number is weird. Otherwise, print Not Weird.

# 		Sample Input 0

# 		3
# 		Sample Output 0

# 		Weird
# 		Explanation 0

# 		n=3
# 		n is odd and odd numbers are weird, so print Weird.

# 		Sample Input 1

# 		24
# 		Sample Output 1

# 		Not Weird
# 		Explanation 1
		
# 		n=24

# 		n>20 and n is even, so it is not weird.




n=int(input("entre the number"))
if n%2 !=0:
    print("weird")
elif n>=2 and n<=5:
    print("not weird")
elif n>=6 and n<=20:
    print("weird")
else:
    print("not weird")    
