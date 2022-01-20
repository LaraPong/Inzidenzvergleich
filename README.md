# Inzidenzvergleich - MySQL-Datenbank

1. Für Windows braucht man XAMPP (Apache Webserver), welcher MySQL schon integriert hat. 
Infos hier: https://freiheit.f4.htw-berlin.de/webtech/tools/ 
VORSICHT: Auf Linux oder Mac sind ggfs. schon Webserver vorhanden
(Außerdem können Fehlermeldung bzgl. UAC, Antivirus und Firewall
entstehen. Auf der Installationsseite, findet ihr Infos dazu. Bei mir
hat es aber auch funktioniert, wenn ich die Meldungen ignoriert habe.)

2. In XAMPP Apache und MySQL starten

3. localhost/phpmyadmin im Internetbrowser öffnen

4. links "Neu" -> Datenbankname "inzidenzen", Kollation: utf8mb4_general_ci (schon voreingestellt) -> "Anlegen"

5. Datei inzidenzen_StandYYYYMMTT.sql aus Slack herunterladen

6. in phpMyAdmin Datenbank inzidenzen auswählen und auf "Importieren" klicken

7. Datei auswählen -> inzidenzen_StandYYYYMMTT.sql hochladen -> Zeichencodierung utf-8 (vorausgewählt) -> Ok
=> Datei mit den Städte-Tabellen wird in der Datenbank angelegt

8. In Eingabekonsole pip install mysql.connector eingeben

9. Das Jupyter Notebook mit dem Datenbankcode ist in meinem GitHub-Branch mit dem Namen Notebook_Projekt_Thoughtworks_Datenbank
-> Zelle vier (Verbindung mit Datenbank) kontrollieren, ob user und password zu deinen Einstellungen passen
-> sobald man alle Zellen nacheinander(!) ausführt, befüllt sich die Datenbank mit den aktuellen Werten
