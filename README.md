# Raspberry_Pi
Temperaturanzeige des Prozessors auf LCD 1602

<img src="bild/LCD_1602_Steckplatine.png" width="400">
<h4>Programmbeschreibung</h4>
<p>Dieser Python-Code dient dazu, die aktuelle CPU-Temperatur eines Computers zu ermitteln und anzuzeigen sowie die aktuelle Uhrzeit darzustellen. Hierbei wird ein LCD-Display verwendet, das über eine I2C-Schnittstelle angeschlossen ist. Der Code nutzt die Bibliothek RPLCD, die speziell für LCD-Displays mit I2C-Schnittstelle geeignet ist.
Im ersten Schritt wird die RPLCD-Bibliothek importiert, und das LCD-Display wird mit der Adresse 0x27 initialisiert. Diese Adresse ist standardmäßig für viele I2C-LCD-Module vorgesehen. Anschließend definiert der Code zwei Hauptfunktionen: getcputemp() und gettimenow().</p>
<p>Die Funktion getcputemp() liest die CPU-Temperatur direkt aus einer Systemdatei, die sich unter /sys/class/thermal/thermal_zone0/temp befindet. Diese Datei enthält die Temperatur in Milligraden Celsius. Um die Temperatur lesbar darzustellen, wird sie durch 1000 geteilt und formatiert, sodass sie in Grad Celsius erscheint. Diese Funktion gibt dann einen String wie "CPU: 45.50 C " zurück, der die Temperatur anzeigt.</p>
<p>Die Funktion gettimenow() dient dazu, die aktuelle Systemzeit im Format Stunden und Minuten abzurufen. Hierbei wird die Funktion strftime() genutzt, um die aktuelle Zeit als String zu formatieren.</p>
<p>Im Hauptteil des Codes wird eine Endlosschleife (while-Schleife) definiert, die die Temperatur und die Uhrzeit kontinuierlich auf dem LCD-Display anzeigt. Zuerst wird das Display mit lcd1602.clear() gelöscht, um alte Daten zu entfernen. Danach wird der Cursor auf die erste Zeile gesetzt, und die CPU-Temperatur wird dort angezeigt. In der zweiten Zeile wird die aktuelle Uhrzeit dargestellt.</p>
<p>Der sleep(10)-Befehl sorgt dafür, dass die Anzeige alle 10 Sekunden aktualisiert wird.</p>
<p>Der try-except-Block fängt eine Tastaturunterbrechung ab (wenn man z. B. Strg+C drückt) und löscht das Display, bevor das Programm endet, um eine saubere Beendigung zu gewährleisten.</p>
