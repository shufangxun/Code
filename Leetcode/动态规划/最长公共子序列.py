def LCS(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[0 for i in range(n+1)] for j in range(m+1)]
    if len(s1) == 0 or len(s2) == 0:
        return 0
    else:
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]


def PrintLCS(X, Y, m, n):
    
	L = [[0 for x in range(n+1)] for x in range(m+1)] 
	for i in range(m+1): 
		for j in range(n+1): 
			if i == 0 or j == 0: 
				L[i][j] = 0
			elif X[i-1] == Y[j-1]: 
				L[i][j] = L[i-1][j-1] + 1
			else: 
				L[i][j] = max(L[i-1][j], L[i][j-1]) 

	# Following code is used to print LCS 
	index = L[m][n] 

	# Create a character array to store the lcs string 
	lcs = [""] * (index+1) 
	lcs[index] = "" 

	# Start from the right-most-bottom-most corner and 
	# one by one store characters in lcs[] 
	i = m 
	j = n 
	while i > 0 and j > 0: 

		# If current character in X[] and Y are same, then 
		# current character is part of LCS 
		if X[i-1] == Y[j-1]: 
			lcs[index-1] = X[i-1] 
			i-=1
			j-=1
			index-=1

		# If not same, then find the larger of two and 
		# go in the direction of larger value 
		elif L[i-1][j] > L[i][j-1]: 
			i-=1
		else: 
			j-=1

	print("".join(lcs))

if __name__ == "__main__":
    s1 = "abcbdab"
    s2 = "bdcaba"
    m = len(s1) 
    n = len(s2) 
    PrintLCS(s1, s2, m, n) 
    print(LCS(s1,s2))