
flag = "LitecOiN"
alpha = ["A","B","C","D","E","F","G","H","I","J","K","L",
         "M","N","O","P","Q","R","S","T","U","V","W","X",
         "Y","Z","0","1","2","3","4","5","6","7"]
string="577611025134561020198016241110256084"
#string= ""

for item in flag:
	for iter in alpha:
		if item==iter:
			string+=str(pow(ord(item),2))
		elif item==iter.lower():
			string+=str(pow(ord(item),2))
		else:
			pass
print string


