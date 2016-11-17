from lxml import html
#from nltk.stem.lancaster import LancasterStemmer
#from nltk.stem import RegexpStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import TweetTokenizer
tknzr = TweetTokenizer(strip_handles=True, reduce_len=True)
import requests
#st = RegexpStemmer('ing$|s$|e$|able$', min=4)
wnl = WordNetLemmatizer()
page = requests.get('http://www.loveisrespect.org/is-this-abuse/types-of-abuse/')
tree = html.fromstring(page.content)
for p in range(1,20):
        str1 = '//*[@id="tab-id-1-container"]/div/ul[1]/li[' + str(p) + ']/text()'
        comments = tree.xpath(str1)
        #print(comments)
        #s1 = '@remy: This is waaaaayyyy too much for bitch you!!!!!!'
        s1 = ''.join(comments)
        x=tknzr.tokenize(s1)
        #x=s1.split()
        s0='ashu'
        print("String Entered:",s1)
        f = open('words.txt')
        print("Matched Words:")
        for y in x:
                #print(st.stem(y))
                print(wnl.lemmatize(y))
                #print(y)
                for line in open('words.txt'):
                        if y==line.strip():
                                print(y)
        print('\n')
        #print(page.content)



    


			
