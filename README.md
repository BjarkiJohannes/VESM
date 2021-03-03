## Verkefni 3

# 3.1

* Hver er munurinn á Arduino Uno og Raspberry Pi, nefndu helstu atriði? Raspberry pi er með 2 input/output pins en Arduino Uno 20 pinna. Pi er 40 sinnum hraðari en Arduino á klukkuhraða. Pi hefur hrút 128000 sinnum meira en Arduino. Svo Raspberry Pi er öflugri en Arduino.
* Hver er munurinn á Arduino Uno og Arduino Nano IoT 33? Helsti munurinn á þessu tvennu er stærðin. Vegna þess að Arduino Uno stærð er tvöföld til nano borð. Svo Uno stjórnir nota meira pláss á kerfinu. Forritun UNO er hægt að gera með USB snúru en Nano notar litla USB snúru.
* Hvenær og afhverju getur það verið gagnlegt að tengja Arduino og Raspberry Pi saman? Komdu með dæmi. Það skemmtilega við Arduino er mikið magn af kóða og skjöldum sem þegar eru til og virka. Vandamálið með Arduino er lítill örgjörvahraði, takmarkað minni osfrv. Svo að nota Arduino og Raspberry Pi geturðu haft það besta frá báðum heimum. Tengdu skynjarana og skjöldinn við Arduino og fáðu Raspberry Pi til að takast á við hluti eins og notendaviðmót, nettengingar, netþjóna o.fl.

# 3.2

* [Kóðin fyrir arduino og raspberry](https://github.com/BjarkiJohannes/VESM/blob/main/hello.py)

* [myndband 3.2](https://streamable.com/fi0aka)

# 3.3

* [raspberry kóði](https://github.com/BjarkiJohannes/VESM/blob/main/33.py)

* [arduino kóði](https://github.com/BjarkiJohannes/VESM/blob/main/33ardu.py)

* [myndband 3.3](https://streamable.com/261ub0)

# 3.4

* [Bluetooth kóði](https://github.com/BjarkiJohannes/VESM/blob/main/bluetooth.py)

* [skjal](https://github.com/BjarkiJohannes/VESM/blob/main/skj)

#  3.8

* 1. Hvað er átt við með samstilltum (e. synchronous) samskiptastaðli? Samstillt samskipti eru þau sem eiga sér stað í rauntíma milli tveggja eða fleiri aðila. Einfaldlega sagt; samstillt samskiptasamskipti eru gagnvirk, „lifandi“ skipti milli fólks.

* 2. Hvað er master-slave samband, útskýrðu útfrá; MISO, MOSI, SCLK og CS/SS? SCLK eða Serial Clock merki er sent frá aðal tækinu. SCLK tilgreinir hvenær gagnabitar verða sendir. 2. MOSI — Master Output Slave Input — sendir gögn frá húsbóndanum til þræla, en MISO — Aðalinntak þrælaútgangur — sendir gögn frá þrælinum til meistarans.

* 3. Engin byrjun og stopp bitar, þannig að hægt er að streyma gögnunum stöðugt án truflana.
Ekkert flókið netfangakerfi eins og I2C.
Hærri gagnaflutningshraði en I2C (næstum tvöfalt hraðar)
Aðskilja MISO og MOSI línur, svo hægt sé að senda og taka við gögnum á sama tíma.

# 3.9 

* [Myndaband 3.9 virkni](https://streamable.com/pbaqxw)

* [Master kóðin](https://github.com/BjarkiJohannes/VESM/blob/main/master.ino)

* [Slave kóðin](https://github.com/BjarkiJohannes/VESM/blob/main/slave.ino)

# 3.10

* [Myndband virkni](https://streamable.com/08cfmf)

* [kóði reciever](https://github.com/BjarkiJohannes/VESM/blob/main/reciever.ino)

* [kóði transmitter](https://github.com/BjarkiJohannes/VESM/blob/main/transmitter.ino)



