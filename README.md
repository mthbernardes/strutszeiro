# strutszeiro
Telegram Bot to manage botnets created with struts vulnerability(CVE-2017-5638)

#Dependencies
pip install -r requeriments.txt

#Config
<pre>
Create a telegram bot, save the API token in config/token.conf
Create a telegram group, save the group id in config/group.conf
</pre>

#Start
python strutszeiro.py

#Telegram Usage
<pre>
/add url - test vulnerability and add the new server
/exploit url *cmd - execute commands in a specific server (you need to use the * caracter)
/botnet cmd - execute commands in all servers
/total - show total of servers in botnet
</pre>

Thanks to @c0r1ng4