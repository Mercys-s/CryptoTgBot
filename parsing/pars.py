import requests
from bs4 import BeautifulSoup
import time
import json


def get_first_news(url):
    
    

    headers = {
        'accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.100',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': 'adBlockerNewUserDomains=1662965932; udid=d1673841d70db545bdf61b4c25690949; _ga=GA1.2.505636899.1662965935; PHPSESSID=dqp77f8ubi6q5755lk2udchh7m; _ym_uid=166296594437371901; _ym_d=1662965944; G_ENABLED_IDPS=google; r_p_s_n=1; reg_trk_ep=exit popup banner; __gads=ID=3739c3542d065173:T=1662965967:S=ALNI_MaRVd8wQrwfA3UWBcil5SEQRfkf1A; _VT_content_2180806_2=1; sideBlockTimeframe=max; _VT_content_2181323_2=1; geoC=RU; gtmFired=OK; __cflb=02DiuF9qvuxBvFEb2qB21qtXaSmcrvEM1K8gyDpkwouVn; _VT_content_200296524_1=1; _gid=GA1.2.1883765198.1663392561; __gpi=UID=00000b37a2037528:T=1662965967:RT=1663392561:S=ALNI_MZeVdVMC7R_i74aF9JalmkViVEMlQ; _ym_isad=2; adsFreeSalePopUp=3; g_state={"i_p":1663479010450,"i_l":2}; _VT_content_2181723_2=1; _VT_content_2183603_2=1; _VT_content_2183695_2=1; smd=d1673841d70db545bdf61b4c25690949-1663396462; _ym_visorc=b; __cf_bm=62eG_J0OhGO2UmUtDCUNdX5ntAKyZb8VjDupYDDbVig-1663396464-0-AdTyrPRGge2s89zOklvp3Y9dJ38fdBYUdDSbIfy1Mxx8/Zfueyv7q7xv+El1nw8gUG2gC5UH1DGlA/941aj/JcBxuf0QoTJ6oNROOTpNIeXnTK8DSOikl6fpT0cahGgstfZ70jkHKmOV6yU+1ZvGQGsjk0lML2jqNMMDW90rXxeK; nyxDorf=NTFiNmQ0MHI3YDwyYzU3K2U1ZD1kZjcrNTVjYTE%2B'
    }

    url = 'https://ru.investing.com/news/cryptocurrency-news'

    r = requests.get(url = url , headers = headers )

    soup = BeautifulSoup(r.text , 'lxml')

    articles_cards = soup.find('section',id='leftColumn').find('div',class_= 'largeTitle').find_all('article', class_='articleItem')
    
    articles_text_list = {}


    # Отсеиваю посты на английском языке, собираю в список
    
    for article in articles_cards :
        autor_name = article.find('span').text.split()[0]

        if autor_name == 'Investing.com':
            article_text = article.find('div',class_='textDiv').find('a',class_='title').text.split(':')[0]
            find_id = article.get('data-id')

            articles_text_list[find_id] = (
                {
                    'Name': article_text.replace('\xa0',' ')
                }
            )
            
            print(find_id)
            time.sleep(3)
       
        else:
            continue
    
    with open(r'D:\Codes Python\Project\parsing\files\new_dict.json', 'w' , encoding='utf-8') as file:
        json.dump(articles_text_list, file , indent=4, ensure_ascii=False)
   




