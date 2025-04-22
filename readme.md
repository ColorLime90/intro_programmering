Elias Berntsson Loggbok
=======================

2025-04-22
[mastergame.py](/mastergame.py), la till så att man ser bollens koordinater uppe i högra textrutan. Ett problem som uppstod var att koordinaterna bestod av ett stort antal decimaler, jag löste det genom att använda str(int(x)) konverterade koordinaterna till heltal. Fixade så att bollen inte fastnar ibland när den studsar genom att arbeta om kollision. En nackdel med min lösning är att den inte använder någon av pygame.sprite s collide funktioner. Däremot så kan den använder den sig av vissa variabler såsom max_speed så att den går att anpassa.

2025-04-08
Fortsatte arbeta på [mastergame.py](/mastergame.py). Gjorde skärmen större och exeperimenterade med lite dynamiska mått. Började omvandla bollen till en sprite, la till att bollens radie blir större med q eller e. La till ett fönster i hörnet för text.

2025-04-07
Skapade en ny pythonfil vid namn [mastergame.py](/mastergame.py). Jag kopierade över kod för inmatning samt rörelse från [ballgame.py](/ballgame.py) till [mastergame.py](/mastergame.py) som jag tyckte var bra. La till en text i spelet som räknar studsar (ej fungerande) och läste på lite om [kod för sprites](https://github.com/karlsson0214/demo_pygame/blob/main/04_droppings_v3_sprite.py).

2025-03-31
Gjorde annat skolarbete.

2025-03-25
Skrev på [ballgame.py](/ballgame.py). Jag löser mina problem med kunskaper de jag redan har, vilket leder till rolig men inte bäst kod. Spelet har en boll som dras neråt av gravitation och studsar när den nuddar väggar. När den nuddar marken så förlorar den lite av sin vertikala hastighet. Bollens rörelse kan påverkas av piltangenterna. q och e centrerar bollen, a och d bollställer vågrät rörelse, w och s återställer lodrät rörelse.

2025-03-24
Skrev på [ballgame.py](/ballgame.py), fixade vågrät rörelse för en boll med acceleration. 

2025-03-18
Läste på om pygame, hur man ritar ut figurer samt hur man kan få figurerna att röra på sig med piltangenterna på ett sätt där rörelsen känns bra och responsiv. Sammanställde lite av detta i [ballgame.py](/ballgame.py)

pygame guide:    http://programarcadegames.com/index.php?chapter=introduction_to_graphics&lang=sv#section_5 

draw circle:    https://www.pygame.org/docs/ref/draw.html#pygame.draw.circle

movement tutorial:  https://www.youtube.com/watch?v=jZ5KmgOGHZI


2025-03-17
Läste lite om RSA: https://people.kth.se/~johantor/foredrag/lusttur/ht03/rsa/index.html 

2025-03-11
La till ytterligare funktioner såsom valet att inte behöva satsa pengar. Finslipade prompts så att de stämmer inför singular och plural (t.ex texten "aktiva ess" och "aktivt ess"). La till cls. 

2025-03-10
Klar med blackjack så att det fungerar och man kan spela det, nu kan man spela kontinuerligt och satsa pengar (Tills man får slut på pengar)

2025-03-03
Blackjack fungerar. La till pengar mm.

2025-02-18
Jag underskattade min förmåga när jag skrev att blackjackkoden nästan var klar. Nu är den nästan klar. Logiken bör funka nu.

2025-02-17
Förbättrade en massa av blackjackkoden. Nästan klar.

2025-01-28
Övade på Github branching, aka gjorde annat.

2025-01-27
Fortsatte med blackjack.

2025-01-21
Utvecklade Blackjack lite.

2025-01-20
Gjorde annat skolarbete

2024-12-10
Fortsatte med Blackjack

2024-12-09
Fortsatte med Blackjack

2024-12-03
Döpte om kortleken till Blackjack. Skrev en del på koden.

2024-12-02
Gjorde annat

2024-11-26
Gjorde annat

2024-11-25
Började på kod för en kortlek. Ska kunna ha grundläggande funktioner som att blanda kort mellan olika spelare, dra kort.

2024-11-18
läst lite olika delar och experimenterat 

2024-10-22
Läste in mig på def och for

24-10-07
woohoo

24-09-17
Sjunde lektionen, fortsatte med fibonacci.

24-09-10
Sjätte lektionen, fortsatte med fibonacci talföljd.

24-09-09
Femte lektionen, började med fibonacci talföljd.

24-09-03
Fjärde lektionen, skrev ett eget program baserad på en uppgift i 7050 if-sats som jag döpte till nodice.py

24-08-27
Andra lektionen, såg till så att git, github och VScodium funkade som de skulle. Loggboken ligger nu uppe på mitt githubkonto. Installerade Python och började med övningarna.

24-08-26
Första lektionen, installerade Git.