#!/usr/bin/python3
import csv


def debut_html(nombre,blesse,implique,ratio,pourcentage_alerte,pourcentage_opération_deces): #La fonction suivante créer une page html, les variables entre parenthèses sont des valeurs importés de différentes fonctions

	file = open('nouvellesValeurs.html', 'w', encoding = 'utf-8')
	message="""                                        
		<html>
	<head>
	<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<link href="style2.css" rel="stylesheet" type="text/css">
		<script src="https://cdnjs.cloudflare.com/ajax/libs/PapaParse/5.1.0/papaparse.min.js"></script>
	<title>NouvellesValeurs(page principale)</title>
	</head>
	<body>
	<div class="background">
	</div>
	

	<section class  = "donnee">
		<h3>Les données fournies par le CROSS</h3>
		<p>Ici se trouve les données  de base presente dans le tableau et calculé via un script python<p>


	<div class="donnee_base">
		<div class="operations">
			<img src="op.png" alt = "opérations de sauvetage logo">
			<h4>Opérations de sauvetage</h4>
			<p>Le nombre d'opérations effectué sur l'année 2018<p/>
			<a class="btn">{0}</a> <!--valeur issue de la 1er varible importé dans la fonction -->
		</div>
		
		<div class="blesse">
			<img src="image.png" alt = "nombre de personne blessé">
			<h4>Nombre de personne blessées</h4>
			<p>Le nombre de personne blessées sur l'année 2018<p/>
			<a class="btn">{1}</a> <!--valeur issue de la ds 2 ème varible importé dans la fonction -->
		</div>
		
		<div class="implique">
			<img src="image3.png" alt = "opérations de sauvetage logo">
			<h4>Nombre de personne impliquée</h4>
			<p>Le nombre de personne impliqué sur l'année 2018<p/>
			<a  class="btn">{2}</a> <!--valeur issue de la 3ème varible importé dans la fonction -->
		</div>
	</div>
	</section>
	
	<section class="donnee2">
		<h3>Les nouvelles données calculées</h3>
		<p>Ici se trouve les données calculées via des fonctions et générées par un script python<p>
		<div class="donnee_calcule">
		
			
			<div class="ratio">
				<img src="ratio.jpg" alt = "opérations de sauvetage logo">
				<h4>Pourcentage de blesssés</h4>
				<p>Le pourcentage de personne blessé sur le nombre de personne impliqué<p/>
				<a  class="btn">{3}</a> <!--valeur issue de la 4ème varible importé dans la fonction -->
			</div>
			
			<div class="mort">
				<img src="mort.jpg" alt = "nombre de personne blessé">
				<h4>Nombre d'operation avec déces</h4>
				<p>Le part représenté des opérations contenant des décès<p/>
				<a  class="btn">{5}</a> <!--valeur issue de la 5ème varible importé dans la fonction -->
			</div>
			
			<div class="alerte">
				<img src="megaphone.jpg" alt = "fausse alerte logo">
				<h4>La part des fausses alertes representées en chiffe</h4>
				<p>Le nombre d'opération engendrée par de fausses alertes '<p/>
				<a  class="btn">{4}</a> <!--valeur issue de la 6 ème varible importé dans la fonction -->
				</div>
		</div>
	</div>
	
	</section>
	<section class="recherche">
		<div class="consigne">
			<p>remplissez le champs de recherche par les valeurs suivantes (copié-collé est plus simple ;) : plaisancier ;pecheur ,etranger ,clandestin</p>
		</div>
		<div class="boxsearch">
		 	<input type="search" id="search" value="" onchange="ouvrirPage()"><input type="submit" id="btn" value="Chercher" onclick="ouvrirPage()">
		</div>
		
		 <script>
			function ouvrirPage() <!-- fonction permettant d'ouvrir les pages html en insérrant des valeurs sur une barre de recherche généré grace à un code javascript -->
			{{
				var a = document.getElementById("search").value;
				if (a === ""){{
					alert("remplissez le champs de recherche par les valeurs suivantes (copié-collé est plus simple ;) : plaisancier ;pecheur ,etranger ,clandestin");
				}}
				if (a === "plaisancier"){{
					window.open("plaisancier.html"); <!-- par exemple on vas ici ouvrir le fichier "plaisancier.html" si on tape "plaisancier" dans la barre de recherche -->
				}}
				if (a === "pecheur"){{
					window.open("pecheur.html");
				}}
				if (a === "etranger"){{
					window.open("etranger.html");
				}}
				if (a === "clandestin"){{
					window.open("clandestin.html");
				}}
				
			   
				
		}}
    
    </script>

			
	</section>
	</div>
	<footer></footer>
	</body>
	</html>
	""".format(nombre, blesse,implique,ratio, pourcentage_alerte,pourcentage_opération_deces) #on importe les différentes valeurs issus d'un script python avec .format qui ont respectivement pour ordre 0,1,2,3,4,5

	file.write(message) #afficher le contenu de message soit toute la page HTML
	file.close()


