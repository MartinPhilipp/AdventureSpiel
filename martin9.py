#Quellenangabe Bilder:
#schönes Schlafzimmer: https://pixabay.com/de/leerer-raum-zimmer-schlafzimmer-1515108/
#schlafzimmer: https://pixabay.com/de/bauernhaus-schlafzimmer-alte-515619/
#dunkler Gang: https://pixabay.com/de/tunnel-korridor-licht-dunkel-2077792/
#vincent: https://pixabay.com/de/junge-jugendlicher-teenager-jugend-2119178/
#spukhaus: https://pixabay.com/de/geisterhaus-burg-turm-mittelalter-1519860/
#monster: https://pixabay.com/de/tod-dunkelheit-dunkel-haube-164761/
#schatz: https://pixabay.com/de/m%C3%BCnzen-alt-r%C3%B6misch-goldm%C3%BCnzen-2183470/
#loser: https://pixabay.com/de/fail-verlieren-andernfalls-fehler-1714367/
#saal: https://pixabay.com/de/saal-schlo%C3%9F-festsaal-historisch-1998436/
#dunklerGarten: https://pixabay.com/de/mystischer-b%C3%A4ume-nebel-misty-wald-918502/
#wohnzimmer: https://pixabay.com/de/wohnzimmer-viktorianischen-581073/
#küche: https://pixabay.com/de/k%C3%BCche-alt-historisch-1839275/


import easygui
import os

