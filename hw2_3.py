# coding: utf-8
import json
from pprint import pprint
import chardet

def json_to_list(file_name):
    with open(file_name) as news:
        messages = json.load(news)
        news_list = []
        for message in messages['rss']['channel']['items']:
            text = message['description']
            for i in text.split(' '):
                if len(i) > 6:
                    news_list.append(i.lower())
        return news_list

def show_top_words_json():
    name = input('Введите имя файла:')
    list_of_news = json_to_list(name)
    dict_of_words = dict((word, list_of_news.count(word)) for word in list_of_news)
    sorted_words = sorted(dict_of_words.items(), key=lambda x: x[1], reverse=True)
    return sorted_words

long_words = show_top_words_json()
for word in long_words[0:9]:
                print('{}: {}'.format(word[0], word[1]))
