str1 = "Sore was I ere I saw Eros"




def isPalindrome(str1):
	s1 = "".join(str1.split()).lower()
	start = 0
	end = len(s1)-1

	while end > start:
		if s1[start] != s1[end]:
			return False
		start += 1
		end -= 1
	return True


print(isPalindrome(str1))
