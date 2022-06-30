import random



wariat = input("wloski klimat, rosyjski klimat, balkanski klimat, polski klimat czy random? ")

wloski = ["Damazzio", "Matheozzi", "Mazzianno", "Kristozzotti"]
rosyjski = ["Damianov", "Klimnoff", "Maciejev", "Krystoff"]
balkanski = ["Damianić", "Matikoć", "Macioć", "Krycionić"]
polski = ["Damiowski", "Mateowski", "Maćkowicz", "Krzyosztowił"]

bot = random.choice([wloski, rosyjski, balkanski, polski])



    
if wariat == "random":
     print(bot)


if bot == "wloski":
    print(wloski)

if bot == "rosyjski":
    print(rosyjski)
    
if bot == "balkanski":
    print(balkanski)

if bot == "polski":
    print(polski)


if wariat == "wloski":
    print("Damazzio", "Matheozzi", "Mazzianno", "Kristozzotti")

if wariat == "rosyjski":
    print("Damianov", "Klimnoff", "Maciejev", "Krystoff")


if wariat == "balkanski":
    print("Damianić", "Matikoć", "Macioć", "Krycionić")


if wariat == "polski":
    print("Damiowski", "Mateowski", "Maćkowicz", "Krzyosztowił")
