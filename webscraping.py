# TODO: Try not to use import *
# https://stackoverflow.com/questions/2386714/why-is-import-bad
from newspaper import *
from string import Template
import webbrowser
from nltk import *

# TODO: Separate functions for separate tasks
# TODO: fetch_article() - should take url and return class object containing members (title, text, summary, keywords)
url1 = "https://www.thehindu.com/sci-tech/health/coronavirus-why-21-day-lockdown-period/article31167442.ece?homepage=true"
hindu_article1 = Article(url1,languages="en")
hindu_article1.download()
hindu_article1.parse()
hindu_article1.nlp()
# TODO: Better naming
a=hindu_article1.title
b=hindu_article1.text
c=hindu_article1.summary
d=hindu_article1.keywords

# TODO: write_to_html() - should take the class object and add it to the webpage
# TODO: Use 'with' statment open file, study about with keyword in python
f = open("webpage.html",'w')
message = '''\
<html>
<head></head>
<body><h1><center>$a<center></h1>
<p style="color:blue;">$b<center></center></p>
</body>
</html>
 '''
# TODO: The webpage does not look user friendly
s = Template(message).safe_substitute(a=hindu_article1.title)
s1 = Template(message).safe_substitute(b=hindu_article1.text)
f.write(s)
f.write(s1)
f.close()























# print("Title:")
# print(hindu_article1.title)
# print("n")
#
# print("Text:")
# print(hindu_article1.text)
# print("\n")
#
# print("Article's Summary:")
# print(hindu_article1.summary)
# print("\n")
#
# print("Article's Keywords:")
# print(hindu_article1.keywords)
