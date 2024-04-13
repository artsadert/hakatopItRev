import numpy as np
import scipy.spatial.distance as ds
#define arrays
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

def str_to_vecs(text, target):
    """Функция трансформирует заданные строки в вектора"""
    # в качестве токенов для векторизации выступают буквы
    vectorizer = CountVectorizer(analyzer='char')
    vectorizer = vectorizer.fit_transform([text, target])
    text_vec, target_vec = vectorizer.toarray()[0], vectorizer.toarray()[1]
    return text_vec, target_vec

def cos_sim_vecs(vec1, vec2):
    """Функция вычисляет косинусное сходство для двух заданных векторов"""
    vec1 = vec1.reshape(1, -1)
    vec2 = vec2.reshape(1, -1)   
    return cosine_similarity(vec1, vec2)[0][0]

def cosDist(text, target):
    # переменная для отслеживания максимального косинусного сходства
    score = 0
    # переменная для отслеживания положения строки похожей на искомую
    pos = 0
    # убеждаемся что текст больше искомой строки 
    try:
        assert len(text) > len(target)
    except AssertionError:
        var = text
        text = target + ' '
        target = var
    # "скользящим окном" размером с искомую строку проходим по всему тексту и вычисляем метрику
    for i in range(len(text) - len(target)):
        # векторизируем искомую строку и срез текста
        text_vec, target_vec = str_to_vecs(text[i: i + len(target)], target)
        # вычисляем косинусное сходство на данном срезе
        current_score = cos_sim_vecs(text_vec, target_vec)
        # если текущая метрика больше чем все предыдущие считаем что мы нашли похожую строку
        if current_score > score:
            score = current_score
            pos = i
    #return score, text[pos: pos + len(target)]
    return score

if __name__ == "__main__":
    a = input()
    b = input()
    print(cosDist(a, b))