orte = {
    "Anfang": {
        "descr":"Du stehst vor einem düsteren Haus, dass du gerne erforschen möchtest. Da tritt Vincent zwischen den Bäumen hervor. Vertrauen wir Vincent?",
        "picture":"vincent.gif",
        "buttons": {"Ja":["Du gehst weiter.", "Start", -5, 0,+1 ] ,  
                      "Nein":["Du hast verloren.","Loserraum",0,0,0],
                      "Vielleicht":["Du gehst weiter.","Start",0,0,+1],
                      }
                      },
    "Start": {
        "descr":"Vincent möchte ins Haus gehen. Gehst du auch in das Haus?",
        "picture":"spukhaus.gif",
        "buttons": {"JA":["Ihr geht in das Haus.","Eingangshalle",+10,0,+1],
                      "Na gut":["Ihr geht langsam in das Haus","Eingangshalle",+5,0,+1],
                      "Auf keinen Fall!":["Du hast verloren.","Loserraum",0,0,0],
                      }
                      },
    "Eingangshalle": {
        "descr":"Du stehst in einer großen Eingangshalle, als ihr in einer dunklen Ecke etwas bemerkt.Ein Monster taucht auf! Was macht ihr?",
        "picture":"monster.gif", 
        "buttons": {"Weglaufen":["Ihr lauft in einen dunklen Gang.","Dunkler Gang",+5,1,+1],
                     "Kämpfen":["Du hast das Monster besiegt! Das war knapp!","Großer Saal",+5,+45,+1],
                     "Verstecken":["Da ist ja ein Geheimgang!","Geheimgang",+10,0,+1],
                      }
                      },
        
      "Dunkler Gang": {
        "descr":"Das Monster verfolgt euch! Schnell in diesen Gang!",
        "picture":"dunklerGang.gif", 
        "buttons": {"Schnell weiter":["Ihr rennt durch den Gang und erreicht einen verwilderten Garten. Das Monster ist nicht mehr zu sehen.","Garten",+8,0,+1]
                      },
                      },
     "Geheimgang": {
        "descr":"Ein Geheimgang! Wohin der wohl führt? Oh, eine Tür! Wollt ihr hineingehen?",
        "picture":None, 
        "buttons": {"Hineingehen":["Ihr geht in einen Raum, der offenbar einmal ein Schlafzimmer war.","Schlafzimmer",0,0,+1],
                    "Draußen bleiben":["Der Gang scheint ewig so weiter zu gehen.","Geheimgang 2",+3,0,+2]
                      },
                      },
      "Schlafzimmer": {
        "descr":"Hier stehen zwei Betten! Wollt ihr schafen gehen?",
        "picture":"schlafzimmer.gif", 
        "buttons": {"Schlafen!":["Ihr legt euch ins Bett und schlaft ein. Nun habt ihr weniger Angst und Schaden, der Hunger ist gestiegen. Ihr verlasst das Schlafzimer und folgt dem Geheimgang.","Geheimgang 2",-10,-3,+3],
                    "Raum verlassen":["Ihr verlasst den Raum und folgt dem Geheimgang weiter.","Geheimgang 2",+3,0,+1]
                      },
                      },
       "Geheimgang 2": {
        "descr":"Eine Tür! Gehen wir hinein oder kehren wir um?",
        "picture":None, 
        "buttons": {"Hineingehen!":["Ihr geht hinein und befindet euch in einer großen Küche.","Küche",+5,0,+1],
                       "Umkehren!":["Ihr gehst den Gang bis zur Eingangshalle zurück.","Eingangshalle",+5,0,+1],
                      },
                      },
         "Garten": {
        "descr":"Wollt ihr den Garten erforschen oder lieber umkehren und hoffen, dass das Monster nicht mehr da ist?",
        "picture":"dunklerGarten.gif", 
        "buttons": {"Umkehren":["Ihr geht zurück in den dunklen Gang.","Gang Rückweg",+30,0,+1],
                        "Erforschen!":["Ihr geht durch den Garten, bis ihr von Dornen zerkratzt durch eine Tür in ein luxeriös eingerichtetes Wohnzimmer kommt.","Wohnzimmer",+6,+4,+2],
                      },
                      },
        "Gang Rückweg": {
        "descr":"Plötzlich greift das Monster aus einer dunklen Ecke an! Ihr habe keine Chance zu entkommen.",
        "picture":"dunklerGang.gif", 
        "buttons": {"Oh nein!":["Ihr habe keine Chance zu entkommen.","Loserraum",+30,+100,+1],
                      },
                      },
        "Wohnzimmer": {
        "descr":"Hier ist alles staubig. Es führen zwei Türen aus dem Raum, eine riesige doppelflüglige und eine eher unscheinbarere. Wohin wollt ihr gehen?",
        "picture":"wohnzimmer.gif", 
        "buttons": {"Große!":["Ihr betretet einen riesigen Raum.","Großer Saal",+5,0,+1],
                    "Unscheinbare!":["Ihr betretet ein gemütliches Schlafzimmer.","Schönes Schlafzimmer",0,0,+1],
                    "Vincent fragen!":["Vincent geht mit dir durch die prächtige Tür, die in einen riesigen Raum führt.","Großer Saal",+5,+0,+1]
                      },
                      },
         "Großer Saal": {
        "descr":"Das war vermutlich einmal der Festsaal des Hauses. Von hier aus kann man viele Räume betreten. Wo wollt ihr hin?",
        "picture":"saal.gif", 
        "buttons": {"Eingangshalle":["Ihr geht in die Eingangshalle zurück.","Eingangshalle",+3,0,+1],
                    "Küche":["Ihr geht durch einen schmalen Gang in die Küche.","Küche",+2,0,+1],
                    "Wohnzimmer":["Ihr betretet das Wohnzimmer","Wohnzimmer",0,0,+1]
                      },
                      },
         "Küche": {
        "descr":"Das ist die Küche des Hauses. Wollt ihr nachsehen ob in den Schränken etwas Essbares ist oder durch die Tür am Ende des Raumes weitergehen",
        "picture":"küche.gif", 
        "buttons": {"Nachschauen":["Ihr durchsucht die Schränke","Küche 2",+3,0,+1],
                    "Weitergehen":["Ihr folgt einem schmalen Gang in einen riesigen Raum","Großer Saal",0,0,+1]
                      },
                      },
         "Küche 2": {
        "descr":"Essen habt ihr nicht gefunden, dafür eine Tür, die in eine Art Vorratsraum führt. Wollt ihr dort suchen oder lieber durch die Tür am anderen Ende des Raumes weitergehen?",
        "picture":None, 
        "buttons": {"Suchen":["Ihr durchsucht die Kammer nach Essen und werdet fündig. Gestärkt geht ihr nun durch die Tür.","Großer Saal",-5,-10,-1],
                    "Weitergehen":["Ihr folgt einem schmalen Gang in einen riesigen Raum","Großer Saal",0,0,+1]
                      },
                      },
         "Schönes Schlafzimmer": {
        "descr":"Hier steht ein Bett. Willst du dich ausruhen oder lieber umkehren?",
        "picture":"Schönes Schlafzimmer.gif", 
        "buttons": {"Ausruhen":["Als du dich hinlegen willst fällt Vincent eine getarnte Tür neben dem Schrank auf. Ehe du ihn daran hindern kannst schlüpft er durch die Tür in einen dunklen Raum.","Geheimer Raum",+5,-1,+3],
                    "Umkehren":["Ihr kehrt um und gelangt wieder ins Wohnzimmer","Wohnzimmer",0,0,+1]
                      },
                      },
         "Geheimer Raum": {
        "descr":"Unsicher stehst du da als plötzlich ein Aufschrei aus dem dunklen Raum vor dir dringt. Was sollst du nur tun?",
        "picture":None, 
        "buttons": {"Weglaufen":["Voller Angst rennst du aus dem Haus und nimmst dir fest vor, nie wieder ein Spukhaus zu betreten.","Kleiner Loserraum",+5,-1,+3],
                    "Hineingehen":["Mutig betrittst du den dunklen Raum und schaust dich nach Vincent um. Vor dir siehst du einen Lichtschimmer. Vorsichtig gehst du auf ihn zu.","Siegerraum",+20,0,+1]
                      },
                      },
         "Siegerraum": {
        "descr":"Nun erkennst du den Grund für den Schrei. Die Kammer ist mit Goldmünzen gefüllt!Ihr nehmt euch so viel ihr tragen könnt und verlasst glücklich das Haus.     ENDE",
        "picture":"schatz.gif", 
        "buttons": {"Erneut spielen":["Viel Spaß beim nächsten Spiel!","Anfang",-1000,-1000,-1000]
                      },
                      },
        "Loserraum": {
        "descr":"Die Gefahren und Tücken des Spukhauses waren einfach zu viel für dich. Vielleicht hast du beim nächsten Mal mehr Glück.",
        "picture":"loser.gif", 
        "buttons": {"Erneut spielen":["Viel Glück beim nächsten Spiel!","Anfang",-1000,-1000,-1000]},
                      },
        "Kleiner Loserraum": {
        "descr":"Die Gefahren und Tücken des Spukhauses waren zu viel für dich. Immerhin bist du mit dem Leben davongekommen.",
        "picture":"loser.gif", 
        "buttons": {"Erneut spielen":["Viel Glück beim nächsten Spiel!","Anfang",-1000,-1000,-1000]},
        }
}

