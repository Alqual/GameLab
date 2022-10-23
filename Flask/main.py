from flask import Flask, render_template, request
import os
import datetime as dt
import pandas_datareader.data as web
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import extracts as ex
 
app = Flask(__name__)


#Home画面の作成
@app.route("/")
async def hello():
    
    
    #日付をランダムに設定
    m= np.random.randint(1,12)
    d = np.random.randint(1,31)
    y = np.random.randint(2010,2020)
    date = '{0}-{1:02d}-{2:02d}'.format(y, m, d)
    print(date)
    date2 = dt.datetime.strptime(date, '%Y-%m-%d')
    date3 = date2+dt.timedelta(days=np.random.randint(90,365))
    
    #株式リストの読み込み
    filename = "./static/data/Stock_list.csv"
    #sampledata = #["ZW.F","ZC.F","GC.F","QC.F","WTI.US","NG.F",  #資源先物
    sampledata = ["NDAQ.US","^DJI", 
    "GOOGL.US","AMZN.US","AAPL.US","TM.US"] #代表産業株#アメリカ総合株
    
    
    
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, ex.extract_data_, filename, date, date3)
    await loop.run_in_executor(None, ex.extract_data_sample, sampledata, date, date3)
    
    return render_template("Start.html")



# テストページへの移行
@app.route('/Challenge', methods=['POST'])
def Challenge():
    # もしPOSTメソッドならresult.htmlに値textと一緒に飛ばす
    if request.method == 'POST':
        return render_template('Challenge.html')

#解答ページへの移行
@app.route('/Answer', methods=['POST'])
def Answer():
    # もしPOSTメソッドならresult.htmlに値textと一緒に飛ばす
    if request.method == 'POST':
        return render_template('Answer.html')  

    
#解答ページへの移行
@app.route('/Back', methods=['POST'])
def Back():
    # もしPOSTメソッドならresult.htmlに値textと一緒に飛ばす
    if request.method == 'POST':
        #日付をランダムに設定
        m= np.random.randint(1,12)
        d = np.random.randint(1,31)
        y = np.random.randint(2010,2020)
        date = '{0}-{1:02d}-{2:02d}'.format(y, m, d)
        print(date)
        date2 = dt.datetime.strptime(date, '%Y-%m-%d')
        date3 = date2+dt.timedelta(days=np.random.randint(90,365))
        #株式リストの読み込み
        df0 = pd.read_csv("./static/data/Stock_list.csv", encoding='shift_jis')
        long = len(df0.loc[:])
        #テスト用dataframeの作成
        df = pd.DataFrame()
        print(df.index,df.empty)
        while df.empty:  #対象期間中にデータが存在するまでランダムに株式を探索
            random_nameind = np.random.randint(0,long-1)
            ticker_symbol_dr= df0.loc[random_nameind][0]+ ".US"
            #print(ticker_symbol_dr, date, date3)
            #データ取得
            df = web.DataReader(ticker_symbol_dr, data_source='stooq',
                                start=date,end=date3)
            #2列目に銘柄コード追加
            df.insert(0, "code", ticker_symbol_dr, allow_duplicates=False)
            #print(df)
        #画像の作成と保存
        plt.figure()
        df = df.drop(columns=["High","Low","Volume"],axis=1)
        df.plot()
        plt.savefig("./static/image/test2.jpg")
        plt.close()
        #csv保存
        #df.to_csv('sample2.csv')
      
        return render_template('Start.html')  



if __name__ == "__main__":
    # webサーバー立ち上げ
    app.run()