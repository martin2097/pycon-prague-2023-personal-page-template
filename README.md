# Príprava na workshop

Tento template repozitár slúži ako štartovací bod pre workshop "*Interaktivní (nejen) datové aplikace s Plotly Dash*" na pražskom PyCone 2023. Výsledok ku ktorému sa pokúsime smerovať bude vyzerať takto: https://pycon-prague-2023-personal-page.onrender.com/

Na workshope bude každý začínať s kópiou tohto template. Tento podrobný návod slúži na uľahčenie prípravy na workshop, aby sme mohli všetci pracovať spoločne z rovnakého bodu. Pokiaľ ste zvyknutý na iné nástroje a cítite sa v nich komfortne, samozrejme ich môžete využívať :). 

Tento podrobný návod je určený hlavne pre každého, kto s týmito nástrojmi skúsenosti nemá a chce sa pred workshopom a na workshope cítiť komfortne. V prípade akýchkoľvek otázok alebo problémov, na ktoré narazíte, ma pokojne oslovte kedykoľvek v priebehu konferencie a pokúsime sa ich spolu vyriešiť.

Prejdením tohto návodu začneme aj náš workshop (aby sme ale ušetrili čas pri prípadných problémoch, budem rád, ak čo najviac z vás tento návod prejde ešte pred začiatkom). 

### Software, ktorý odporúčam nainštalovať

1. Python - workshop bol pripravovaný vo verzii [3.11.4](https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe)
2. PyCharm Community Edition - [aktuálna verzia 2023.2.1](https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows&code=PCC)
3. GitHub Desktop - [najnovšie verzie](https://desktop.github.com/)

> Na spustenie všetkých skriptov vám bude stačiť iba Python. Vzhľadom na to, že budeme tvoriť komplexnejšiu aplikáciu, budeme na workshope pracovať v prostredí PyCharm. Materiály na workshop sú pripravené ako GitHub template v repozitári v ktorom sa práve nachádzate. Keďže každý bude mať možnosť vytvoriť a nasadiť svoju vlastnú unikátnu osobnú stránku, využijeme aj aplikáciu GitHub Desktop. Všetok software je iba odporúčaný - v rovnakom softwari bude daný workshop vedený. **Neočakávam žiadne skúsenosti s daným softwareom, všetko si ukážeme :).** Zároveň sa ospravedlňujem, ale budeme pracovať v prostredí Windows, s ostatnými systémami nemám skúsenosti.

### Účty, ktoré budeme následne potrebovať

1. Účet na github.com
2. Účet na render.com

> Účet na github.com využijete, aby ste si mohli vytvoriť kópiu tohto template a následne zaverzovať svoju vlastnú stránku. Z tohto repozitára následne nasadíme webovú stránku v službe render.com a vaša osobná stránka sa tak stane prístupnou na internete.

### Vytvorenie kópie z template

V chvíli keď máme všetko nainštalované a registrované môžeme pristúpiť k samotnej príprave. Najprv si vytvoríme svoj vlastný repozitár ako kópiu z tohto template. 

1. Prihlásime sa na github.com
2. Otvoríme si [template](https://github.com/martin2097/pycon-prague-2023-personal-page-template)
3. Klikneme na **Use this template**
4. Vyberieme **Create a new repository**
5. Skontrolujeme, že ako Owner je vybraný náš účet
6. Zvolíme **Repository name** - napríklad my-personal-page
7. Môžeme pridať Description
8. Ponecháme možnosť **Public**
9. **Create repository**

![enter image description here](https://i.ibb.co/jZdNBK6/copy-repostiory-from-template.gif)

### Naklonovanie repozitára na náš počítač

Keď už máme vytvorenú svoju vlastnú kópiu template repozitáru, pristúpime ku klonovaniu repozitáru na náš počítač. 

1. Musíme sa nachádzať v repozitári, ktorý sme vytvorili z template
2. Klikneme na **Code**
3. Vyberieme **Open with GitHub Desktop**
4. Otvorí sa nám okno v GitHub Desktop
5. V **Local Path** vyberieme, kde chceme repozitár naklonovať. Cesta by mala smerovať do prázdneho súboru. Pokiaľ sme spokojný s prednastaveným `C:\Users\moje_meno\Documents\GitHub\my-personal-page` nemusíme nič meniť
6. Kliknem na **Clone**

![enter image description here](https://i.ibb.co/qyTvWnL/clone-repository.gif)

### Otvorenie projektu v PyCharm a vytvorenie virtuálneho prostredia

Posledným krokom je otvorenie projektu v PyCharm a vytvorenie virtuálneho prostredia (naša instance Pythonu v ktorej si nainštalujeme balíčky).

1. Keď sa nachádzame v GitHub Desktop mali by sme vidieť tlačidlo **Open in JetBrains PyCharm**. Pokiaľ tlačidlo nevidíme vojdeme do záložky **Repository** a vyberieme **Open in JetBrains PyCharm**.
2. Projekt sa nám otvorí v PyCharm, zároveň by sa nám malo otvoriť vyskakovacie okno na inicializáciu virtuálneho prostredia. Keďže sme do projektu pribalili súbor `requirements.txt`, stačí okno potvrdiť tlačidlom **OK**
3. PyCharm bude následne chvíľu sťahovať balíčky. Po dokončení sťahovania máme hotovo. 
4. Pokiaľ by sme si chceli overiť, že všetko prebehlo v poriadku, môžeme v ľavom stĺpci nájsť skript app.py, dvojitým poklepaním ho otvoríme. Následne do skriptu klikneme pravým tlačidlom a vyberieme možnosť Run 'app'. Keď v prehliadači otvoríme stránku http://127.0.0.1:8050/ mali by sme vidieť text Hello World! 

![enter image description here](https://i.ibb.co/HgFfcgx/create-project-venv.gif)

### Obsahové zmeny

Keďže účelom tohto workshopu bude vytvorenie osobnej stránky, v súbore ktorý máte naklonovaný na disku sa nachádza súbor `obsah_stranky.txt`. Tento súbor obsahuje všetok textový obsah, ktorý budeme používať na našich stránkach. Pokiaľ by ste si chceli z workshopu odniesť stránku s vlastným obsahom a nie iba vzorový príklad, môžete si tento súbor upraviť (odporúčam si vytvoriť kópiu). Tieto texty následne využijete v priebehu workshopu. Vlastné texty si môžete samozrejme doplniť aj kedykoľvek po skončení workshopu :)

A to je všetko! Dúfam, že vás tento obsiahly návod nevydesil, účelom bolo aby ste sa cítili komfortne pokiaľ by ste sa radi na workshop pripravili :)
