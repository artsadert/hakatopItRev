from os import listdir
from os.path import abspath
import os

from pandas import DataFrame
import pandas as pd

from priceChecker.priceCheck import price_check

def submit(input_folder, output_file):
    data = {"Наименование файла": [], "Наименование товара": [], "Категория продукта": [], "Цена": []}
    dataset_dir = os.path.abspath(f"./{input_folder}")
    
    for file_name in listdir(dataset_dir):
        print(file_name)
        
        res = price_check(abspath(f"./{input_folder}/{file_name}"), abspath("./priceChecker/rostov_prices.json"))
        data["Наименование файла"].append(file_name)
        data["Наименование товара"].append(res[1])
        df = pd.read_excel(abspath("./priceChecker/prices.xlsx"))

        res_temp = None
        for i in range(len(df)):
            temp_name = df.loc[i, r"Наименование товара/группы товаров"]
            value = df.loc[i, r"Ед. изм."]
            if value is None:
                res_temp = temp_name
            if res[1] == temp_name:
                break
        data["Категория продукта"] = res_temp
        data["Цена"].append(res[4])
        print(data)
        df = DataFrame(data)
        df.to_csv(output_file)

if __name__ == "__main__":
    folder = input()
    output = input()
    submit(folder, output)

