#!/usr/bin/env python
# coding: utf-8

# In[8]:


class CpStockCode:
    def __init__(self):
        self.stocks = {'유한양행' : 'A000100'}
    def GetCount(self):
        return len(self.stocks)
    def NameToCode(self, name):
        return self.stocks[name]


# In[9]:


instCpStockCode = CpStockCode()
print(instCpStockCode.GetCount())
print(instCpStockCode.NameToCode('유한양행'))


# In[11]:


import win32com.client

explore = win32com.client.Dispatch("InternetExplorer.Application")
explore.Visible = True


# In[13]:


import win32com.client
word = win32com.client.Dispatch("Word.Application")
word.Visible = True


# In[16]:


import win32com.client

excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True
wb = excel.Workbooks.Add()
ws = wb.Worksheets("Sheet1")
ws.Cells(1, 1).Value = "hello world"
wb.SaveAs('c:\\Python\\test.xlsx')
excel.Quit()


# In[22]:


import win32com.client
excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True
wb = excel.Workbooks.Open('C:\\Users\\user\\Desktop\\input.xlsx')
ws = wb.ActiveSheet
print(ws.Cells(1,1).Value)
excel.Quit()


# In[39]:


import win32com.client

excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True
wb = excel.Workbooks.Open('C:\\Users\\user\\Desktop\\input.xlsx')
ws = wb.ActiveSheet

ws.Cells(1,2).Value = 'is'
ws.Range('C1').Value = 'good'
ws.Range('C1').Interior.ColorIndex = 10

