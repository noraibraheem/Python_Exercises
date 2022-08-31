num = int(input())


def fibonacci(n):
	#complete the recursive function
	if n>1 :  #positive num
		List=[0,1]
		print(List[0])
		print(List[1])
		for i in range (2,n):
			List.append(List[i-1]+List[i-2])
			print(List[i])
		

			


fibonacci(num)


def least_difference(a, b, c):
    """Return the smallest difference between any two numbers
    among a, b and c.
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return  min(diff1, diff2, diff3)
    
print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7),
)



#