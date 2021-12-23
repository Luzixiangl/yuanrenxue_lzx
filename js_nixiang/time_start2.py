# -*-coding:utf-8-*-
from datetime import date, datetime
# import redis
import time
import os
import arrow
import time
import hashlib
import json
import re
from apscheduler.schedulers.background import BackgroundScheduler
import requests

def form1(data):
    if data == "":
        return None
    if data == "None":
        return None
    if data == []:
        return None
    if data == {}:
        return None
    else:
        return str(data)


def id_listing1(url):
    """
    生成 id
    :param url:
    :return:
    """
    batch = cur_batch()
    md5 = hashlib.md5()
    md5.update(f'{url}{batch}'.encode('utf-8'))
    return md5.hexdigest()


def cur_week():
    """
    获取当前是年度第几周
    :return:
    """
    return time.strftime("%W")


def cur_time(fmt):
    """
    获取当前的时间/日期字符串.
    """
    time_str = arrow.now().format(fmt)
    return time_str


def cur_batch():
    """
    批次号，年度第几周
    :return:
    """
    if cur_batch1:
        return cur_batch1
    else:
        batch_ = cur_time('YYYY') + cur_week()
        return batch_
def tick():
    print("tick ! the time is : %s" % datetime.now())
    os.system("python 20-重置所有账号.py")
def tick1():
    print("tick ! the time is : %s" % datetime.now())
    os.system("python 23-us爬取sk_asin_list的卖家精灵数据4.py")
def tick2():
    print("tick ! the time is : %s" % datetime.now())
    # os.system("python 15-爬取bs_asin的卖家精灵数据4.py")
    os.system("python 23-fr爬取sk_asin_list的卖家精灵数据4.py")
def tick3():
    print("tick ! the time is : %s" % datetime.now())
    # os.system("python 15-爬取bs_asin的卖家精灵数据4.py")
    os.system("python 23-ca爬取sk_asin_list的卖家精灵数据4.py")
def tick4():
    print("tick ! the time is : %s" % datetime.now())
    # os.system("python 15-爬取bs_asin的卖家精灵数据4.py")
    os.system("python 23-uk爬取sk_asin_list的卖家精灵数据4.py")
def tick5():
    print("tick ! the time is : %s" % datetime.now())
    # os.system("python 15-爬取bs_asin的卖家精灵数据4.py")
    os.system("python 23-es爬取sk_asin_list的卖家精灵数据4.py")
def tick6():
    print("tick ! the time is : %s" % datetime.now())
    # os.system("python 15-爬取bs_asin的卖家精灵数据4.py")
    os.system("python 23-de爬取sk_asin_list的卖家精灵数据4.py")
def tick7():
    print("tick ! the time is : %s" % datetime.now())
    # os.system("python 15-爬取bs_asin的卖家精灵数据4.py")
    os.system("python 23-it爬取sk_asin_list的卖家精灵数据4.py")

def tick8():
    print("tick ! the time is : %s" % datetime.now())
    # os.system("python 15-爬取bs_asin的卖家精灵数据4.py")
    os.system("python 26-ca爬取bs_asin_list的卖家精灵数据4.py")
def tick9():
    print("tick ! the time is : %s" % datetime.now())
    # os.system("python 15-爬取bs_asin的卖家精灵数据4.py")
    os.system("python 26-de爬取bs_asin_list的卖家精灵数据4.py")
def tick10():
    print("tick ! the time is : %s" % datetime.now())
    # os.system("python 15-爬取bs_asin的卖家精灵数据4.py")
    os.system("python 26-es爬取bs_asin_list的卖家精灵数据4.py")
def tick11():
    print("tick ! the time is : %s" % datetime.now())
    # os.system("python 15-爬取bs_asin的卖家精灵数据4.py")
    os.system("python 26-fr爬取bs_asin_list的卖家精灵数据4.py")
def tick12():
    print("tick ! the time is : %s" % datetime.now())
    # os.system("python 15-爬取bs_asin的卖家精灵数据4.py")
    os.system("python 26-it爬取bs_asin_list的卖家精灵数据4.py")
def tick13():
    print("tick ! the time is : %s" % datetime.now())
    # os.system("python 15-爬取bs_asin的卖家精灵数据4.py")
    os.system("python 26-uk爬取bs_asin_list的卖家精灵数据4.py")
def tick14():
    print("tick ! the time is : %s" % datetime.now())
    # os.system("python 15-爬取bs_asin的卖家精灵数据4.py")
    os.system("python 26-us爬取bs_asin_list的卖家精灵数据4.py")


