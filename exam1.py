#!/usr/bin/env python
# coding: utf-8

# In[15]:


urls = [
    "http://www.google.com/a.txt",
    "http://www.google.com.tw/a.txt",
    "http://www.google.com/download/c.jpg",
    "http://www.google.co.jp/a.txt",
    "http://www.google.com/b.txt",
    "https://facebook.com/movie/b.txt",
    "http://yahoo.com/123/000/c.jpg",
    "http://gliacloud.com/haha.png",
]

Dict_ = {}

for i in urls:
    element = i.split("/")[-1]
#     print(element)
    if not element in Dict_:
        Dict_[element] = 1

    elif element in Dict_:
        Dict_[element] += 1

print(Dict_)




# In[51]:


def anonymous(x):
    return x**2 + 1
def integrate(fun, start, end):
    step = 0.1
    intercept = start
    area = 0
    while intercept < end:
        intercept += step
''' your work here '''


    return area
print(integrate(anonymous, 0, 10))


# In[10]:


import numpy as np

goal = 1000
n3 = []
n5 = []
n3_and_n5 = []

for i in range(1, goal):
    if i % 3 == 0 and i % 5 != 0:
        n3.append(i)
    elif i % 5 == 0 and i % 3 != 0:
        n5.append(i)
    elif i % 3 == 0 and i % 5 == 0:
        n3_and_n5.append(i)

N3 = np.array(n3)
N5 = np.array(n5)
N3_5 = np.array(n3_and_n5)

print("the sum of all the multiples of 3 or 5 below 1000 : ", np.sum(N3) + np.sum(N5) + np.sum(N3_5))


# In[72]:


from flask import Flask
import random


app = Flask(__name__)

@app.route("/")
def Print_str():
    sentence = [
        "Beautiful is better than ugly.",
        "Explicit is better than implicit.",
        "Simple is better than complex.",
        "Complex is better than complicated.",
        "Flat is better than nested.",
        "Sparse is better than dense.",
        "Readability counts.",
        "Special cases aren't special enough to break the rules.",
        "Although practicality beats purity.",
        "Errors should never pass silently.",
        "Unless explicitly silenced.",
        "In the face of ambiguity, refuse the temptation to guess.",
        "There should be one-- and preferably only one --obvious way to do it.",
        "Although that way may not be obvious at first unless you're Dutch.",
        "Now is better than never.",
        "Although never is often better than *right* now.",
        "If the implementation is hard to explain, it's a bad idea.",
        "If the implementation is easy to explain, it may be a good idea.",
        "Namespaces are one honking great idea -- let's do more of those!"
    ]
    idx = random.randint(0, len(sentence)-1)
    return sentence[idx]

if __name__ == "__main__":
    app.run(debug=True, port=5000)


# In[ ]:




