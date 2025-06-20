import pandas as pd 
import re ,random
from nltk.corpus import stopwords 
from sklearn.model_selection  import train_test_split 
from sklearn.feature_extraction.text import CountVectorizer , TfidfVectorizer 



STOPWORDS = stopwords.words('english')


def clean_text(text):
	text = text.lower()
	text = re.sub("[^\w\s]"," ",text)
	text =  ' '.join([w for w in text.split() if w not in STOPWORDS])
	return text



class DATA:

	def __init__(self):
		self.data = pd.read_csv("amazon_alexa.tsv",sep='\t')
		self.data = self.data.dropna()
		self.data = self.data.drop(columns=['date','variation','rating'])
		self.data['text'] =  self.data['verified_reviews'].apply(clean_text)
		self.cv = CountVectorizer()
		self.tf = TfidfVectorizer()


	def sample(self):
		sp = random.randint(1,self.data.shape[0])
		return " ORIGINAL : {}\n TARGET : {}\n CLEANED : {}".format(self.data.iat[sp,0],self.data.iat[sp,1],self.data.iat[sp,2])

	def load(self,transform='cv',test_size=0.2,return_type='raw',y_type='ft'):

		trans = None
		if transform == "cv":
			trans = self.cv
			trans_text = 'CountVectorizer'

		if transform == "tf":
			trans = self.tf
			trans_text = 'TfidfVectorizer'


		if y_type == "ft":
			y = self.data['feedback']
			y = y.astype("str").map({"1":"positive","0":"negative"})
		else:
			y = self.data['feedback']  # set 'new'






		

		#https://stackoverflow.com/questions/54491953/can-i-use-countvectorizer-on-both-test-and-train-data-at-the-same-time-or-do-i-n
		# first split then vectorization else it might lead to data leakage 

		x_train , x_test,y_train,y_test = train_test_split(self.data['text'],y,test_size=test_size,random_state=42,stratify=y)

		print("data splitted ")


		trans.fit(x_train)
		x_train_ = trans.transform(x_train)
		x_train_ = x_train_.toarray()



		x_test_ = trans.transform(x_test)
		x_test_ = x_test_.toarray()

		if return_type =='raw':
			return (x_train,x_test,y_train,y_test)
		else:
			print(f"USING {trans_text}")   # set 'new'
			return (x_train_,x_test_,y_train,y_test)











# data = DATA()
# print(data.load(return_type='new'))