def html_plaisancier(plaisancier): #fonction qui génère la page plaisancier
	file = open('plaisancier.html', 'w', encoding='utf-8')
	message = """
		<html>
	<head>
	<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<link href="style2.css" rel="stylesheet" type="text/css">
	<title>Le nombre de plaisanciers sur l'année 2018</title>
	</head>
	<body>
	<div class="background">
	</div>
	<section class  = "donnee">
		<h3>Les données fournies par le CROSS sur les plaisancier</h3>
		<p>Tout d'abord qu'est ce qu'un plaisancier? <br>
		Les plaisanciers en région sont avant tout composés de retraités résidant en région possédant un bateau d'occasion et pratiquant les sorties à la journée.<br>
		Le nombre de plaisanciers atteint aujourd’hui les 13 millions et les immatriculations de bateaux de plaisance augmentent d’environ 12 000 unités par an. Sur le littoral,<br>
		 près de 473 installations portuaires sont destinées à l’accueil des navires de plaisance. En eaux intérieures, il est dénombré 556 installations portuaires ou haltes nautiques.<br>
		  8 500 km de voies d’eau navigables et d’innombrables lacs ou plans d’eau sont ouverts à la navigation de plaisance. <br>
		L’enjeu économique de la filière nautique est majeur : la France est le premier constructeur de bateaux de plaisance en Europe et le second au niveau mondial. L’actualité des loisirs nautiques s’exerce sur l’ensemble du territoire.<p>
		<div class="donnee_base">
		
		
		<div class="newlink">
			
			<h4>Le nombre de plaisanciers</h4>
			<p>Le nombre de plaisanciers sur l'année 2018<p/>
			<a class="btn">{0}</a>
		</div>
		
	


	
	<footer></footer>
	</body>
	</html>
	""".format(plaisancier) #on importe la variable plaisancier contenu dans la fonction nombre_plaisancier

	file.write(message)
	file.close()

def nombre_plaisancier():
	f = open('resultats_humain.csv', 'r', encoding='utf-8')
	myReader = csv.DictReader(f)
	c = 0
	for row in myReader:
		if row["categorie_personne"] == "Plaisancier français": #on va chercher dans la colonne ""categorie_personne" du fichier "resultats_humain.csv" qui comporte la ligne "plaisancier français"
			c += 1 #on incrémente +1 à chaque ligne correspondante
	print("Voici le nombre de plaisancier",c)
	html_plaisancier(c) #on récupère la variable pour l'injecter dans la fonction "html_plaisancier" qui génère la page "plaisancier.html", on stcok alors la variable dans "c"
	f.close() #on ferme le fichier csv apres utilisation pour qu'il puisse le parcourir une nouvelle fois en cas de besoin

def html_pecheur(pecheur): #fonction qui génère la page pecheur
	file = open('pecheur.html', 'w', encoding='utf-8')
	message = """
		<html>
	<head>
	<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<link href="style2.css" rel="stylesheet" type="text/css">
	<title>Le nombre de plaisanciers sur l'année 2018</title>
	</head>
	<body>
	<div class="background">
	</div>
	<section class  = "donnee">
		<h3>Les données fournies par le CROSS sur les pecheurs</h3>
		<p>Les pêcheurs: <br>
		Le secteur de la pêche constitue un univers autonome régi par ses spécificités et ses valeurs.<br>
		 Tout au long du littoral, les zones de pêche présentent les situations les plus variées selon les espèces pêchées, les techniques utilisées, les genres de navigation, les débouchés commerciaux, les types d'armement, etc.
		</p>
		<div class="donnee_base">


		<div class="newlink">

			<h4>Le nombre de pecheurs</h4>
			<p>Le nombre de pecheurs sur l'année 2018<p/>
			<a class="btn">{0}</a>
		</div>





	<footer></footer>
	</body>
	</html>
	""".format(pecheur) #on importe la variable c contenu dans la fonction nombre_pecheur

	file.write(message)
	file.close()

