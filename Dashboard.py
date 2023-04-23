import requests
from tkinter import *
import io
import tkinter as tk
import pandas as pd
import json
import subprocess 
# from PIL import ImageTk, Image

# Global Variables:
region = ""
symbol = ""
txt1=Entry()
txt2=Entry()
data = {}

# REDIRECT TO DASHBOARD REPORT:
def redirect():
    subprocess.run(['C:/Program Files/Microsoft Power BI Desktop/bin/PBIDesktop.exe', 'C:/Users/HP/OneDrive/Desktop/Hackathon/get_qotes.pbix'])

def dummy():
    pass

# CUSTOMIZED API REQUEST:
def request_():
    global region, symbol, txt1, txt2
    region = txt1.get()
    symbol = txt2.get()
    # url = "https://yh-finance.p.rapidapi.com/market/v2/get-quotes"
    # querystring = {"region":f"{region}","symbols":f"{symbol}"}
    # headers = {
    #     "X-RapidAPI-Key": "4efcd7b4d0msha6cd1e712b7e810p187e1cjsna5a77428ecba",
    #     "X-RapidAPI-Host": "yh-finance.p.rapidapi.com"
    #     }
    # data = requests.request("GET", url, headers=headers, params=querystring).json()
     
    # df = pd.DataFrame()
    # #Extracting the columns & populating:
    # x = data["quoteResponse"]["result"]
    # count = 0
    # for i in x:
    #         # x[count] = i["regularMarketDayHigh","regularMarketDayLow","shortName","bidSize","bookValue","floatShares","ebitda","targetPricemean","totalCash","fiftyTwoWeekHighChangePercent","priceToBook","quoteSummary"]
    #         x[count] = i["shortName"]
    #         if count == 0: # Instantiating the dataframe
    #             y = data["quoteResponse"]["result"][j]
    #             for i in y:
    #                 df[str(i)] = [y[i]]
    #         else: # Populating it further
    #             pd.concat([df,i],axis=1)
    #         count = count + 1
    # print(df)
    # df.to_csv('quotesquotes.csv', index=False)
    print("#####################")
    # print(x)
    # print("Succesfull")
    redirect()

# Main Navigation Menu GUI:
mmenu = Tk()
mmenu.geometry('600x600')
mmenu.resizable(0,0)
mmenu.title('One Stop Analytics Solution')
mmenu.configure(background='white')

def market():
    global region, symbol, txt1, txt2
    market = Toplevel(mmenu)
    market.geometry('600x800')
    market.title("MARKET")
    mrkt_heading = Label(market,text="MARKET",font=("Arial",60))
    mrkt_heading.grid(row=0,column=0)
    def quote():
        global region, symbol, txt1, txt2
        quote = Toplevel(market)
        quote.geometry('2160x1080')
        quote.title("QUOTE")
        lbl1 = Label(quote, text="Region").grid(row=0,column=0)
        lbl2 = Label(quote, text="Symbols").grid(row=1,column=0)
        txt1 = Entry(quote,font=("Arial",50))
        txt1.grid(row=0,column=1)
        txt2 = Entry(quote,font=("Arial",50))
        txt2.grid(row=1,column=1)

        request = Button(quote,text="Update The CSV",command=request_,font=("Arial",40))
        request.grid(row=6,column=1)
        ################# DASHBOARD SCREENSHOT#################
        # frame = Frame(quote, width=600, height=400)
        # frame.pack()
        # frame.place(anchor='center', relx=0.5, rely=0.5)
        # img = PhotoImage(Image.open("dashboard.png"))

    qt = Button(market,text="QUOTE",font=("Arial",35),command=quote)
    qt.grid(row=2,column=0)
##########################################################

mrkt = Button(mmenu, text="Market", font = ("Arial",30), command = market, foreground="red")
mrkt.grid(row=0,column=0)

stck = Button(mmenu, text="Stock", font = ("Arial",30), command = dummy, foreground="red")
stck.grid(row=0,column=1)

screener = Button(mmenu, text="Screener", font = ("Arial",30), command = dummy, foreground="red")
screener.grid(row=1,column=0)

news = Button(mmenu,text="NEWS", font = ("Arial",30),command = dummy)
news.grid(row=1,column=1)

mmenu.mainloop()