ort = "Anfang"
damage = 0
hunger = 0
angst = 0

def status():
    return "Angst: {}% Schaden: {}% Hunger: {}%".format(angst,damage,hunger)
    
def checkit():
	print("Checke ob die Bilder existieren")
	for meinort in orte:
		if (orte[meinort]["picture"]!=None):
			if (os.path.exists("./"+orte[meinort]["picture"])==False):
				print("   Ort "+meinort+"  Bild fehlt "+orte[meinort]["picture"])
	print("Pruefe Verknuepfung")
	for meinort in orte:
		for meinziel in orte[meinort]["buttons"].keys():
			ziel=orte[meinort]["buttons"][meinziel]
			if (len(ziel)!=5):
				print("   Ort "+meinort+"  Ziel "+meinziel+" anzahl der werte falsch ")
			if ((ziel[1] in orte)==False):
				print("   Ort "+meinort+"  Ziel "+meinziel+" den Raum gibt es nicht ")
	print("Alle Checks abgeschlossen")

#checkit()

while True:
   
    hunger += 1
    hunger = max(0,hunger)
    angst = max(0,angst)
    
    buttons=orte[ort]["buttons"]
    antwort = easygui.buttonbox(orte[ort]["descr"], "Ort:"+" " + ort +"   "+  status(),
              choices = list(buttons.keys() ), image=orte[ort]["picture"])
    deltaangst = buttons[antwort][2]
    effekt = buttons[antwort][0]
    
    angst += buttons[antwort][2]
    damage += buttons[antwort][3]
    hunger += buttons[antwort][4]
    ort = buttons[antwort][1]
    if angst < 0: 
        angst = 0
    if damage < 0:
        damage = 0
    if hunger < 0:
        hunger = 0
    if angst > 100:
        easygui.msgbox("Vor lauter Angst rennt ihr aus dem Haus.", status())
        ort = "Kleiner Loserraum"
    elif hunger >= 100:
        easygui.msgbox("Du bist verhungert.", status())
        ort = "Loserraum" 
    elif damage >= 100:
        easygui.msgbox("Du bist verblutet.", status())
        ort = "Loserraum"
    else:
        easygui.msgbox(effekt, status())
       
    
