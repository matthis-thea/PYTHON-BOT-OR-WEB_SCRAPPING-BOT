#coding:utf-8
import  socket
import  time
import  codecs
# Variables
IP = "irc.root-me.org"
channel = "#root-me_challenge"
Port = 6667
my_name = "Matthis"
text = ""
str_example = ""
liste = ""

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("You are connected : " + IP)

irc.connect((IP, Port))

irc.send(bytes("USER " + my_name + " " + my_name + " " + my_name + " :USER USER\r\n", "UTF-8"))
time.sleep(1)

irc.send(bytes("NICK " + my_name + "\r\n", "UTF-8"))
time.sleep(1)

irc.send(bytes("JOIN " + channel + "\r\n", "UTF-8"))
time.sleep(1)

irc.send(bytes("PRIVMSG Candy : !ep3 \r\n", "UTF-8"))
while True:
    text = irc.recv(1024).decode()
    print(text)
    liste = text.split("\r\n")
    word = ""
    for x in liste:
        word = x
        if (word.find("PRIV") != -1):
            chaine = word.split(":")
            liste = chaine[2]
            str_example = codecs.decode(liste, 'rot_13')
            irc.send(bytes("PRIVMSG Candy : !ep3 -rep " + str_example + "\r\n", "UTF-8"))

