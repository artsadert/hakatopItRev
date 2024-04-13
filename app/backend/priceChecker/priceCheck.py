from cv_data import get_data
from cosine_similiarity import cos_check
import json
from price import get_price
import re
import os

def price_check(img_path):
    cv_data = get_data(img_path)
    try:
        name = cv_data[1][0]
    except KeyError:
        return None
    name = re.sub(r"[^\sа-яА-ЯёЁ0-9]", "", name).replace('ООО ЮГ ТЕХ ЛОГИСТИКА', '').strip().replace('О', '0').replace('ЮГ ТЕХ ЛОГИСТИКА', '')
    pattern = r"\d{1,4}[лг]"
    matches = re.findall(pattern, name)
    count = " ".join(matches)
    name = re.sub(pattern, "", name)
    name = re.sub('r"(\d{3,})"', '', name)
    

    
    #загрузка json файла
    with open("rostov_prices.json", "r") as json_file:
        data = json.load(json_file)
    
    #базовые переменные
    best_coincidence = 0
    max = 0.3
    soc_price_naming = 0
    max_soc = 0.9
    
    #наименование товара
    for product in data:
        product_name = product["Наименование товара/группы товаров"]
        if cos_check(product_name, name)[0] > max:
            max = cos_check(product_name, name)[0]
            best_coincidence = product_name
        if cos_check("социальная цена", name)[0] > max_soc:
            soc_price_naming = 1

    #цена товара
    try:
        real_price = int(list(get_price(img_path))[0][0])
    except IndexError:
        real_price = None
   


    return name, best_coincidence, count, soc_price_naming, real_price

if __name__ == "__main__":
    print(price_check(os.path.abspath("../test.jpg")))
