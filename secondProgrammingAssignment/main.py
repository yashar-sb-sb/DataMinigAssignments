try: #Python3
    import urllib.request as urllib
except:
    import urllib

import html2text
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer().fit_transform([html2text.html2text(urllib.urlopen(input()).read().decode('utf-8')),html2text.html2text(urllib.urlopen(input()).read().decode('utf-8'))])
print((tfidf * tfidf.T).A[1,0])
