# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/3/17 6:08 PM
#       @Author  : cxy =.= 
#       @File    : async_await.py
#       @Software: PyCharm
#       @Desc    : 
# ---------------------------------------------
async def downloader(url):
    return 'cxy'


async def download_url(url):
    # do something
    html = await downloader(url)

    return html


if __name__ == '__main__':
    coro = download_url("http://www.imooc.com")
    coro.send(None)
