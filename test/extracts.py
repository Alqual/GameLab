def extract_data(ticker_symbol, start, end):
        df = pd.DataFrame()
        #データ取得
        df = web.DataReader(ticker_symbol, data_source='stooq',
                                start=start, end= end)
        #2列目に銘柄コード追加
        df.insert(0, "code", ticker_symbol, allow_duplicates=False)
        print(df)
        return df
    
    def extract_data_(filename, start, end):
        
        data_ = pd.read_csv(filename,encoding='shift_jis')
        #テスト用dataframeの作成
        df = pd.DataFrame()
        print(df.index,df.empty)
        long = len(data_.loc[:])
        
        while df.empty:
            random_nameind = np.random.randint(0,long-1)
            ticker_symbol_dr= data_.loc[random_nameind][0]+ ".US"
            #print(ticker_symbol_dr, date, date3)
            #データ取得
            df = extract_data(ticker_symbol_dr, date, date3)
            
            #画像の作成と保存
            plt.figure()
            df = df.drop(columns=["High","Low","Volume"],axis=1)
            df.plot()
            plt.savefig("./static/image/test2.jpg")
            plt.close()
            del df
            
            return True
        
        
    def extract_data_sample(sampledata, start, end):
        
        for label in sampledata:
            print(label)
            df = pd.DataFrame()
            #print(df.index,df.empty)
            #データ取得
            if extract_data(label, date, date3):
                df = extract_data(label, date, date3)
                print(df)
                #画像の作成と保存
                file = "./static/image/testsample/" + label +".jpg"
                print(file)
                plt.figure()
                df = df.drop(columns=["High","Low","Volume"],axis=1)
                df.plot()
                plt.savefig(file)
                plt.close()
            del df