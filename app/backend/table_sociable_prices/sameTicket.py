import pandas as pd
import numpy as np

from cosDist import cosDist


class ReaderXlsx:
    def __init__(self):
        self.df = pd.read_excel("./prices.xlsx")

    def search(self, a: str):
        res_likes = 1
        res_name = None
        res_price = None
        res_value = None
        for i in range(len(self.df)):
            #print(x)
            name = self.df.loc[i, 'Наименование товара/группы товаров']
            value = self.df.loc[i, 'Ед. изм.']
            if value is np.NaN:
                continue
            price = self.df.loc[i, 'Цена региона-аналога (Ростова-на-Дону)']
            temp_dist = cosDist(a.lower(), name.lower())
            print(temp_dist, res_likes)
            if temp_dist < res_likes:
                res_likes = temp_dist
                res_name = name
                res_price = price
                res_value = value
            
        print(res_likes, res_name, res_price, res_value)
if __name__ == "__main__":
    a = ReaderXlsx()
    #for i, x in a.df.iterrows:
    #    print(x)
    a.search(input())
    #print(a.df['Наименование товара/группы товаров'])

