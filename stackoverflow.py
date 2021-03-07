import requests
import time
import datetime



def get_questions(tag, days, site='stackoverflow'):
    '''
    Получает вопросы со stackoverflow с тэгом 'tag' за прошедшие 'n' дней
    '''
    now = int(time.time())
    seconds_per_day = 86400
    start_find = now - (days * seconds_per_day)

    url = 'https://api.stackexchange.com/2.2/questions'

    params = {'fromdate': start_find,
              'todate': now,
              'site': site,
              'tagged': tag,
              'page': 1,
              'pagesize': 100,
              }

    list_of_questions = []

    while True:
        response = requests.get(url, params=params)
        if not response.json().get('items'):
            break # если вопросов на странице нет
        else:
            for questions in response.json().get('items'):
                # date = time.ctime(questions.get('creation_date'))
                date = time.strftime('%D %H:%M:%S', time.localtime(questions.get('creation_date'))) # дата вопроса в читабельном виде
                # date = datetime.datetime.fromtimestamp(questions.get('creation_date')).strftime('%Y-%m-%d %H:%M:%S')
                questions_on_page = {'date': date,
                                     'link': questions.get('link'),
                                     'title': questions.get('title'),
                                     'tags': questions.get('tags'),
                                     } # получаю словарь с датой вопроса, ссылкой, заголовком и тэгом вопроса
                list_of_questions.append(questions_on_page) # добавляю информацию о вопросе в список
        params['page'] += 1
    print(f'Всего вопросов с тэгом "{tag}" за {days} дня - {len(list_of_questions)}')
    return list_of_questions