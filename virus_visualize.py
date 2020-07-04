import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecs


#filename=
name_list = ["influenza","virus_2020_kaku-ketsumaku-en","virus_2020_te-ashi-kuchi", "virus_2020 - 感染性胃腸炎（ロタウイルス）","virus_2020 - 咽頭結膜熱","virus_2020 - マイコプラズマ肺炎","virus_2020 - RSウイルス","virus_2020 - Ａ群溶血性レンサ球菌咽頭炎", "virus_2020 - 流行性角結膜炎"]

for filename in name_list:
    filename_csv = filename + ".csv"
    print(filename_csv)
    df_raw = pd.read_csv(filename_csv, header=0)

    df_raw["year"] =df_raw["Unnamed: 0"]#.str.replace("年","")
    df_raw.reset_index()
    plt.figure(figsize=(12,8))
    length_df = len(df_raw)
    for i in range(2,length_df):
        x=df_raw.columns[1:53]
        y=df_raw.iloc[i,1:53].values #df.iloc[[1,2,4],[0,2]]
        #print(x.shape)
        #print(y.shape)
        plt.plot(x,y,label=str(df_raw.iloc[i,54]))

    plt.axvline(5, ls = "--", color = "navy")
    plt.title(filename)
    plt.grid()
    plt.legend()    
    #plt.show()
    plt.savefig(filename+".png")