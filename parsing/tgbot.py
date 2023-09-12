from aiogram import Bot , Dispatcher , executor , types 
from aiogram.dispatcher.filters import Text
from pars import check_news_update
import asyncio
from utodayparsing import get_new_info
import random



token = '564359svks40328:AAFdi_6Gvfkvkkj5VaXBsmoLB-miHqJ1ujjvfdnR4gYbfU'

bot = Bot(token=token)
dp = Dispatcher(bot)


async def news_every_minute():
    while True:
        fresh_news = check_news_update()

        if len(fresh_news) >= 1  :
            await bot.send_message( chat_id = 5344097059 , text = fresh_news , disable_notification=True)
            await bot.send_message( chat_id = 964180757  , text = fresh_news , disable_notification=True) 

        else:
           print ('Пока нет новостей на английском')

        await asyncio.sleep(random.randint(60,90))




async def news_every_minute2():
    while True:
        
        eng_fresh_news = get_new_info()

        if len(eng_fresh_news) >= 1  :
            await bot.send_message( chat_id = 5344097059 , text = eng_fresh_news , disable_notification=True)
            await bot.send_message( chat_id = 964180757  , text = eng_fresh_news , disable_notification=True)
            
        else:
           print('Пока нет новостей')

        await asyncio.sleep(random.randint(60,90))





def main():
    loop = asyncio.get_event_loop()
    loop.create_task(news_every_minute()) 
    loop.create_task(news_every_minute2())
    executor.start_polling(dp)


if __name__ == '__main__':
    main()
    



