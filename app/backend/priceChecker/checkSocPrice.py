import pandas as pd

from os.path import abspath


def checkSocPrice(name):
    df = pd.read_excel(abspath("./priceChecker/prices.xlsx"))

    for i in range(len(df)):
        temp_name = df.loc[i, r"Наименование товара/группы товаров"]
       # print(temp_name, name)
        if name == temp_name:
            #print("finded")
            return (df.loc[i, "Цена региона-аналога (Ростова-на-Дону)"], df.loc[i, "Ед. изм."])
        