def check_news_update():
    
    
    with open(r'D:\Codes Python\Project\parsing\files\new_dict.json','r',encoding='utf-8') as file:
        new_dict = json.load(file)
    


    headers = {
        'accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.100',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': 'adBlockerNewUserDomains=1662965932; udid=d1673841d70db545bdf61b4c25690949; _ga=GA1.2.505636899.1662965935; PHPSESSID=dqp77f8ubi6q5755lk2udchh7m; _ym_uid=166296594437371901; _ym_d=1662965944; G_ENABLED_IDPS=google; r_p_s_n=1; reg_trk_ep=exit popup banner; __gads=ID=3739c3542d065173:T=1662965967:S=ALNI_MaRVd8wQrwfA3UWBcil5SEQRfkf1A; _VT_content_2180806_2=1; sideBlockTimeframe=max; _VT_content_2181323_2=1; geoC=RU; gtmFired=OK; __cflb=02DiuF9qvuxBvFEb2qB21qtXaSmcrvEM1K8gyDpkwouVn; _VT_content_200296524_1=1; _gid=GA1.2.1883765198.1663392561; __gpi=UID=00000b37a2037528:T=1662965967:RT=1663392561:S=ALNI_MZeVdVMC7R_i74aF9JalmkViVEMlQ; _ym_isad=2; adsFreeSalePopUp=3; g_state={"i_p":1663479010450,"i_l":2}; _VT_content_2181723_2=1; _VT_content_2183603_2=1; _VT_content_2183695_2=1; smd=d1673841d70db545bdf61b4c25690949-1663396462; _ym_visorc=b; __cf_bm=62eG_J0OhGO2UmUtDCUNdX5ntAKyZb8VjDupYDDbVig-1663396464-0-AdTyrPRGge2s89zOklvp3Y9dJ38fdBYUdDSbIfy1Mxx8/Zfueyv7q7xv+El1nw8gUG2gC5UH1DGlA/941aj/JcBxuf0QoTJ6oNROOTpNIeXnTK8DSOikl6fpT0cahGgstfZ70jkHKmOV6yU+1ZvGQGsjk0lML2jqNMMDW90rXxeK; nyxDorf=NTFiNmQ0MHI3YDwyYzU3K2U1ZD1kZjcrNTVjYTE%2B'
    }

    url = 'https://ru.investing.com/news/cryptocurrency-news'

    r = requests.get(url = url , headers = headers)

    soup = BeautifulSoup(r.text , 'lxml')

    articles_cards = soup.find('section',id='leftColumn').find('div',class_= 'largeTitle').find_all('article', class_='articleItem')  # type: ignore
    
    
    # Цикл - Получаю ссылки на сами статьи и буду парсить с них инфу  
    
    fresh_news = {}
    ready_news = ()

    for article in articles_cards:
        find_id = article.get('data-id')
        
        # Лист с статьями
       
        try:
            
            # Фильтр
            
            autor_name = article.find('span').text.split()[0]
            if autor_name == 'Investing.com':
                article_text = article.find('div',class_='textDiv').find('a',class_='title').text.split(':')[0]
                find_id = article.get('data-id')
                

                # Получение инфы
                
                if find_id in new_dict :
                    continue
                
                else:

                    card_href = article.find('a').get('href')
                    
                    href = f'https://ru.investing.com{card_href}'

                    req = requests.get(url = href, headers = headers )
                    soup = BeautifulSoup(req.text , 'lxml')
                    
                    card_title = soup.find('div', class_='wrapper').find('h1',class_='articleHeader').text.split(':')[0].replace('\xa0',' ')
                    card_image = soup.find('div',class_='WYSIWYG articlePage').find('div',class_='imgCarousel').find('img').get('src')
                    card_text = soup.find('div',class_='WYSIWYG articlePage').find_all('p')
                    
                    card_text_list = []
                    
                    
                    # Цикл для обработки 'p' тегов (текст)
                    for p in card_text:
                        p.text.strip()
                        if 'Позиция успешно добавлена:' in p.text:
                            continue
                        else:
                            card_text_list.append(p.text)
                    
                    

                    a = card_text_list[1:len(card_text_list)]
                    
                    paragraf = card_text_list[0]
                    paragraf2 = card_text_list[1]
                    paragraf3 = card_text_list[2]
                    paragraf4 = card_text_list[3]
                    paragraf5 = card_text_list[4]
                    
                    all_paragraf = f'• {paragraf}\n\n• {paragraf2}\n\n• {paragraf3}\n\n• {paragraf4}\n\n• {paragraf5}'

                    card_text_not_list = ' '.join(a)



                    
                    # Добавление информации в Json,чтобы информация не повторялась

                    new_dict[find_id] = (
                        {
                            'Image_Src': card_image,
                            'News_Title': card_title,
                            'News_Text': card_text_not_list.replace('\n',' ').replace('\xa0',''), 
                            'Source': href
                        }
                    )


                    fresh_news[find_id] = (
                        {
                            'Image_Src': card_image,
                            'News_Title': card_title,
                            'News_Text': card_text_list,
                            'Source': href
                        }
                    )

                    open_fresh_news = fresh_news[find_id]
                    news = f'🐹 {open_fresh_news["News_Title"]} 🐹\n\n' \
                           f'{all_paragraf}\n\n' \
                           f'🐻 Источник: {open_fresh_news["Source"]} 🐻\n\n' \
                            
                    ready_news = news


                    
                    print(f'[Info] Статья с названием : "{card_title}" была добавлена ')
    
                
        except Exception as ex:
            print(ex)
       
        else:
            #print('Новых статей пока нет')
            continue
    
    with open(r'D:\Codes Python\Project\parsing\files\new_dict.json','w',encoding='utf-8') as file:
        json.dump(new_dict, file , indent=4, ensure_ascii=False)
    


    return ready_news

def main():
    #get_first_news('https://ru.investing.com/news/cryptocurrency-news')
    print(check_news_update())
    

if __name__ == '__main__':
    main() 



