
import socket
import json
from traitement import *
from create_p import *
hote = ''
port = 8887

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)
print("Le serveur écoute à présent sur le port {}".format(port))
msg_recu = b""
while 1:


    connexion_avec_client, infos_connexion = connexion_principale.accept()
    while 1:
        msg_recu = connexion_avec_client.recv(4021)
        msg_recu_decode = msg_recu.decode()
        print(msg_recu_decode)
        msg_recu = msg_recu_decode.split()
        donnees = {}

        if(msg_recu[0] == "create"):
            if msg_recu[1]=="database":

                print(b"wa ehh")
                req=create_db_test(msg_recu_decode)
                if req!="":
                    createCC(req)

                else:
                    print(b"Syntaxe incorrecte")
            else:
                if msg_recu[1]=="table":
                    print("doug na deh")
                    req=create_table_test(msg_recu_decode)
                    if req!="":
                        createCC(req)
                    else:
                        print(b"Syntaxe incorrecte")

        
        if(msg_recu[0]=="use"):
            use(msg_recu)
        if(msg_recu[0]=="drop"):
            drop(msg_recu)

        if (msg_recu)[0]=="update":
            update(msg_recu)
        if (msg_recu)[0]=="select":
            sol=select(msg_recu)
            
        if (msg_recu)[0]=="insert":
            insert(msg_recu)
print("Fermeture de la connexion")
connexion_avec_client.close()
connexion_principale.close()
