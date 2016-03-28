str1 = "dave barry"
str2 = "ray adverb"

def isAnagram(str1, str2):
	s1 = "".join(str1.split())
	s2 = "".join(str2.split())
	if(len(s1) != len(s2)):
		return False
	count1 = {}
	count2 = {}
	for i in range(0, len(s1)):
		current1 = s1[i]
		current2 = s2[i]
		if current1 in count1:
			count1[current1] += 1
		else:
			count1[current1] = 1

		if current2 in count2:
			count2[current2] += 1
		else:
			count2[current2] = 1

	for key, value in count1.items():
		if key not in count2 or (count1[key] != count2[key]):
			return False
	return True





def isAnagram2(str1, str2):
	s1 = "".join(str1.split())
	s2 = "".join(str2.split())
	if(len(s1) != len(s2)):
		return False
	count = {}
	for i in range(0, len(s1)):
		current1 = s1[i]
		current2 = s2[i]
		if current1 in count:
			count[current1] += 1
		else:
			count[current1] = 1

		if current2 in count:
			count[current2] -= 1
		else:
			count[current2] = -1

	for key, value in count.items():
		if value != 0:
			return False
	return True



print(isAnagram2(str1, str2))
