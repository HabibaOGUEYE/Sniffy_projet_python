#http://www.iredmail.org/index.html
#Habiba O'GUEYE TERRIM
#Samba DIOP
#

#Setup you domain

sudo su

nano /etc/hosts

127.0.0.1       mail.mydomain.com mail localhost


wget https://github.com/iredmail/iRedMail/archive/refs/tags/1.5.2.tar.gz

tar -xzvf 1.5.2.tar.gz

cd iRedMail-1.5.2


bash iRedMail.sh

#This starts the wizard.

#DNS Records

A record
MX record


#Admin

https://mail.recinal.com/iredadmin/

#Webmail

https://mail.recinal.com/mail/

username: postmaster@recinal.com
password: Resolve:2020>

#Tips

/root/iRedMail-0.8.6/iRedMail.tips

