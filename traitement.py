import os
import json

class Traitements(object):
	"""docstring for ClassName"""
	pass
current_db=""
def createCC(requetes):
	global current_db
	
	if requetes[1]== "database":
		with open("/home/annie/Downloads/Compressed/projetBDDIC2/my_flask_app/{0}.json".format(requetes[2]), 'w') as fichier:
			json.dump({}, fichier)
		fichier.close()
		return "base de donnee creee"
	else:
		if requetes[1]== "table":
			if current_db!="":
				with open("/home/annie/Downloads/Compressed/projetBDDIC2/my_flask_app/{0}".format(current_db)) as f:
					db=json.load(f)
					
					champs=[]
					meschamps=requetes.Colones
					j=1

					for i in range(len(meschamps)): 
						champs.append(meschamps[i][0])
			
					db['{0}'.format(requetes[2])]={}

					for k in range(len(champs)):
						db['{0}'.format(requetes[2])]['{0}'.format(champs[k])] = "here"
				
					with open("/home/annie/Downloads/Compressed/projetBDDIC2/my_flask_app/{0}".format(current_db), 'w') as f1:
						json.dump(db, f1, indent=4)
					return champs
		
		
	
def use(requetes):
	global current_db
	if requetes[0]=="use":
		if requetes[1]== "database":
			path="/home/annie/Downloads/Compressed/projetBDDIC2/my_flask_app/{0}.json".format(requetes[2])
			if os.path.exists(path):
				current_db="{0}.json".format(requetes[2])
				return "base de donnees ouverte"
			else:
				return "base de donnees inexistante"

def drop(requetes):
    global current_db    
    if requetes[1]=="database":
        path='{0}.json'.format(requetes[2])
        if os.path.exists(path):
            os.remove(path)
            current_db =""
            return "base de donnees supprimee"
        else:
            return "base de donnees inexistante"
    else:
        if requetes[1]=="table":
            if current_db !="":
                data = json.load(open("{0}".format(current_db), 'r'))
                delete = [] 
                for key, val in data.items(): 
                    if key == requetes[2]: 
                        delete.append(key) 
                    for i in delete: 
                        del data[i]
                        print(data) 
                        with open("{0}".format(current_db), 'w') as f1:
                            json.dump(data, f1, indent=4)
def select(requetes):
	if current_db !="":
			if requetes[1]=="*":
				if requetes[2]=="from":
					with open("{0}".format(current_db)) as json_data:
						data_dict = json.load(json_data)
						data_str = json.dumps(data_dict)
						begin_balise =requetes[3]
						end_balise = '},'
						pos_begin = data_str.find(begin_balise)
						pos_end = data_str.find(end_balise,pos_begin)
						print("ya doug na")
						if pos_begin > 1:
							tables = data_str[pos_begin : pos_end]
							print(tables)
							return tables
						else : 
							return ("table inexistante")

def update(requetes):
    val = requetes[5]
    if current_db !="":
        with open("{0}".format(current_db)) as json_data:
            table_dict = json.load(json_data)
            for table,value_tab in table_dict.items():
                if table == requetes[1]:
                    if requetes[2]=="set":
                        col = requetes[3]
                        if col in value_tab:
                            if requetes[4]=="=":
                                if requetes[6]=="where":
                                    condition=requetes[7]
                                    if condition in value_tab:
                                        if requetes[8]=="=":
                                            v = requetes[5]
                                            if(table_dict[table][col] == requetes[9]):
                                                with open("{0}".format(current_db), "w") as f:
                                                    table_dict[table][col] = v
                                                    json.dump(table_dict, f, indent=4)
                                                    print("Mise a jour effectuee")
def insert(requetes):
    global current_db
    if (requetes[1] == "into" and requetes[3] == "values" ):
        data = json.load(open("{0}".format(current_db) ,'r+'))
        for key, val in data.items():
            if( key == requetes[2]):
                donnee  = data[requetes[2]].keys()
                diction = {}
                tab = []
                for i in range(len(requetes)):
                    if requetes[i] in ['(',','] :
                    	j = i+1
                    	while not requetes[j] == ')':
                        	tab.append(requetes[j])
                        	j+=1
                print(tab)
                tab.remove(",")
                print(tab)
                diction = dict(zip(donnee,tab))
                # print(diction)
                    
        with open("{0}".format(current_db), 'a') as f1:
            json.dump(diction, f1, indent=4)
            # print(data)