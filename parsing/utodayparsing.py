import requests
from bs4 import BeautifulSoup
import json
import time
from translate import Translator
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



def get_first_list_news():

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.100',
        'accept-language': 'ru,en;q=0.9,ru-RU;q=0.8,en-US;q=0.7',
        'cookie': '_ga=GA1.2.1467385129.1663848546; _gid=GA1.2.1639641072.1663848546; __auc=5f7a70a4183651a01392c1ba394; __gads=ID=067fa46110d5b100-2201fa432bce0077:T=1663848573:RT=1663848573:S=ALNI_MYbWzYA26NGoFaadlpOSfFJ_2_Fvg; __asc=9117c77b183699c504c5267b426; __gpi=UID=00000b493606985f:T=1663848573:RT=1663925285:S=ALNI_MY7j2TK3EEmSkd_09WPhRqw-cWdJQ; FCNEC=%5B%5B%22AKsRol_SQR2nkx9rkd0eQi7uR-842iy1XxKUBoXEvhUanVMvLPfkSuoEhRMWJY7xtJxmJYbLwZAcYpkX3ULGCAv5HJy5RBHYuR-c_2hwkCsj4-ISNnwjJSGBF_Ko_O0xcZ0lfctgK7pR5dNcP3kA4kah0KAHdCv6lA%3D%3D%22%5D%2Cnull%2C%5B%5D%5D'
    }

    url = 'https://u.today/latest-cryptocurrency-news'

    r = requests.get(url = url , headers = headers)

    soup = BeautifulSoup(r.text , 'lxml')


    # Получение первой инфы : Заголовок , ссылку на полную статью

    all_cards = soup.find('main' , class_= 'main-block').find_all('div' , class_='category-item')
    

    # Цикл , перебираю карточки        
    info_dict = {}
    for card in all_cards : 
        
        # Фильтр только на ФРС и SEC 

        card_title_splited = card.find('a' ,class_='category-item__title-link').find('div',class_='category-item__title').text.replace(':' , ' ').replace(',' , ' ' ).split(' ')
        
        
        if 'FED' in card_title_splited  or 'Fed' in card_title_splited  or 'fed' in card_title_splited  or 'SEC' in card_title_splited  or 'Sec' in card_title_splited  or 'sec' in card_title_splited  :
            
            card_href = card.find('a' , class_='category-item__title-link').get('href')
            
            
            # Подключаюсь и забираю инфу со статьи
            request_card = requests.get(url = card_href, headers = headers)
            soup = BeautifulSoup(request_card.text, 'lxml')
            
            card_header = soup.find('div', class_='views-row').find('div', class_='article').find('h1', class_='article__title').text.strip()
            
            card_text = soup.find('div' , class_='article__content').find_all('p')
            
            
            # Собираю части текста в целое
            text_list = []
            for p in card_text:
                text_list.append(p.text.strip())

            all_text = ','.join(text_list)

            info_dict[card_href] = (
                {
                    'Title': card_header,
                    'Text': all_text,
                    'Source': card_href
                }
            )

            with open(r'D:\Codes Python\Project\parsing\parsutoday\utoday_info.json' , 'w' , encoding='utf-8') as file:
                json.dump(info_dict, file , indent=4 , ensure_ascii=False)
        
        else:
            continue
    





