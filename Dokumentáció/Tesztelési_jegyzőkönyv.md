## Tesztelési jegyzőkönyv

| Sorszám |Név | Funkció leírása| Vizsgálat módja/eszköze, részletes leírása | Elvárt eredmény| Eredmény |Verzió |
|--|--|--|--|--|--|--|
|T1| Bögös Bálint | Konvertálás | Konvertálás importált állományok nélkül | Fatal error dobása | Hibát dob a pycharmban, de a program tovább fut | Beta 1.1 |
|T2| Bögös Bálint | Importálás | Állomány importálása | Az állomány neve megjelenik a képernyőn | Az állomány neve megjelent | Beta 1.1 |
|T3| Csépányi Gergely | Importálás | Nem videó állomány importálása | Ne engedje feltölteni | Nem engedi feltölteni | Beta 1.1 |
|T4| Csépányi Gergely | Konvertálás | Konvertálás importált állományok nélkül | Fatal error dobása | Hibát dob a pycharm-ban, de a program tovább fut | Beta 1.1 |
|T5| Csépányi Gergely | Konvertálás | Konvertálás 1 importált állománnyal | Fatal error dobása | Hibát dob a pycharm-ban, de a program tovább fut | Beta 1.1 |
|T6| Csépányi Gergely | Konvertálás | Konvertálás 2 importált állománnyal | Videó állomány sikeres letöltése | A videóállományt sikeresen letölti a program a kiválasztott helyre | Beta 1.1 |
|T7| Csomós Patrik | Konvertálás | Konvertálás 3 importált állománnyal | Fatal error dobása | Hibát dob a pycharmban, de a program tovább fut | Beta 1.1 |
|T8| Csomós Patrik | Konvertálás | Konvertálás 4 importált állománnyal | Videó állomány sikeres letöltése | A videó állományt sikeresen letölti a program a kiválasztott helyre | Beta 1.1 |
|T9| Csomós Patrik | Konvertálás | Letöltés fájlnév megadása nélkül | Ne engedje letölteni | Az exportálás sikeresen végbe megy, a fájlnak nem lesz neve, csak kiterjesztése| Beta 1.1 |
|T10| Csomós Patrik | Konvertálás | Letöltés ha a fájlnévben megadjuk a kiterjesztést | Ne engedje letölteni | Az exportálás sikeresen végbe megy, a fájl megkapja a megadott nevet| Beta 1.1 |
|T11| Zettisch Márk | Konvertálás | Letöltés ha a fájlnévben speciális karakterek vannak | Ne engedje letölteni | Hibát dob a pycharmban de a program tovább fut | Beta 1.1 |
|T12| Zettisch Márk | Konvertálás | Nem adunk meg időintervallumot az állományoknak | Az alap hosszával mergelje a többi állománnyal | A pycharm hibát dob, de fut tovább | Beta 1.1 |
|T13| Zettisch Márk | Konvertálás | Túl nagy időintervallumot adunk az állományoknak | Hibával térjen vissza a program | A pycharm hibát dob, de a program fut tovább | Beta 1.1 |

