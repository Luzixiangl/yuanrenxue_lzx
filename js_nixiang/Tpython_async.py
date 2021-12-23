# -*-coding:utf-8-*-
# import json
# import re
# import requests
# import pandas as pd
# import redis as redis
# import time
# import arrow
# import hashlib

import aiohttp
import asyncio
# import aioredis
# from config import redis_info, CUR_BATCH1, TYPE


async def get_bs_n_data():
    print("abc")


async def async_main():

    while True:
        try:
            async_list = []
            for i in range(10):
                async_list.append(get_bs_n_data())
            print("长度为：", len(async_list), async_list)
            if async_list != []:
                await asyncio.gather(*async_list)
                await asyncio.sleep(5)
                # break
            else:
                break
        except Exception:
            continue
if __name__ == '__main__':

    asyncio.get_event_loop().run_until_complete(async_main())
    # async_main()