def nombre_pecheur(): #fonction qui cherche dans la colonne "categorie_personne" du fichier "resultats_humain.csv" et qui comporte la ligne "Pêcheur français" puis effectue une incrémentation pour compter nb de ligne
	f = open('resultats_humain.csv', 'r', encoding='utf-8')
	myReader = csv.DictReader(f)
	c = 0
	for row in myReader:
		if row["categorie_personne"] == "Pêcheur français":
			c += 1
		else:
			pass
	print("Le nombre de pêcheurs vaut : ", c)
	html_pecheur(c) #on stock la variable dans "c" puis on l'injecte comme argument à la fonction  html_pecheur pour utilisé la valeur à la page web
	f.close()



def html_etranger(etranger):  #fonction qui génère la page pecheur
	file = open('etranger.html', 'w', encoding='utf-8')
	message = """
		<html>
	<head>
	<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<link href="style2.css" rel="stylesheet" type="text/css">
	<title>Le nombre de plaisanciers sur l'année 2018</title>
	</head>
	<body>
	<div class="background">
	</div>
	<section class  = "donnee">
		<h3>Les données fournies par le CROSS sur les étrangers</h3>
		<p>Les étrangers en mer <br>
		 Ce sont les personnes dépourvu de nationnalité française et n'ayant pas le statu de clandestin<br>
		</p>
		<div class="donnee_base">


		<div class="newlink">

			<h4>Le nombre de plaisanciers</h4>
			<p>Le nombre de plaisanciers sur l'année 2018<p/>
			<a class="btn">{0}</a>
		</div>





	<footer></footer>
	</body>
	</html>
	""".format(etranger)#on importe la variable etranger stocker dans la fonction "nombre_etranger"

	file.write(message)
	file.close()

def nombre_etranger():
	f = open('resultats_humain.csv', 'r', encoding='utf-8')
	myReader = csv.DictReader(f)
	c = 0
	for row in myReader:
		if row["categorie_personne"] == "Marin étranger":
			c += 1
		else:
			pass
	print("Le nombre d'étrangers vaut : ", c)
	html_etranger(c) #on stock la variable dans "c" puis on l'injecte comme argument à la fonction  html_etranger pour utilisé la valeur à la page web
	f.close()



def html_clandestin(clandestin):
	file = open('clandestin.html', 'w', encoding='utf-8')
	message = """
		<html>
	<head>
	<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<link href="style2.css" rel="stylesheet" type="text/css">
	<title>Le nombre de plaisanciers sur l'année 2018</title>
	</head>
	<body>
	<div class="background">
	</div>
	<section class  = "donnee">
		<h3>Les données fournies par le CROSS sur les clandestins</h3>
		<p>Tout d'abord qu'est ce qu'un clandestin? <br>
		Les clandestins sont des personnes qui à la suite d'une immigration en dehors d'un cadre légal,<br>
		 les personnes se trouvent dans une situation dénommée étrangers en situation irrégulière, aussi appelées « clandestins », ou « sans-papiers ».<p>
		<div class="donnee_base">


		<div class="newlink">

			<h4>Le nombre de clandestin</h4>
			<p>Le nombre de clandestin sur l'année 2018<p/>
			<a class="btn">{0}</a>
		</div>





	<footer></footer>
	</body>
	</html>
	""".format(clandestin)

	file.write(message)
	file.close()

def nombre_clandestin():
	f = open('resultats_humain.csv', 'r', encoding='utf-8')
	myReader = csv.DictReader(f)
	c = 0
	for row in myReader:
		if row["categorie_personne"] == "Clandestin":
			c += 1
		else:
			pass
	print("Le nombre de clandestins vaut : ", c)
	html_clandestin(c)
	f.close()




def nombre_disparu():
	f = open('resultats_humain.csv', 'r', encoding='utf-8')
	myReader = csv.DictReader(f)
	c = 0
	for row in myReader:
		if row["resultat_humain"] == "Personne disparue":
			c += 1
		else:
			pass
	print(c,"Le nombre de personne disparu")

	f.close()



def valide(table):  ### fonction qui crée une copie de la table et modifie le type de certaines données
	op_id = table["operation_id"]
	cat_prsn = table["categorie_personne"]
	res_hum = table["resultat_humain"]
	nombre = int(table["nombre"])
	nb_blesse = int(table["dont_nombre_blesse"])
	return {"op_id": op_id, "cat_prsn": cat_prsn, "res_hum": res_hum, "nombre": nombre, "nb_blesse": nb_blesse}

