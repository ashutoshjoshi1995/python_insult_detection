from nltk.tokenize import TweetTokenizer
tknzr = TweetTokenizer(strip_handles=True, reduce_len=True)
s1 = '@remy: This is waaaaayyyy too much for bitch you!!!!!!'
x=tknzr.tokenize(s1)
x=s1.split()
s0='ashu'
print("String Entered\n",s1,"\n")
f = open('words.txt')
print("Matched Words:")

for y in x:	
	#print(y)
	for line in open('words.txt'):
		if y==line.strip():
			print(y)