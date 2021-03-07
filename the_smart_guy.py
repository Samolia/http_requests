import requests

def get_intelligence(TOKEN, names):
    '''
    Функция получает данные из get-запроса для выбранных персонажей. Записывает значение интеллекта в словарь.
    :param names: Имена персонажей.
    :param url: Адрес для доступа к API по информации о супергероях.
    :return: Словарь, где ключи - имена персонажей, значения - уровень их интеллекта.
    '''
    hero_intelligence = {}
    for name in names:
        url = f'https://superheroapi.com/api/{TOKEN}/search/{name}'
        response = requests.get(url)
        data = response.json()['results']
        hero_intelligence[name] = int(data[0]['powerstats']['intelligence'])
    return hero_intelligence

def show_the_smart_guy(hero_intelligence):
    '''
    Функция показывает умника.
    '''
    max_value = max(hero_intelligence.values())
    the_smart_guy = {key: value for key, value in hero_intelligence.items() if value == max_value}
    for key, velye in the_smart_guy.items():
        return f'Самый умный чувак - "{key}". Его интеллект - "{velye}".\n'