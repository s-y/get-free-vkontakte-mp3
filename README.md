Get Free VK mp3!
======================

Сначала ставим сам модуль для роаботы с VK  ::

    $ pip install vkontakte

Если вы под Windows то надо скачать https://bitbucket.org/kmike/vkontakte/get/default.zip 
и положить папку vkontakte позле script.py. 

Так как надо получить access token идем на специально подготовленную страницу :  
https://oauth.vk.com/authorize?client_id=2473476&scope=groups,offline,photos,audio,wall,video,docs,places,secure,storage,pages,friends&redirect_uri=blank.html&response_type=token

Даем там права приложению Ask.fm и делаем то от чего нас предостерегают :-) 
А именно копируем токен что там есть в адресной строке

![alt text](https://raw.github.com/s-y/get-free-vkontakte-mp3/master/screen.png "Logo Title Text 1")

Что с ним делать ? ::

    In [1]: import vkontakte
    In [2]: vk = vkontakte.API(token='__Ваш токен__')
    In [3]: print vk.get('audio.get', gid=30559784)[2]
    {u'album': u'36662883', u'artist': u'Vision Anomaly', u'url': u'http://cs521605.vk.me/u21879215/audios/45dae3064020.mp3?extra=69PZLlPd0wRRFmEZexMewgvGifH-JkxR1FHed0i_QRZf97WrHOOjHpuieqAxohJRuIpndhByzF4ae1WWsUrZIb1ghhKS7KmX', u'title': u'Percepcion Emulada', u'genre': 18, u'duration': 247, u'aid': 206202661, u'owner_id': -30559784}
    In [4]: 
Собственно что нам интересно это url. 
Причем качать файл можно только с IP которого обращались к API.

Вместо audio.get можно использовать любой метод с этой страницы -> http://vk.com/pages?oid=-1&p=%D0%9E%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5_%D0%BC%D0%B5%D1%82%D0%BE%D0%B4%D0%BE%D0%B2_API

Например что-бы получить список своей музыки надо сделать ::

    print vk.get('audio.get')

Пример https://github.com/s-y/get-free-vkontakte-mp3/blob/master/script.py
