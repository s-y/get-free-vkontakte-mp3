#!/usr/bin/env python
# coding: utf-8
from __future__ import unicode_literals

import time
import urllib 
import datetime
import vkontakte
from Queue import Queue
from threading import Thread

num_worker_threads = 10
gid='30559784' # Здесь номер группы, но можно id пользователя
save_to = '/tmp/' # Папка где храним mp3
token=''
i = 0

vk = vkontakte.API(token=token)
source = vk.get('audio.get', gid=gid)

def save(song, save_to=save_to, i=i):
    name = '%s - %s' % (song['artist'], song['title'])
    save_to += name
    print '#'*10 + ' Start download of ' + name
    start = datetime.datetime.now()
    urllib.urlretrieve(song['url'], save_to)
    print '#'*10 + ' Succesful download  of ' + name + (datetime.datetime.now() - stat).__str__()

def worker():
    while True:
        item = q.get()
        save(item)
        q.task_done()

q = Queue()
for i in range(num_worker_threads):
     t = Thread(target=worker)
     t.daemon = True
     t.start()
print source[:10]


for item in source:
    q.put(item)

q.join()   