# Rendszerterv

## A rendszer célja

- A rendszer célja egy olyan alkalmazás elkészítése ahol tetszés szerint kiválasztott videó fájlokat lehet egy állománnyá alakítani
- A program indítása parancsikonon keresztül történik
- A program célja, hogy egyszerűen lehessen több videót összemergelni

## Projektterv
**Projekt szerepkörök, felelősségek**
- szerepkörök
    - product owner: Tajti Tibor
    - scrum master: Guti Adrián, Bencsik Krisztián
    - junior fejlesztők: Csépányi Gergely, Csomós Patrik, Zettisch Márk, Bögös Bálint

- felelősségek: 
    - scrum master: A Scrum mester felügyeli és megkönnyíti a folyamat fenntartását, segíti a csapatot, ha problémába ütközik, illetve felügyeli, hogy mindenki betartja-e a Scrum alapvető szabályait.
    - junior fejlesztő: A projekt elkészítése

**Projekt munkások és felelősségeik** 
Frontend: Csépányi Gergely, Csomós Patrik, Zettisch Márk, Bögös Bálint
Backend: Csépányi Gergely, Csomós Patrik, Zettisch Márk, Bögös Bálint

## Üzleti folyamatok modellje
- Üzleti szereplők:
    - Felhasználó
    
- Üzleti folyamatok:
    - videó fájlok feltöltése
    - videók méretének és pozíciójának változtatása
    - aktív hangsávok kiválasztása
    - videók kezdeti és végpontjainak a megváltoztatása
    - végleges videó letöltése

## Követelmények
- Funkcionális
	- Asztalról való indítás
- Nem funkcionális
	- Gyors működés
	- Egyszerű, egyértelmű kezelés
- Törvényi előírások, szabályok
	- GDPR követelményeinek való megfelelés

## Funkcionális terv
- Rendszerszereplők
	- Felhasználó

- Rendszerhasználati esetek futtatása
	- Felhasználó
		- videó fájlok feltöltése és módosítása

## Fizikai környezet
- Eszköz: Asztali gép/Laptop 
- Operációs rendszer: Független
- Konfiguráció: Nem specifikus

## Absztrakt domain modell
A program működése során a felhasználó több féle szerepkörben tud tevékenykedni. A felhasználó képes videót hozzáadni, kezdő/végpontját beállítani, aktív hangsávot beállítani és letölteni a végső állományt

## Architekturális terv
Az alkalmazást Pycharm-ban és/vagy Visual Studio Code-ban készítjük el

