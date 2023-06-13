from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    korting = prijs - (prijs * korting)
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {korting:.2f} euro."
print (aanbieding_1("aardbei", 4.0, 0.1))

def inkomsten_totaal(inkomsten, btw):
    inkomsten = sum(inkomsten)
    btw = inkomsten * btw
    return f"Het totaal van alle inkomsten van deze week is {inkomsten} euro, waarover {btw} euro btw betaald dient te worden."
print (inkomsten_totaal([220, 430, 125, 160, 205, 90, 345], 0.09))

def laag_en_hoog(mijn_lijst):
    mijn_lijst = max(mijn_lijst), min(mijn_lijst)
    return mijn_lijst
print (laag_en_hoog([220, 430, 125, 160, 205, 90, 345]))

def gemiddelde(mijn_lijst):
    mijn_lijst = sum(mijn_lijst) / len(mijn_lijst)
    return f"De gemiddelde inkomsten deze week zijn {mijn_lijst} euro."
print(gemiddelde([220, 430, 125, 160, 205, 90, 345]))

def meervoudig(invoer_lijst):
    invoer_lijst = laag_en_hoog(invoer_lijst)
    return invoer_lijst
print(meervoudig([10,5,3,2,1,2,9]))

def combinatie(invoer_lijst_2):
    korte_lijst = meervoudig(invoer_lijst_2)
    return mijn_functie_2(korte_lijst)
