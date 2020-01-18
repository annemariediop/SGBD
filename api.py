from flask_restful import reqparse, abort, Api, Resource
from flask import Flask, request
from traitement import *
from create_p import *
app = Flask(__name__)
api = Api(app)

class MyAPI(Resource):
	def put(self):
		#requetes=request.form['data'].split()
		requetes_decode=request.form['data']
		requetes=requetes_decode.split()

		if(requetes[0] == "create"):
			if requetes[1]=="database":
				print(b"wa ehh")
				req=create_db_test(requetes_decode)
				if req!="":
					createCC(req)
				else:
					print("Syntaxe incorrecte")
			else:
				if requetes[1]=="table":
					print("doug na deh")
					req=create_table_test(requetes_decode)
					if req!="":
						createCC(req)
					else:
						print("Syntaxe incorrecte")

		
		if(requetes[0]=="use"):
			use(requetes)
		if(requetes[0]=="drop"):
			drop(requetes)
		if (requetes[0]=="update"):
			update(requetes)
		if (requetes[0]=="select"):
			select(requetes)
		if (requetes)[0]=="insert":
			insert(requetes)

    	
    				
api.add_resource(MyAPI, '/')    			

if __name__ == '__main__':
    app.run(debug=True, port=8889)