def nb_de_prsn(registre):  ### fonction qui renvoie le nombre de personnes impliquées
	n = 0
	for i in registre:
		n = n + i["nombre"]
	return n

def nb_de_blesse(registre):
	n = 0
	for i in registre:
		n = n + i["nb_blesse"]
	return n

def ratio():
	f = open('resultats_humain.csv', 'r', encoding='utf-8')
	c = nb_de_blesse(table_valide)/nb_de_prsn(table_valide)*100# effectue la divison nombre de personne blesse/ nombre de personne totale multiplié par 100 car c'est un pourcentage
	c=round(c,3) #permet d'arrondir la variable c à 3 chiffres après la virgule
	x=str(c)+"%"
	print(x)
	f.close()
	return x

def nombre_opdeces():
	f = open('resultats_humain.csv', 'r', encoding='utf-8')
	myReader = csv.DictReader(f)
	c = 0
	for row in myReader:
		if row["resultat_humain"] == "Personne décédée accidentellement":
			c += 1
		else:
			pass
	print("Le nombre d'operation contenant des deces",c)

	f.close()
	return c

def alerte():
	f = open('resultats_humain.csv', 'r', encoding='utf-8')
	myReader = csv.DictReader(f)
	c=0
	for row in myReader:
		if row["resultat_humain"] == "Personne impliquée dans fausse alerte":
			c += 1
		else:
			pass
	print(c,"le nombre d'alerte")
	f.close()
	return c

def Palerte(w): #une fonction qui calcul le pourcentage d'operation engendré par des fausses alertes
	c = alerte()/w*100 #Ici la valeur du nombre d'alerte calculé par la fonction "alerte" divisé par le nombre de personne puis le tout multiplié par 100 car c'et un pourcentage
	c=round(c,3) # On arrondie la valeur à 3 chiffres après la virgule

	x=  str(c)+"%" #on affiche la variable sous forme de chaine de caractère avec le signe "%" ajouté à la suite
	print(x)
	return x






















## PROGRAMME PRINCIPAL
fichier = open("resultats_humain.csv")
table = list(csv.DictReader(fichier))
#print (table)

### TABLE VALIDE ###
table_valide = [valide(x) for x in table]            # Création par compréhension



nombre_opdeces()


alerte()



w = nb_de_prsn(table_valide ) # est la valeur qui stock le nombre de personne


def nb_operation():
	f = open('resultats_humain.csv', 'r', encoding='utf-8')
	lignecompteur = 0
	for row in f:#pour chaque ligne dans le fichier csv
		x = row.split(",") # on défini ici chaque fin de ligne par le séparateur ","
		lignecompteur += 1 #on incremente +1 à chaque fin de ligne
	print(lignecompteur,"le nombre d'operatoion totale effectué")
	f.close()
	return lignecompteur
nb_operation()


def Pop_deces():# fonction qui calcule le pourcentage d'opération contenant des déçès
	c =nombre_opdeces()*100/nb_operation()
	c=round(c,4)
	x= (str(c)+"%")

	return x
Pop_deces()


def fonctions():#Fonction qui récupère les varibles des autres fonctions pour les injecter dans la page html principale
	f = open('resultats_humain.csv', 'r', encoding='utf-8')
	lignecompteur = 0
	for row in f:
		x = row.split(",") 
		#on défini ici chaque fin de ligne par le séparateur ","
		lignecompteur += 1
	print("Il y a alors",lignecompteur,"opérations de sauvetage qui on été effectué sur l'année 2018" )
	debut_html(lignecompteur,nb_de_blesse(table_valide ),nb_de_prsn(table_valide ), ratio(), Palerte(w),Pop_deces() )

	f.close()

fonctions() #appelle de la fonction

















## PROGRAMME PRINCIPAL
fichier = open("resultats_humain.csv")
table = list(csv.DictReader(fichier))
#print (table)

### TABLE VALIDE ###
table_valide = [valide(x) for x in table]            # Création par compréhension
#print(table_valide)

w = nb_de_prsn(table_valide )
x = nb_de_blesse(table_valide )
y = x/w #ratio blessé impliqué

y=round(y,4)
print(y)
# Le pourcentage de personne blessé parmis les operations
# Le nombre de personne impliqué par opérations
print ("nombre total de personnes impliquées : ", w)
print ("nombre total de personnes blessées : ", x, ", ce qui donne un porcentage de : ", y, "% de blessés")

nombre_pecheur()
nombre_etranger()
nombre_clandestin()
nombre_disparu()
nombre_plaisancier()









