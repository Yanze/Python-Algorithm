s = "asahello"

def func(s):
	count = {}
	for i in s:
		if i in count:
			count[i] += 1
		else:
			count[i] = 1
	for i in s:
		if count[i] == 1:
			return i


func(s)
