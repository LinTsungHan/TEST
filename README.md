#TEST Q.

----
## Part 1
**1. Counting**
> Given a list of urls, print out the top 3 frequent filenames.


ex.
Given
 urls = [
"http://www.google.com/a.txt",
"http://www.google.com.tw/a.txt",
"http://www.google.com/download/c.jpg",
"http://www.google.co.jp/a.txt",
"http://www.google.com/b.txt",
"https://facebook.com/movie/b.txt",
"http://yahoo.com/123/000/c.jpg",
"http://gliacloud.com/haha.png",]



 The program should print out

 a.txt 3

 b.txt 2

 c.jpg 2



**2. **

![image](https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Integral_approximations-3-steps.png/320px-Integral_approximations-3-steps.png
)

> Please try to add 1~3 line of code to finish the integration



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

**3.Multiples of 3 and 5.**

> If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
• Find the sum of all the multiples of 3 or 5 below 1000.



----
## Part 2
> 請以下題目擇一


1.  a) 請用 Python 寫出一個可以爬 ptt /reddit 任意看板(https://www.ptt.cc )的爬蟲
程式,可以使用任意 Python 套件
以下欄位為必要

  • 日期


  • 作者


  • 標題


  • 內文


  • 看板名稱

2. b) 請用 python 寫出一個簡單的網頁,只需要一個頁面 每次瀏覽時隨機出現 thezen of python 其中一條

 [網址](http://wiki.python.org.tw/The%20Zen%20Of%20Python)
