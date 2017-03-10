# -*- coding: utf-8 -*-

import os
import time
import telepot
from pprint import pprint
from plugins.actions import actions

class strutszeiro:
    def handle(self,msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if chat_id == self.allowedGROUP and chat_type == 'group' and content_type == 'text':
            actions(self.bot,msg['text'],chat_id)
        else:
            self.bot.sendMessage(chat_id,'GET OUT!!')
            user = msg['from']
            first_name = user['first_name'] if 'first_name' in user else ''
            last_name = user['last_name'] if 'last_name' in user else ''
            username = user['username'] if 'username' in user else ''
            userID = user['id']
            text = msg['text']
            SOS = 'houston we have a problem, someone is trying to talk to me, %s %s, %s owner of id %d sent me this message %s' % (first_name,last_name,username,userID,text)
            self.bot.sendMessage(self.allowedGROUP,SOS)

    def main(self,):
        apiPATH = os.path.abspath(os.path.join('conf','token.conf'))
        apiTOKEN = open(apiPATH).read().strip()
        groupFILE = os.path.abspath(os.path.join('conf','group.conf'))
        self.allowedGROUP = int(open(groupFILE).read())
        self.bot = telepot.Bot(apiTOKEN)
        self.bot.message_loop(self.handle)
        print 'Olha o monstro vindo muleque...'
        while 1:
            time.sleep(10)

if __name__ == '__main__':
    s = strutszeiro()
    s.main()
