# Futtatás

## Alapok
A program futtatásához elengedhetetlen a python miviepy bővítményének megléte a felhasználó számítógépén, ezt viszont egyszerű telepíteni, minössze a command prompt-ba kell beírnunk a következőt: pip install moviepy

Amint ezzel megvagyunk, már indíthatjuk is a programot. Ez szintén a command prompt-ból történik, meg kell adni a fájl mappájának elérési útját, majd a python split_screen_merger.py paranccsal elindítjuk a programot.

A program betöltésekor három gomb és kettő szöveges mező fogad minket.

## Videó importálása
Videó importálására az Import Video gomb segítségével van lehetőség, ha megnyomjuk, megnyitja a fájlkönyvtárunkat, ahonnan ki tudunk választani egy videó fájlt, viszont a program ezen verziójában csakis mp4 kiterjesztésű fájlokat enged feltölteni. Ha ezzel meg vagyunk, az importált videó neve megjelenik a képernyőn. Fontos megjegyezni, hogy maximum négy videó importálására van lehetőség.

## Trimmelés
A videók trimmelésére a videók neve mellett megjelenő két szövegdobozzal van lehetőség. Ezekben az időt olyan formátumban kell megadni, hogy a percet a másodperctől vesszővel elválasztva kell leírni (Például: 2,34 - a kettő perc, harmincnégy perc). Fontos, hogy ezeket a mezőket nem szabad üresen hagyni!

## Inaktív hangsáv kiválasztása
Az inaktív hangsáv kiválasztására a trim mezők után megjelenő checkboxokkal van lehetőség. Értelem szerűen azokat kell bepipálni, amelyikeknek NEM szeretnénk hallani a hangját.

## Vízjel beillesztése
Vízjel beillesztésére az Import Watermark gombbal van lehetőségünk. Ha rákattintunk, szintén megjelenik a fájlkönyvtárunk, ahol kiválaszthatunk egy képet. Fontos hogy a kép méretezésére itt már nincsen lehetőség, így egy megfelelő méretezésű képet kell kiválasztani. Miután megvagyunk, a kép neve szintén megjelenik az ablakon.

## Vízjel áttetszőségének a beállítása
A vízjel áttetszőségét a Watermark opacity mezővel lehet beállítani. Ez egy sszázalékos érték, tehát csak 0-100-ig adhatunk meg neki értéket, máskülönben nem fog működni.

## Videó exportálása
A videó exportálsa a Convert felíratú gombbal történik, amire rákattintva ki kell választani, hogy hova szeretnénk ha letöltené a videónkat, ám mindezek előtt meg kell adni neki egy nevet a Merged video name mezőben. Fontos hogy a program csak kettő vagy négy videót képes összemergelni, tehát ha csak egy, vagy három videónk van, akkor nem fog lefutni a program!