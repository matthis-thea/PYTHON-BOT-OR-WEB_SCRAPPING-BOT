#coding:utf-8
import  socket
import  time
import  math

# Variables
IP = "irc.root-me.org"
channel = "#root-me_challenge"
Port = 6667
my_name = "Matthis"
text = ""
b = 1

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("You are connected : " + IP)

irc.connect((IP, Port))

irc.send(bytes("USER " + my_name + " " + my_name + " " + my_name + " :USER USER\r\n", "UTF-8"))
time.sleep(1)

irc.send(bytes("NICK " + my_name + "\r\n", "UTF-8"))
time.sleep(1)

irc.send(bytes("JOIN " + channel + "\r\n", "UTF-8"))
time.sleep(1)

irc.send(bytes("PRIVMSG Candy : !ep1 \r\n", "UTF-8"))
while (b == 1):
    text = irc.recv(1024).decode()
    print(text)
    liste = text.split("\r\n")
    word = ""
    for x in liste:
        word = x
        if (word.find("PRIV") != -1):
            chaine = word.split(":")
            final = chaine[2]
            final = final.split("/")
            result = math.sqrt(float(final[0])) * float(final[1])
            result = round(result, 2)
            final_result = "{}".format(result)
            irc.send(bytes("PRIVMSG Candy : !ep1 -rep " + final_result + "\r\n", "UTF-8"))
            b = 0
while True:
    text = irc.recv(1024).decode()
    print(text)

