# AutoSuggestsApp

Gebruik jij de suggesties in Google ter inspiratie voor je zoekwoorden onderzoek? Het is vaak een mooie manier maar enorm tijdrovend!

Daarom heb ik de AutoSuggestsApp gecreëerd! Een app voor Windows en Mac waarbij je gemakkelijk van 5 zoekwoorden tegelijk de suggesties uit Google kunt scrapen en ze vervolgens makkelijk kunt opslaan als CSV of kopiëren naar je klembord.

# Waarom deze app?
Als SEO’er doe ik geregeld zoekwoorden onderzoek. Een onderdeel hiervan is opdoen van inspiratie en dat deed ik vaak in Google zelf met de suggesties die Google gaf.

![google-suggesties](https://user-images.githubusercontent.com/26331947/204914676-8ef27578-4964-4644-a106-56483627e4ee.jpg)

Inmiddels begon mijn interesse in Python te groeien en zag ik een super tof script van Michael Van Den Reym, namelijk het ophalen van de suggesties met een script. Het originele Google Colab is hier te vinden. Het script haalt de zoekwoorden + alle mogelijke letters door Google, clustert de zoekwoorden en zet alles in één dataframe met ‘zoekwoord’ en ‘cluster’ als kolommen.

Hoe tof het script ook was, het ging voor mij nog niet snel genoeg in Google Colab (sorry Michael). Ik zette het script om naar een ‘offline’ Python script en converteerde dit naar een .command bestand. Op basis van input velden en loops kon ik tijdens het doen van een zoekwoorden onderzoek al een stuk sneller gebruik maken van dit script.

![autosuggestsapp-command](https://user-images.githubusercontent.com/26331947/204914759-d214ff00-6fc6-4f43-a81b-9a7c06235c79.jpg)

Inmiddels had ik een werkend script en maakte ik hier veel gebruik van, super tof! Wel vond ik het mega zonde dat ik nu als enige op werk hiervan gebruik kon maken. Hoe kon ik dit makkelijk delen met mijn collega’s?

Toen is het idee ontstaan voor het maken van een visuele app. Deze hoeft dan enkel gedownload en geïnstalleerd te worden zonder dat iemand Python + een hoop libraries moest installeren en deze makkelijk gebruikt kon worden.

De app is gebouwd met Python in combinatie met Tkinter, een populaire GUI library voor Python. Uiteindelijk zijn deze scripts omgezet naar een app met Py2App (Mac) & Py2Installer (Windows).

Hoe gebruik je deze app?

![autosuggestsapp](https://user-images.githubusercontent.com/26331947/204914786-b2b041d0-eae8-44da-8e92-04b3e9ea6239.jpg)

Zodra je de app in bezit hebt krijg je de optie om maximaal 5 zoekwoorden in te vullen. Vervolgens kun je het script laten starten door op de knop ‘Haal de suggesties op >’ te klikken en begint de magie.

Goed om te weten is dat de app ook gebruikt kan worden om suggesties in andere talen op te halen. Op dit moment ondersteunt de app Nederlands, Engels, Duits en Frans. Meerdere talen kunnen overigens toegevoegd worden mocht je dat willen, stuur me dan even een mail op mail@thijsvanhal.nl.

Het script doet er, afhankelijk van het zoekwoord en het aantal zoekwoorden, ongeveer tussen de 30 seconden en 3 minuten over om te voltooien.

Zodra het script klaar is wordt de status aangepast naar ‘Klaar ✅’ en kun je op de knoppen eronder klikken.

# Wat doet de ‘Download als CSV bestand’ knop?
Dit plaatst een ‘zoekwoorden.csv’ bestand in je downloads map. Dit is bijzonder praktisch, want deze kun je heel snel naar Google Ads uploaden via de planstatistieken. Als je het CSV opent zul je ook zien dat ‘Cluster’ vervangen is voor ‘Ad Group’, exact hoe we het voor Google Ads willen hebben.

Niet alleen zie je dan het zoekvolume per zoekwoord, je kan dit ook per cluster zien! Ga naar prognose, klik op ‘advertentiegroepen’ en sorteer vervolgens op aantal impressies.

![advertentiegroepen](https://user-images.githubusercontent.com/26331947/204914900-91d968ad-d1d3-4757-889e-5ade6a662dc5.jpg)

Impressies staat niet helemaal gelijk aan zoekvolume maar geeft je toch een goed beeld welke clusters veel zoekvolume hebben 😉

# Wat doet de ‘Kopieer naar clipboard’ knop?
Heel simpel, kopieert het dataframe naar je clipboard zodat je deze makkelijk kunt plakken in bijvoorbeeld Excel. Tijdens het doen van een zoekwoorden vind ik dit bijzonder praktisch aangezien ik dan in de brainstorm fase heel makkelijk de lijsten kan kopiëren en in mijn Excel bestand kan zetten zodat ik deze later altijd nog weer terug kan zien!

![zoekwoorden-excel-2048x400](https://user-images.githubusercontent.com/26331947/204914946-7aee9e98-9383-4ad7-b6f5-e18b5970f9fa.jpg)

# De AutoSuggestsApp downloaden
Geïnteresseerd en wil je de app downloaden? Bekijk dan https://www.thijsvanhal.nl/blog/autosuggestsapp/#download
