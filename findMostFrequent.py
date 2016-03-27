arr = [1,2,3, 2, 10, 5, 10, 10, 2, 2]



def findMostFrequent(arr):
	count = {}
	mostFrequent = 0
	val = 0
	for i in range(0, len(arr)):
		current = arr[i]
		if current in count:
			count[current] += 1
			if mostFrequent < count[current]:
				mostFrequent = count[current]
				val = current
		else:
			count[current] = 1
	return val






findMostFrequent(arr)
