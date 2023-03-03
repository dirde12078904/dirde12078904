#  Copyright (c) 2023. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.
print('-------------------------本产品是邵宗贤独家制作,人工智能-小思2023年的新年产物-----------------------')
print('----------本产品加入以我名义开发的新一代模块【 WKS pro 2.0】----------')
print("WPS 加强版(WKS pro 2.0)")
print("Xiao Si wishes everyone and netizens a happy New Year")
print("小思祝大家新年快乐"
      #  Copyright (c) 2023. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
      #  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
      #  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
      #  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
      #  Vestibulum commodo. Ut rhoncus gravida arcu.
      "")
import json as j
import socket
import uuid

import pyttsx3
import requests

print('你好,我是小思')
engline = pyttsx3.init()
engline.setProperty('voice', 'zh')
line0 = '你好，欢迎使用,小思的新年特别版(本产品发布时间为2023年1月21日)'
line1 = '你好，主人'
line2 = '欢迎光临'
line3 = '我是小思同学'
line4 = '小思的新年产品/Xiaosi`s New Year products'
line5 = '欢迎为您服务'
line6 = 'Hello, welcome to KWS pro'
line7 = "Welcome to Small thinking is world pro"
line8 = "Xiao Si wishes you a happy New Year"
engline.say(line0)
engline.say(line1)
engline.say(line2)
engline.say(line3)
engline.say(line4)
engline.say(line5)
engline.say(line6)
engline.say(line7)
engline.say(line8)
engline.runAndWait()


def handle(socket, address):
    while True:
        socket.recv(1080)
        import sys
        import socket
        c = socket.create_connection((sys.argv[1], sys.argv[2]))
        k = socket.create_connection(sys.argv[3], sys.argv[4])
        while 1:
            c.send('\n')
            c.send('\k')


class Turing_robot(object):
    while True:
        a = input()
        url = 'https://api.ownthink.com/bot?appid=9ffcb5785ad9617bf4e64178ac64f7b1&spoken=%s' % a
        te = requests.get(url).json()
        data = te['data']['info']['text']
        print(data)
        ini = pyttsx3.init()
        shuo = ini.say(data)
        shuo = ini.say('daya')
        ini.runAndWait()

    def Turing_robot(init):
        while True:
            a = input()
            url = 'https://api.ownthink.com/bot?appid=9ffcb5785ad9617bf4e64178ac64f7b1&spoken=%s' % a
            te = requests.get(url).json()
            data = te['data']['info']['text']
            print(data)
            ini = pyttsx3.init()
            shuo = ini.say(data)
            shuo = ini.say('daya')
            ini.runAndWait()


engine = pyttsx3.init()


def getTuringText(self, text):
    user_ip = self.getHostIP(2)
    user_ip = self.getHostIP(2)
    mac_id = self.getMacID()
    turing_url_data = dict(key=self.app_key, info=text, userid=mac_id)


def getHostIP(self):
    socket_info = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_info.connect('8.8.8.8', 80)
    ip = socket_info.getsockname()[0]
    return ip


def getMaID(self):
    node = uuid.getnode()

    mac = uuid.UUID(int=node).hex[-12:]
    return mac


voices = 1
voices = 0
""" RATE"""
rate = engine.getProperty('rate')
print(rate)
engine.setProperty('rate', 125)
int(voices)
engine.setProperty('volume', 1.0)

"""VOICE"""
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('voice', voices[1].id)

engine.say("Hello,Windows")
engine.say('my name is xiao si')
engine.runAndWait()
engine.stop()

""" RATE"""
rate = engine.getProperty('rate')
print(rate)
engine.setProperty('rate', 125)

"""VOLUME"""
volume = engine.getProperty('volume')
print(volume)
engine.setProperty('volume', 1.0)

"""VOICE"""
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)


def getTuringText(self, text):
    user_ip = self.getHostIP()
    mac_id = self.getMacID()
    turing_url_data = dict(key=self.app_key, info=text, userid=mac_id)


def getHostIP(self):
    socket_info = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socket_info.connect('8.8.8.8', 80)
    ip = socket_info.getsockname()[0]
    return ip


def getMaID(self):
    node = uuid.getnode()
    mac = uuid.UUID(int=node).hex[-12:]
    return mac


def getMaID(self):
    node = uuid.getnode('voices')


voices = 1
voices = 0
""" RATE"""
rate = engine.getProperty('rate')
print(rate)
engine.setProperty('rate', 125)
int(voices)
engine.setProperty('volume', 1.0)

"""VOICE"""
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('voice', voices[1].id)

engine.say("Hello,Windows")
engine.say('my name is xiao si')
engine.runAndWait()
engine.stop()

""" RATE"""
rate = engine.getProperty('rate')
print(rate)
engine.setProperty('rate', 125)

"""VOLUME"""
volume = engine.getProperty('volume')
print(volume)
engine.setProperty('volume', 1.0)

"""VOICE"""
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)


def getMaID(self):
    node = uuid.getnode()
    mac = uuid.UUID(int=node).hex[-12:]
    return mac


def getMaID(self):
    node = uuid.getnode('voices')


voices = 3
voices = 4

shaozongxian = 1, 2, 3, 4, 5, 6, 7, 8, 9


class Turing_robot(object):
    while True:
        a = input(shaozongxian)
        url = 'https://api.ownthink.com/bot?appid=9ffcb5785ad9617bf4e64178ac64f7b1&spoken=%s' % a
        te = requests.get(url).json()
        data = te['data']['info']['text']['daya']
        print(data)
        print('daya')

        def getMaID(self):
            uuid.getnode('voices')

            def getMaID(self):
                j.data = j.load('https://api.ownthink.com/bot?appid=9ffcb5785ad9617bf4e64178ac64f7b1&spoken=%s')
                node = uuid.getnode('voices')
                while True:
                    a = input()
                    url = 'https://api.ownthink.com/bot?appid=9ffcb5785ad9617bf4e64178ac64f7b1&spoken=%s' % a
                    te = requests.get(url).json()
                    data = te['data']['info']['text']
                    print(data)
                    ini = pyttsx3.init()
                    shuo = ini.say(data)
                    shuo = ini.say('daya')
                    ini.runAndWait()

        ini = pyttsx3.init('voices = 5,voices = 6,voices = 7,voices = 8,voices = 9,voices =10')
        shuo = ini.say(data)
        ini.runAndWait('voices')
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('voice', voices[1].id)
        j.data = j.load(open('my_file.json', 'r'))
        print(j.load(open('my_file.json', 'j')))

        def grtMaID(self):
            node = voices = j = rate = id()
            url = voices = node = rate = j

        def geipandas(help):
            j.decoder(rate)
            redHad = ('self')
            redHad = (print(j))


pro = j.load(20)
WKS = j.encoder()


def __getattr__():
    if WKS is None:
        a = input()
        url = 'https://api.ownthink.com/bot?appid=9ffcb5785ad9617bf4e64178ac64f7b1&spoken=%s' % a
        te = requests.get(url).json()
        data = te['data']['info']['text']['WKS']
        print(data)
        ini = pyttsx3.init()
        shuo = ini.say(data)
        shuo = ini.say('daya')
        ini.runAndWait()


def __getattr__():
    if pro is None:
        b = input()
        url = 'https://api.ownthink.com/bot?appid=9ffcb5785ad9617bf4e64178ac64f7b1&spoken=%s' % b
        te = requests.get(url).json()
        data = te['data']['info']['info']['text']['WKS']['pro']
        print(data)
        ini = pyttsx3.init()
        shou = ini.proxy()
        shou = ini.say("daya")
        ini.runAndWait()
