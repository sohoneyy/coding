#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas_datareader.data as web  #from pandas_datareader.data import * as web으로 쓰면 안 되는 거지?
import datetime
start = datetime.datetime(2016, 2, 19)  #from a import *로 쓰면 그냥 datetime()만 쓰면 되지만, import로 불렀기 때문에 클래스명.함수()라고 씀
end = datetime.datetime(2016, 3, 4)

gs = web.DataReader("078930.KS", "yahoo")

gs.info()

import matplotlib.pyplot as plt
plt.plot(gs['Adj Close'])  #plt(클래스명).plot(함수), gs데이터의 [Adj Close] 인덱스
plt.show()


# In[22]:


import pandas as pd
import pandas_datareader.data as web
gs = web.DataReader("078930.KS", "yahoo", "2014-01-01", "2016-03-06")

ma5 = gs['Adj Close'].rolling(window=5).mean()
gs.insert(len(gs.columns), 'MA5', ma5)  #맨 뒤에 넣겠다는 뜻같음

ma20 = gs['Adj Close'].rolling(window=20).mean()
gs.insert(len(gs.columns), 'MA20', ma20)

ma60 = gs['Adj Close'].rolling(window=60).mean()
gs.insert(len(gs.columns), 'MA60', ma60)

gs.tail(10)


# In[29]:


import matplotlib.pyplot as plt

plt.plot(gs.index, gs['Adj Close'], label='Adj Close')  #Q.gs.index가 왜 들어가지? 앞에서는 안 들어갔는데? 빼도 되던데?. 아 혹시 새로운 창에서 저 데이터를 이끌어 쓰려고?
plt.plot(gs.index, gs['MA5'], label='MA5')
plt.plot(gs.index, gs['MA20'], label='MA20')
plt.plot(gs.index, gs['MA60'], label='MA60')  #MA5 ~ MA60이라는 값은 윗 칸에 있는데, 값이 이어지나?

plt.legend(loc='best')
plt.grid()
plt.show()


# In[32]:


import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

gs = web.DataReader("078930.KS", "yahoo", "2014-01-01", "2016-03-06")

ma5 = gs['Adj Close'].rolling(window=5).mean()
ma20 = gs['Adj Close'].rolling(window=20).mean()
ma60 = gs['Adj Close'].rolling(window=60).mean()
ma120 = gs['Adj Close'].rolling(window=120).mean()

gs.insert(len(gs.columns), 'MA5', ma5)
gs.insert(len(gs.columns), 'MA20', ma20)
gs.insert(len(gs.columns), 'MA60', ma60)
gs.insert(len(gs.columns), 'MA120', ma120)

plt.plot(gs.index, gs['Adj Close'], label='Adj Close')
plt.plot(gs.index, gs['MA5'], label='MA5')
plt.plot(gs.index, gs['MA20'], label='MA20')
plt.plot(gs.index, gs['MA60'], label='MA60')
plt.plot(gs.index, gs['MA120'], label='MA120')

plt.legent(loc="best")
plt.grid()
plt.show()

