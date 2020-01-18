
import socket
import sys
import json
hote = "localhost"
port =8887
connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))
data = json.load(open("user_pass.json", "r"))
msg_a_envoyer = " "
connexionBd= False
for user in data:
        if(data[user]['username']== sys.argv[2]):
                
                if(data[user]['password']== sys.argv[4]):
                        
                        connexionBd=True
                        print("Connexion établie avec le serveur sur le port {}".format(port))
                        break
        else:
                print("mot de passe ou nom d'utilisateur incorrect")
                msg_a_envoyer = b""
if connexionBd==True:                        
        while msg_a_envoyer !="fin":
                msg_a_envoyer = input("jsonBase> ")
                msg_a_envoyer = msg_a_envoyer.encode()
                
                connexion_avec_serveur.send(msg_a_envoyer)
                                                        
                
print("Fermeture de la connexion")
