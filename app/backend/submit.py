from os import listdir
from os.path import abspath
import os

from pandas import DataFrame
import pandas as pd

from priceChecker.priceCheck import price_check

def submit(imput_folder, output_file):
    data = {"Наименование файла": [], "Наименование товара": [], "Категория продукта": [], "Цена": []}
    for file_name in listdir(os.path.abspath):
        res = price_check(abspath("./{folder}/{file_name}.jpg"), abspath("./priceChecker/rostov_prices.json"))
        data["Наименование файла"].append(file_name)
        data["Наименование товара"].append(res[1])
        df = pd.read_excel(abspath("./priceChecker/rostov_prices.json"))

        res = None
        for i in range(len(df)):
            temp_name = df.loc[i, r"Наименование товара/группы товаров"]
            value = df.loc[i, r"Ед. изм."]
            if value is None:
                res = temp_name
            if res[1] == temp_name:
                break
        data["Категория продукта"] = res
        data["Цена"].append(res[4])
    df = DataFrame(data)
    df.to_csv(output_file)

if __name__ == "__main__":
    folder = input()
    output = input()
    submit(folder, output)
