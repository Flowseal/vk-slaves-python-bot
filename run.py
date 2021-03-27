import time
import random
import requests # pip install requests

from threading import Thread
from module import Slaves # module.py
from config import settings # config.py


# some constants to be used later

token = settings['TOKEN']
local_id = settings['251461069']

steal = settings['STEAL_TOP']
multi_steal = settings['MULTI_STEAL']

targets = settings['TARGETS']
price = settings['MAX_PRICE']

abuse = settings['ABUSE_SLAVES']
abuse_balance = settings['ABUSE_IF_BALANCE']


# init our main client
client = Slaves(token)


jobs = ['Сварщик', 'Шахтёр', 'Бармен', 'Наркоторговец', 'Дилер', 'Брокер', 'Трейдер', 'Инвестор', 'Врач', 'Технарь', 'IT', 'Хирург', 'Бомж', 'Инженер', 'Бригадир']



# //////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////
# Default Calls using API //////////////////////////////////////////////////////


def _start():
    try:
        start = client.start()
        return start
    except Exception as e:
        print(str(e))
        time.sleep(15)
        return _start()

def get_user(id):
    try:
        user = client.user(id=id)
        return user
    except Exception as e:
        print(str(e))
        time.sleep(15)
        return get_user(id)

def get_slaves(id):
    try:
        slaves = client.slave_list(id=id)
        return slaves
    except Exception as e:
        print(str(e))
        time.sleep(15)
        return get_slaves(id)

def buy(id):
    try:
        a_buy = client.buy_slave(slave_id=id)
        return a_buy
    except Exception as e:
        print(str(e))
        time.sleep(15)
        return buy(id)

def make_job(id, name):
    try:
        job = client.job_slave(slave_id=id, job_name=name)
        return job
    except Exception as e:
        print(str(e))
        time.sleep(15)
        return make_job(id, name)

def fetter(id):
    try:
        a_fetter = client.buy_fetter(slave_id=id)
        return a_fetter
    except Exception as e:
        print(str(e))
        time.sleep(15)
        return fetter(id)

def sale(id):
    try:
        a_sale = client.sale_slave(slave_id=id)
        return a_sale
    except Exception as e:
        print(str(e))
        time.sleep(15)
        return sale(id)

def get_top():
    try:
        top = client.top_users()
        return top
    except Exception as e:
        print(str(e))
        time.sleep(15)
        return get_top()


# //////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////




# //////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////
# processing slaves functions //////////////////////////////////////////////////

def get_slaves_to_steal(slaves_list):
    slaves = {}

    current_time = int(time.time()) # текущее unix-время
    for slave in slaves_list['slaves']: # Получаем каждого раба в словаре
        if slave['fetter_to'] < current_time: # проверяем время цепей раба
            if slave['price'] <= price: # если цена подходит под условие
                slaves[slave['id']] = slave['price'] / (slave['profit_per_min'] + 1) # добавляем раба в наш словарь

    return slaves

    
def get_slaves_to_job(slaves_list):
    job_slaves = []

    for slave in slaves_list['slaves']: # Получаем каждого раба в словаре
        if slave['job']['name'] == '': # если безработен
            job_slaves.append(slave['id']) # добавляем раба в безработных

    return job_slaves


def get_slaves_to_fetter(slaves_list):
    slaves = {}
    current_time = int(time.time()) # текущее unix-время
    for slave in slaves_list['slaves']: # Получаем каждого раба в словаре
        if (slave['profit_per_min'] * 120) >= slave['fetter_price']: # мы не уйдём в минус
            if slave['fetter_to'] < current_time: # проверяем время цепей раба
                slaves[slave['id']] = 1 - slave['profit_per_min'] / (slave['fetter_price'] + 1) # добавляем раба в наш словарь (по формуле выгодности)

    # сортируем рабов по цене
    {k: v for k, v in sorted(slaves.items(), key=lambda item: item[1])}
    
    # возвращаем айди рабов
    return list(slaves.keys())


# //////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////




# //////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////
# main functions to be used ////////////////////////////////////////////////////


def job_niggers():
    while True:
        slaves_list = _start()
        slaves_to_job = get_slaves_to_job(slaves_list)
        print(f'{len(slaves_to_job)} раба(ов) подлежат работе')
        
        # даём работу рабам
        for slave in slaves_to_job:
            make_job(slave, jobs[random.randrange(0, len(jobs))])

            # обход блокировки
            time.sleep(random.randrange(0, 2) + min(0.7, 150 / len(slaves_to_job)))
        else:         
            time.sleep(random.randrange(12, 23))


