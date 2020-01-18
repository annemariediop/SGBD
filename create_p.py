from pyparsing import (
    CaselessKeyword,
    Literal,
    Word,
    delimitedList,
    alphas,
    alphanums,
    Optional,
    OneOrMore,
    ZeroOrMore,
    CharsNotIn,
    Group,
    nums,
    replaceWith,
    ParseException,
    pyparsing_common as ppc
)
keywords=["create", "database","table", "integer", "varchar"]
[create, database, table,integer, varchar]=[CaselessKeyword (word) for word in keywords]
database_name=Word(alphas, alphanums)
table_name=Word(alphas, alphanums)
colone=Group(Word(alphas, alphanums)+(integer|varchar+"("+ppc.integer+")"))
champs=Group(delimitedList(colone))


InsertIntoStatement=(create+database+ database_name.setResultsName("db_name"))
InsertIntoStatement2=(create+table+ table_name.setResultsName("table_n") + "("+ champs.setResultsName("Colones") +")")
def create_db_test(req):
    #req=input("entrez votre requete : ")
    #print("-->",req)
    try:
        resultat=InsertIntoStatement.parseString(req)
        #  print("tokens", tokens)
        #  print("Nom de la base: ",tokens.db_name)
        #print(resultat)
        return resultat
    except ParseException as err:
        return False
#create_db_test(req)

def create_table_test(req):
    #req=input("entrez votre requete : ")
   # print("-->",req)
    try:
        resultat=InsertIntoStatement2.parseString(req)
        #  print("tokens", tokens)
        #  print("Nom de la base: ",tokens.db_name)
        #print(resultat)
        return resultat
    except ParseException as err:
        return False

#create_table_test()
        
