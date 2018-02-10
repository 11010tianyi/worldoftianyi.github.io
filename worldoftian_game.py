#!/usr/bin/env python
# _*_ coding: utf-8 _*_
__author__ = 'tiany'
__date__ = '2018/2/9 10:30'

from sys import exit
from random import randint

class Map(object):

    def __init__(self):
        self.quips = [
            "你挂了",
             "Game Over.",
             "你像个失败者.",
             "江湖险恶，英雄请重新来过!"
        ]
        # self.start = start

    # def play(self):
    #     next = self.start
    #
    #     while True:
    #         print "\n************************"
    #         room = getattr(self, next)
    #         next = room()


    def death(self):
        print "\n"
        print self.quips[randint(0, len(self.quips)-1)]
        exit(1)

    def central_corridor(self):
        print "欢迎来到田怡的世界!"
        print "\n"
        print "来到这里，首先你要干点什么呢？"
        action = raw_input("> ")

        if action == "吃饭":
            print "\n##########"
            print "田怡的世界只有精神食粮！"
            return 'death'

        elif action == "睡觉":
            print "\n##########"
            print "在田怡的世界里睡着了就不会在醒来了！"
            return 'death'

        elif action == "找出口":
            print "\n##########"
            print "田怡的世界里没有出口！"
            return 'death'

        elif action == "打他":
            print "\n##########"
            print "田怡的世界里的人都是很友善的！"
            return 'death'

        elif action == "爱他":
            print "\n##########"
            print "在田怡的世界里爱不是唯一的主题！"
            return 'death'

        elif action == "找屁屁":
            print "\n##########"
            print "田怡的世界里屁屁无处不在！"
            return 'death'

        elif action == "q" or action == "exit":
            print "\n##########"
            print "你可能是需要离开！"
            return 'death'

        elif action == "学习":
            print "\n##########"
            print "对.只有学习是唯一的出路"
            return 'laser_weapon_armory'

        else:
            print "\n##########"
            print "在田怡的世界可能暂时不能完成这些事!"
            return 'central_corridor'

    def laser_weapon_armory(self):
        print "你可能需要一个密码推开第一扇门！"
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input("[三位哦]> ")
        guesses = 0
        if guess == "q" or guess == "exit":
            print "你可能是需要离开！"
            return 'death'
        while guess != code and guesses < 10:
            if guesses<5:
                print "用点♥ 猜!"
            else:
                print "不要放弃！"
            guesses += 1
            if guesses >= 9:
                print "上天从不辜负会努力的人！：%s"%code
            guess = raw_input("[记得是三个数哈]> ")
            if guess == "q" or guess == "exit":
                print "你可能是需要离开！"
                return 'death'

        if guess == code:
            print "你推开了田怡的世界的第一扇大门."
            return 'the_bridge'
        else:
            print "你可能是真的尽力了！"
            return 'death'


    def the_bridge(self):
        print "哇,只有勇者才能到达这里，恭喜你！"
        print "打开了第一扇门你将会看到："
        
        action = raw_input("> ")

        if action == "田怡":
            print "你看不到我，因为我无处不在！"
            return 'death'

        if action == "世界":
            print "世界一直都在你的视线！"
            return 'death'

        if action == "屁屁":
            print "都说了，你别想了！"
            return 'death'

        if action == "自己":
            print "你看不到你，因为这是我的世界！"
            return 'death'

        if action == "q" or action == "exit":
            print "你可能是需要离开！"
            return 'death'


        elif action == "知识":
            print "对，知识的力量是无穷的！"
            print "而且不光是知识，你还能看到一个鲜活的思想!"
            return 'escape_pod'
        else:
            print "\n##########"
            print "可能这不是你该看到的!"
            return "the_bridge"

    def escape_pod(self):
        print "你看到的知识是什么？"
        print "能描述么?"
        alist = ["python",'鸡汤','生物','生活',"自拍","干货"]
        good_pod = alist[randint(0,5)]
        guess = raw_input("[两个字或一个词]> ")
        if guess == "q" or guess == "exit":
            print "你可能是需要离开！"
            return 'death'

        n = 1
        while guess != good_pod and  n<5:
            print "\n##########"
            print " %s 可能不是今天的主题." % guess
            n+=1
            if n>3:
                print "今天的主题可能是 %s 或者 %s" % (good_pod,alist[randint(0,5)])
            if n>=5:
                print "你可能是需要认真的思考一下！"
                return 'death'
            guess = raw_input("[两个字或一个词]> ")
            if guess =="q" or guess =="exit":
                return 'death'
        else:
            print "\n##########"
            print "%s 是我们今天的主题." % guess
            print "你真的是万里挑一的智慧！"
            print "希望你在这里能有些许收获,"
            print "这是我的荣幸，"
            print "同时也是我最大的期望，是我之所以坚持的理由！"
            print "恭喜你，你成功了!"
            print "***************************"
            exit(0)


class Engine(object):
    def __init__(self,start):
        self.start = start

    def play(self):
        next = self.start

        while True:
            print "\n************************"
            room = getattr(Map(), next)
            next = room()



Engine("central_corridor").play()
# a_game = Game("central_corridor")
# a_game.play()