import pandas as pd
import matplotlib.pyplot as plt

dataframe_data=pd.ExcelFile("GraphMakerV1.xlsx")#on construit un dataframe pour ensuite le lire. 
paramètres=pd.read_excel(dataframe_data,"paramètres")#je déclare ma page de paramètrage 

courbes=paramètres["valeurs"][0] #Je récupère quel type de graphe je veux plot.
barres=paramètres["valeurs"][3]

if courbes !="off":
    data= pd.read_excel(dataframe_data,"données courbes")#un peu obscure mais fonctionne comme ça.

    légende= pd.read_excel(dataframe_data,"légende courbes")#je déclare mes données dans un feuillets et la lagénde dans un autre

    nombre_de_lignes=paramètres["valeurs"][2]
    multiple=paramètres["valeurs"][1]

    #le plot

    fig,ax=plt.subplots()#on déclare la figure
    ax.plot(data["X"], data["Y"], label=légende["nom des courbes"][0], color=légende["couleur"][0]) #je plot la première ligne.

    if multiple == 1:# je teste si on cherche à faire plusieurs ligne de graph ou pas
        i=2
        while i<= nombre_de_lignes:
            ax.plot(data["X"], data[str(i)], label=légende["nom des courbes"][i-1], color=légende["couleur"][i-1])#je plot la nouvelle ligne
            i=i+1#j'ajoute 1 pour passer à la ligne suivante 
    
    

    #légende
    titre=légende["titre du graphique"][0]
    x=légende["légende x"][0]
    y=légende["légende y"][0]
    plt.ylabel(y)
    plt.xlabel(x)#plot de l'axe x, y et du titre 
    plt.title(titre)
    plt.legend()#je met en place la légende

    plt.show()#j'affiche le graphique
    
if barres !="off":
    data= pd.read_excel(dataframe_data,"données barres")#un peu obscure mais fonctionne comme ça.
    légende= pd.read_excel(dataframe_data,"légende barres")#je déclare mes données dans un feuillets et la lagénde dans un autre

    nombre_de_stacked=paramètres["valeurs"][5]
    stacked=paramètres["valeurs"][4]

    fig,ax=plt.subplots()#on déclare la figure

    #on plot la première barre qui est toujour là avec les donnée de la première variable de la barre
    nom_des_bars= légende["nom des bars"]#je déclare mon label => le nom de ma bar 
    donnée = data["1"]#je donne la première colone 
    width=0.35#on pose la largeur de ma bar

    ax.bar(nom_des_bars,donnée,width, label=légende["nom des champs"][0],color=légende["couleur"][0])#je plot


    #on a un cas avec un stack
    if stacked!=0: 
        i=2
        bas=data["1"]#je pose le bas de mon stack pour le stack suivant 
        while i <=nombre_de_stacked:
            donnée= data[str(i)]#je récupère ma valeur pour mon satck i
            ax.bar(nom_des_bars,donnée,width,bottom=bas, label=légende["nom des champs"][i-1],color=légende["couleur"][i-1])#je plot par dessus la précédante valeur 
            bas=bas+donnée #je stock mon nouveau bas pour le champ suivant 
            i=i+1 #j'ajoute 1 pour passer à la donnée suivante 

    titre=légende["titre du graphique"][0]
    x=légende["légende x"][0]
    y=légende["légende y"][0]
    plt.ylabel(y)
    plt.xlabel(x)#plot de l'axe x, y et du titre 
    plt.title(titre)
    plt.legend()#je met en place la légende 
    plt.show()#j'affiche 