def get_new_info():
    with open(r'D:\Codes Python\Project\parsing\parsutoday\utoday_info.json', 'r' , encoding='utf-8') as file:
        json_card_list = json.load(file)

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.100',
        'accept-language': 'ru,en;q=0.9,ru-RU;q=0.8,en-US;q=0.7',
        'cookie': '_ga=GA1.2.1467385129.1663848546; _gid=GA1.2.1639641072.1663848546; __auc=5f7a70a4183651a01392c1ba394; __gads=ID=067fa46110d5b100-2201fa432bce0077:T=1663848573:RT=1663848573:S=ALNI_MYbWzYA26NGoFaadlpOSfFJ_2_Fvg; __asc=9117c77b183699c504c5267b426; __gpi=UID=00000b493606985f:T=1663848573:RT=1663925285:S=ALNI_MY7j2TK3EEmSkd_09WPhRqw-cWdJQ; FCNEC=%5B%5B%22AKsRol_SQR2nkx9rkd0eQi7uR-842iy1XxKUBoXEvhUanVMvLPfkSuoEhRMWJY7xtJxmJYbLwZAcYpkX3ULGCAv5HJy5RBHYuR-c_2hwkCsj4-ISNnwjJSGBF_Ko_O0xcZ0lfctgK7pR5dNcP3kA4kah0KAHdCv6lA%3D%3D%22%5D%2Cnull%2C%5B%5D%5D'
    }


    url = 'https://u.today/latest-cryptocurrency-news'

    r = requests.get(url = url , headers = headers)

    soup = BeautifulSoup(r.text , 'lxml')

    # Получение первой инфы : Заголовок , ссылку на полную статью


    all_cards = soup.find('main' , class_= 'main-block').find_all('div' , class_='category-item')
    

    # Цикл , перебираю карточки        
    
    new_dict = {}
    translated_info = None
    for card in all_cards : 
        
        try:
            # Фильтр только на ФРС и SEC 

            card_title_splited = card.find('a' ,class_='category-item__title-link').find('div',class_='category-item__title').text.replace(':' , ' ').replace(',' , ' ' ).split(' ')
            
            
            if 'FED' in card_title_splited  or 'Fed' in card_title_splited  or 'fed' in card_title_splited  or 'SEC' in card_title_splited  or 'Sec' in card_title_splited  or 'sec' in card_title_splited  :
                card_href = card.find('a' , class_='category-item__title-link').get('href')

                if card_href in json_card_list:
                    continue

                else:
                    
                    service = Service(r'D:\Codes Python\Project\parsing\chromedriver.exe')
                    options = webdriver.ChromeOptions()
                    options.add_argument('--disable-blink-features=AutomationControlled')
                    options.add_argument('--no-sandbox')

                    options.headless = True
                    
    
                    driver = webdriver.Chrome(service=service, options=options)



                    # Подключаюсь и забираю инфу со статьи
                    request_card = requests.get(url = card_href, headers = headers)
                    soup = BeautifulSoup(request_card.text, 'lxml')
                    
                    card_header = soup.find('div', class_='views-row').find('div', class_='article').find('h1', class_='article__title').text.strip()
                    
                    card_text = soup.find('div' , class_='article__content').find_all('p')
                    
                    
                    # Собираю части текста в целое
                    text_list = []
                    for p in card_text:
                        text_list.append(p.text.strip())

                    a = text_list[1:len(text_list)]

                    paragraf = text_list[0]
                    paragraf2 = text_list[1]
                    paragraf3 = text_list[2]
                    paragraf4 = text_list[3]
                    paragraf5 = text_list[4]

                    card_text_not_list = ' '.join(a)

                    all_paragraf = f'• {paragraf}\n\n• {paragraf2}\n\n• {paragraf3}\n\n• {paragraf4}\n\n'

                    

                    json_card_list[card_href] = (
                        {
                            'Title': card_header,
                            'Text': card_text_not_list,
                            'Source': card_href
                        }
                    )
                    
                    new_dict[card_href] = (
                        {
                            'Title': card_header,
                            'Text': text_list,
                            'Source': card_href
                        }
                    )
                    
                    
                    #Исходник на английском
                    open_new_dict = new_dict[card_href]
                    news = f'{open_new_dict["Title"]}\n\n' \
                        f'{all_paragraf}' \
                        f'Translated from English\n\n' \
                        f'{open_new_dict["Source"]}\n\n'  
                    
                     
                    ready_news = str(news)

                    #================================================================
                    # Перевод
                    
                    try:
                        driver.implicitly_wait(20)
                        driver.get('https://yandex.ru/search/?text=%D0%BF%D0%B5%D1%80%D0%B5%D0%B2%D0%BE%D0%B4&search_source=dzen_desktop_safe&lr=68')
                        time.sleep(5)
                        
                        send_title = driver.find_element(by=By.XPATH ,value='/html/body/main/div[2]/div[2]/div[1]/div[1]/ul/li[1]/div/div/div/div/div[3]/div[3]/form/span/span/textarea').send_keys(open_new_dict["Title"])
                        time.sleep(5)

                        take_translated_title = driver.find_element(by=By.XPATH, value ='/html/body/main/div[2]/div[2]/div[1]/div[1]/ul/li[1]/div/div/div/div/div[4]/div[1]/div[2]').text
                        time.sleep(5)

                        clear_text = driver.find_element(by=By.XPATH , value= '/html/body/main/div[2]/div[2]/div[1]/div[1]/ul/li[1]/div/div/div/div/div[3]/div[1]').click()
                        time.sleep(2)
                        
                        # 1-й параграф
                        send_text_1 = driver.find_element(by=By.XPATH ,value='/html/body/main/div[2]/div[2]/div[1]/div[1]/ul/li[1]/div/div/div/div/div[3]/div[3]/form/span/span/textarea').send_keys(paragraf)
                        time.sleep(3)
                        
                        take_translated_text_1p = driver.find_element(by=By.XPATH, value ='/html/body/main/div[2]/div[2]/div[1]/div[1]/ul/li[1]/div/div/div/div/div[4]/div[1]/div[2]').text
                        
                        clear_text_1 = driver.find_element(by=By.XPATH , value= '/html/body/main/div[2]/div[2]/div[1]/div[1]/ul/li[1]/div/div/div/div/div[3]/div[1]').click()

                        
                        
                        # 2-й параграф
                        send_text_2 = driver.find_element(by=By.XPATH ,value='/html/body/main/div[2]/div[2]/div[1]/div[1]/ul/li[1]/div/div/div/div/div[3]/div[3]/form/span/span/textarea').send_keys(paragraf2)
                        time.sleep(3)
                        
                        take_translated_text_2p = driver.find_element(by=By.XPATH, value ='/html/body/main/div[2]/div[2]/div[1]/div[1]/ul/li[1]/div/div/div/div/div[4]/div[1]/div[2]').text
                        
                        clear_text_2 = driver.find_element(by=By.XPATH , value= '/html/body/main/div[2]/div[2]/div[1]/div[1]/ul/li[1]/div/div/div/div/div[3]/div[1]').click()

                        

                        # 3-й параграф
                        send_text_3 = driver.find_element(by=By.XPATH ,value='/html/body/main/div[2]/div[2]/div[1]/div[1]/ul/li[1]/div/div/div/div/div[3]/div[3]/form/span/span/textarea').send_keys(paragraf3)
                        time.sleep(3)
                        
                        take_translated_text_3p = driver.find_element(by=By.XPATH, value ='/html/body/main/div[2]/div[2]/div[1]/div[1]/ul/li[1]/div/div/div/div/div[4]/div[1]/div[2]').text
                        
                        clear_text_3 = driver.find_element(by=By.XPATH , value= '/html/body/main/div[2]/div[2]/div[1]/div[1]/ul/li[1]/div/div/div/div/div[3]/div[1]').click()

                        
                        
                        # 4-й параграф
                        send_text_4 = driver.find_element(by=By.XPATH ,value='/html/body/main/div[2]/div[2]/div[1]/div[1]/ul/li[1]/div/div/div/div/div[3]/div[3]/form/span/span/textarea').send_keys(paragraf4)
                        time.sleep(3)
                        
                        take_translated_text_4p = driver.find_element(by=By.XPATH, value ='/html/body/main/div[2]/div[2]/div[1]/div[1]/ul/li[1]/div/div/div/div/div[4]/div[1]/div[2]').text
                        
                        clear_text_4 = driver.find_element(by=By.XPATH , value= '/html/body/main/div[2]/div[2]/div[1]/div[1]/ul/li[1]/div/div/div/div/div[3]/div[1]').click()

                        


                        translated_info =  f'💵 {take_translated_title} 💵\n\n' \
                                        f'• {take_translated_text_1p}\n\n' \
                                        f'• {take_translated_text_2p}\n\n' \
                                        f'• {take_translated_text_3p}\n\n' \
                                        f'• {take_translated_text_4p}\n\n' \
                                        f'Переведено с Английского\n\n' \
                                        f'📈 Источник: {open_new_dict["Source"]} 📈'  



                    except Exception as ex:
                        print(ex)

                    finally:
                        driver.close()
                        driver.quit()
                        
                    #================================================================

                    print(f'[Info] Статья с названием : "{card_header}" была добавлена ')

        except Exception as ex:
            print(ex)

        else:
            continue

    with open(r'D:\Codes Python\Project\parsing\parsutoday\utoday_info.json', 'w' , encoding='utf-8') as file:
        json.dump(json_card_list , file , indent=4 , ensure_ascii=False)       


    return translated_info  
    


def main():
    print(get_new_info())
    
    

if __name__ == '__main__':
    main()
