ss = "hello"

def iterateReverseStr(ss):
	a = 0
	b = len(ss)-1
	arr = list(ss)
	while b > a:
		temp = arr[a]
		arr[a] = arr[b]
		arr[b] = temp

		a += 1
		b -= 1
	return ''.join(arr)


print(iterateReverseStr(ss))


def recursivelyReverseStr(ss, start, end):
	if(end <= start):
		return ss

	arr = list(ss)
	temp = arr[start]
	arr[start] = arr[end]
	arr[end] = temp

	newStr = "".join(arr)
	return recursivelyReverseStr(newStr, start+1, end-1)


print(recursivelyReverseStr(ss, 0, len(ss)-1))