def fet_niggers():
    while True:
        slaves_list = _start()
        slaves_to_fetter = get_slaves_to_fetter(slaves_list)
        print(f'{len(slaves_to_fetter)} раба(ов) подлежат оцепенению')
        
        # кидаем цепи на рабов
        for slave in slaves_to_fetter:
            fetter(slave)

            # обход блокировки
            time.sleep((random.randrange(0, 2) * random.randrange(0, 2)) + min(0.9, 145 / len(slaves_to_fetter)))
            time.sleep(random.randrange(0, 1))
        else:
            time.sleep(random.randrange(11, 18))

def steal_niggers():
    while True:
    
        # покупаем рабов без цепей у целей
        for target in targets:
            targets_slaves = get_slaves(target)
            slaves_to_steal = get_slaves_to_steal(targets_slaves)

            if len(slaves_to_steal) > 0:
                print(f'Найдено {len(slaves_to_steal)} раба(ов) для кражи')

            for slave in slaves_to_steal:
                buy(slave) # покупаем
                time.sleep(random.random() + random.random()) # обход блокировки
                fetter(slave) # кидаем цепь
                time.sleep(random.random() + random.random() + random.random()) # обход блокировки (именно так)
                make_job(slave, jobs[random.randrange(0, len(jobs))]) # даём работу

                # обход блокировки
                time.sleep((random.randrange(0, 2) * random.randrange(0, 2)) + min(0.9, 155 / len(slaves_to_steal)))
                time.sleep(random.random())

            time.sleep(random.randrange(1, 3))
        
        time.sleep(random.randrange(6, 12))


def abuse_niggers():
    while True:
        me = get_user(local_id)
        balance = me['balance']

        if (balance >= abuse_balance):
            slaves_list = _start()

            for slave in slaves_list['slaves']:
                id = slave['id']
                id_used = False

                if (slave['sale_price'] < 19500):

                    s_price = (get_user(id))['sale_price']
                    while s_price < 19500:
                        id_used = True

                        sale(id) # продаём
                        time.sleep(random.random()) # обход блокировки
                        buy(id) # снова покупаем
                        time.sleep(random.random() + random.random() + random.random() * 2) # обход блокировки (именно так)

                        s_price = (get_user(id))['sale_price']

                if (id_used):
                    print(f'Заабузил {id}')

                    fetter(id) # кидаем цепь    
                    time.sleep(random.random() + random.random()) # обход блокировки (именно так)

                    make_job(id, jobs[random.randrange(0, len(jobs))])
                    time.sleep(random.randrange(1, 3) + random.random())

                    id_used = False # useless but ok
        
        time.sleep(random.randrange(24, 40))

def steal_top_reverse():
    top = (get_top())['list']
    top.reverse()

    while True:
        for user in top:
            target = user['id']
            targets_slaves = get_slaves(target)
            slaves_to_steal = get_slaves_to_steal(targets_slaves)

            if len(slaves_to_steal) > 0:
                print(f'Найдено {len(slaves_to_steal)} раба(ов) для кражи')

            for slave in slaves_to_steal:
                buy(slave) # покупаем
                time.sleep(random.random() + random.random()) # обход блокировки
                fetter(slave) # кидаем цепь
                time.sleep(random.random() + random.random() + random.random()) # обход блокировки (именно так)
                make_job(slave, jobs[random.randrange(0, len(jobs))]) # даём работу

                # обход блокировки
                time.sleep((random.randrange(0, 2) * random.randrange(0, 2)) + min(0.9, 155 / len(slaves_to_steal)))
                time.sleep(random.random())

            time.sleep(random.randrange(0, 1))

        time.sleep(random.randrange(8, 15))


def steal_top():
    top = (get_top())['list']

    while True:
        for user in top:
            target = user['id']
            targets_slaves = get_slaves(target)
            slaves_to_steal = get_slaves_to_steal(targets_slaves)

            if len(slaves_to_steal) > 0:
                print(f'Найдено {len(slaves_to_steal)} раба(ов) для кражи')

            for slave in slaves_to_steal:
                buy(slave) # покупаем
                time.sleep(random.random() + random.random() * 2) # обход блокировки
                fetter(slave) # кидаем цепь
                time.sleep(random.random() + random.random() * 2 + random.random()) # обход блокировки (именно так)
                make_job(slave, jobs[random.randrange(0, len(jobs))]) # даём работу

                # обход блокировки
                time.sleep((random.randrange(0, 3) + random.randrange(0, 2)) + min(0.9, 155 / len(slaves_to_steal)))
                time.sleep(random.random())

            time.sleep(random.randrange(0, 2))

        time.sleep(random.randrange(8, 15))


# //////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////



# just start

if __name__ == '__main__':
    _start()

    Thread(target=job_niggers).start()
    Thread(target=fet_niggers).start()

    if (len(targets)):
        Thread(target=steal_niggers).start()

    if (abuse):
        Thread(target=abuse_niggers).start()

    if (steal):
        Thread(target=steal_top_reverse).start()

    if (steal and multi_steal):
        Thread(target=steal_top).start()