def get_proxy():
    r.delete('ip_pool:amazon')
    get_ip = json.loads(requests.get(
        url="http://api01.idataapi.cn:8000/proxyip?apikey=yPCg6ig17c811fD2EzCtm0oz7FE8BtCeS0vQxd9n6S4ZqBO9fvMJZFgR2GaOxZoT").text)
    if get_ip.get('data'):
        ip_lis1 = get_ip['data']
        for i in ip_lis1:
            the_ip1 = f"{i['proxy_ip']}:8000"
            r.sadd('ip_pool:amazon', the_ip1)

if __name__ == "__main__":

    from config import redis_info, CUR_BATCH1, TYPE
    scheduler = BackgroundScheduler()
    r = redis.Redis(host=redis_info["host"], port=redis_info["port"], db=redis_info["db"],
                    password=redis_info["password"], decode_responses=True)
    cur_batch1 = CUR_BATCH1
    # type = TYPE
    # 是否是公司 产品
    t_ape = "1"
    # cur_batch1 = ""
    batch11 = cur_batch()
    # scheduler.add_job(get_bs_asin_elf,)
    # scheduler.add_job(get_bs_asin_elf1, 'interval', minutes=4)
    # scheduler.add_job(get_bs_asin_elf2, 'interval', minutes=5)
    # scheduler.add_job(get_bs_asin_elf3, 'interval', minutes=6)
    type_obj = {
        'amazon.com': 'amazon_com',
        'amazon.ca': 'amazon_ca',
        'amazon.co.jp': 'amazon_jp',
        'amazon.co.uk': 'amazon_uk',
        'amazon.es': 'amazon_es',
        'amazon.de': 'amazon_de',
        'amazon.fr': 'amazon_fr',
        'amazon.it': 'amazon_it',
        'amazon.com.au': 'amazon_au',
    }
    #
    # for k ,v in type_obj.items():
    #     scheduler.add_job(get_bs_asin_elf1, 'interval', minutes=8,args=[k])
    #     scheduler.add_job(get_bs_asin_elf2, 'interval', minutes=9,args=[k])
    #     scheduler.add_job(get_bs_asin_elf3, 'interval', minutes=10,args=[k])
    scheduler.add_job(tick, 'interval', minutes=10)
    # scheduler.add_job(tick1, 'interval', minutes=10)
    # scheduler.add_job(tick2, 'interval', minutes=30)
    # scheduler.add_job(tick3, 'interval', minutes=30)
    # scheduler.add_job(tick4, 'interval', minutes=30)
    # scheduler.add_job(tick5, 'interval', minutes=30)
    # scheduler.add_job(tick6, 'interval', minutes=30)
    # scheduler.add_job(tick7, 'interval', minutes=30)

    ############
    scheduler.add_job(tick8, 'interval', minutes=30)
    scheduler.add_job(tick9, 'interval', minutes=30)
    scheduler.add_job(tick10, 'interval', minutes=30)
    scheduler.add_job(tick11, 'interval', minutes=30)
    scheduler.add_job(tick12, 'interval', minutes=30)
    scheduler.add_job(tick13, 'interval', minutes=30)
    scheduler.add_job(tick14, 'interval', minutes=30)

    # scheduler.add_job(get_bs_asin_elf1, 'interval', minutes=4, args=['amazon.com'])
    # scheduler.add_job(get_bs_asin_elf2, 'interval', minutes=5, args=['amazon.com'])
    # scheduler.add_job(get_bs_asin_elf3, 'interval', minutes=6, args=['amazon.com'])
    #
    # scheduler.add_job(get_bs_asin_elf1, 'interval', minutes=4, args=['amazon.ca'])
    # scheduler.add_job(get_bs_asin_elf2, 'interval', minutes=5, args=['amazon.ca'])
    # scheduler.add_job(get_bs_asin_elf3, 'interval', minutes=6, args=['amazon.ca'])


    # scheduler.add_job(get_bs_asin_elf3, 'interval', minutes=2)
    # scheduler.add_job(tick, 'interval', seconds=5,misfire_grace_time=3600,max_instances=10)
    # print(a)
    # scheduler.add_job(tick, 'interval', minutes=2)
    # scheduler.add_job(tick, 'interval', days=1, start_date="2021-2-19 5:00:00")
    # scheduler.add_job(tick, 'cron' ,hour=11,minute=44)
    # scheduler.add_job(tick,'cron', hour='12-23', minute='00', second='00')
    # scheduler.add_job(tick,'cron', hour='0-6', minute='00', second='00')
    scheduler.start()
    # print("Press Ctrl + {0} to exit".format('Break' if os.name == 'nt' else 'C'))
    try:
        while True:
            time.sleep(5)
            print(f"sleep! - {datetime.now()}")

    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        print("Exit The Job !")