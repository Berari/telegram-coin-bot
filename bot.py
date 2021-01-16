from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from telethon import TelegramClient, events, sync
import requests
import json
import hashlib
from time import sleep, time
import re
import webbrowser
import urllib.request
import os
import sqlite3
import collections
import random





def wating(x, opts, cur, client):

    sleep(3600)
    bot(x, opts, cur, client)


def start_client(x):
    db = sqlite3.connect('Accounts.db')
    cur = db.cursor()

    print("Очередь аккаунта № " + str(x))
    cur.execute(f"SELECT PHONE FROM telegram WHERE ID = '{x}'")
    sleep(0.2)
    Phone = str(cur.fetchone()[0])
    print("Входим в аккаунт: " + Phone)
    cur.execute(f"SELECT PASSWORD FROM telegram WHERE ID = '{x}'")
    sleep(0.2)
    password = str(cur.fetchone()[0])
    print(password)
    cur.execute(f"SELECT API_ID FROM telegram WHERE ID = '{x}'")
    sleep(0.2)
    api_id = str(cur.fetchone()[0])
    cur.execute(f"SELECT API_HASH FROM telegram WHERE ID = '{x}'")
    sleep(0.2)
    api_hash = str(cur.fetchone()[0])
    session = str("anon" + str(x))
    client = TelegramClient(session, api_id, api_hash)
    client.start()
    
    db.close()

    return client

def browser(driver, url):
    
    try:
        driver.get(url)
        sleep(1.5)
        time = driver.find_element_by_class_name('timer').text.split('wait')[1].split(' ')[1]
        time = int(time) + 2
        #print(time)

        sleep(time)
        driver.close()

    except:
        time = 13
        sleep(time)
        driver.close()

def checking_link_list(linkl_list):

    a = [item for item, count in collections.Counter(linkl_list).items() if count > 1]
    i = len(a)

    if i == 0:
        print('совпадений нет')

        return False

    else:

        return True

def listening_messages(x, cur, opts, client):

    task = []


    while True:
        
        time = random.randint(1,10)

        sleep(time)

        client.send_message('LTC Click Bot', '🖥 Visit sites')
        sleep(1.5)
        dp = client.get_entity('LTC Click Bot')
        messages = client.get_messages(dp, limit=1)
        for message1 in messages:
            text = message1.message.split('😟')[0]
        print(text)
        
        if text == 'Sorry, there are no new ads available. ':
            print('заданий нет')
            task.append('1')


        if len(task) >= 4:
            task = []
            print('заданий больше нет')
            main(x = x + 1 )

def method_2(x, opts, cur, client):
    while True:

        client.send_message('LTC Click Bot', '🖥 Visit sites')
        sleep(2)

        dp = client.get_entity('LTC Click Bot')
        messages = client.get_messages(dp, limit=1)

        for message in messages:
        
            text = message.message

        try:
            url = text.split('---------------------')[1].split('❤❤❤❤❤❤❤❤❤')[1].split('\n')
            #a = len(url)
            #url = url.split('\n')
            print(url)

        except:
            url = text.split('---------------------')[1]
            #a = len(url)
            #url = url.split('\n')
            print(url)

def bot(x, opts, cur, client):
    time_list = []
    cycles_passed = 0
    driver = Firefox(options=opts)
    link_list = []
    i = 0
    try:
        while True:

            startTime = time()
            #print(startTime)

            try:
                time1 = random.randint(1, 3)
                sleep(time1)
                client.send_message('LTC Click Bot', '🖥 Visit sites')
                sleep(2)

                dp = client.get_entity('LTC Click Bot')
                messages = client.get_messages(dp, limit=1)
            
                for message in messages:
                    a = message.reply_markup
                    url = a.rows[0].buttons[0].url
                print(url)
                link_list.append(url)
                
                browser(driver,url)
                

                endTime = time() #время конца замера
                totalTime = endTime - startTime #вычисляем затраченное время
                print(totalTime)
                time_list.append(totalTime)

                #if text == 'There is a new site for you to /visit! 🖥':
                    #print('___________________________________________\n')
                    #print('messages')
                    #print('___________________________________________\n')
            except:
                pass
        
            if cycles_passed >= 5:
                i = 0
                a = checking_link_list(link_list)
                link_list = []

                if a :

                    average_time = sum(time_list) / len(time_list)

                    print('заданий боль нет')
                    print('Всего пройденно циклов: ' + str(cycles_passed) + ' Среднее время цикла: ' + str(average_time))

                    print('бот ожидает новые задания')
                    wating(x, opts, cur, client)

                    break
            
            cycles_passed = cycles_passed + 1
            print('Цикл пройден за: ' + str(totalTime) + ' Циклов пройдено: '+ str(cycles_passed))

    except:
        print('ошибка')    

def main(x):


    db = sqlite3.connect('Accounts.db')
    cur = db.cursor()
    opts = Options()
    opts.set_headless()
    assert opts.headless

    client = start_client(x)

    bot(x, opts, cur, client)
    #method_2(x, opts, cur, client)

    

if __name__ == "__main__":
    main(1)