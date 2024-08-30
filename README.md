# Sitemap to Markdown Webcrawler

Dieses Projekt enthält zwei Python-Skripte (`sitemap.py` und `crawler.py`), die zusammenarbeiten, um eine Sitemap-XML-Datei von einer Website zu analysieren, alle enthaltenen URLs zu extrahieren und die Inhalte dieser Seiten als Markdown-Dateien zu speichern.

## Anforderungen

Stellen Sie sicher, dass Sie Python 3.x installiert haben. Außerdem benötigen Sie die folgenden Python-Bibliotheken:

- `requests` — für HTTP-Anfragen
- `beautifulsoup4` — für die HTML-Analyse
- `markdownify` — für die Konvertierung von HTML zu Markdown

Installieren Sie die benötigten Bibliotheken mit pip:

```bash
pip install requests beautifulsoup4 markdownify
```

Projektstruktur

    sitemap.py: Liest die Sitemap-XML-Datei ein und speichert alle enthaltenen URLs in einer Textdatei.
    crawler.py: Liest die URLs aus der Textdatei, crawlt die Seiten, extrahiert die Inhalte und speichert sie in Markdown-Dateien.

Verwendung
Schritt 1: Sitemap-URLs extrahieren

Verwenden Sie das Skript sitemap.py, um alle URLs aus einer Sitemap-XML-Datei zu extrahieren und in einer Textdatei zu speichern.

Führen Sie das Skript sitemap.py aus:

bash

python sitemap.py <Sitemap-URL>

Ersetzen Sie <Sitemap-URL> durch die URL Ihrer Sitemap, z.B.:

bash

python sitemap.py https://hoch3fotografie.com/post-sitemap.xml

Das Skript erstellt eine Datei sitemap_urls.txt, die alle URLs enthält, die in der Sitemap gefunden wurden.
Schritt 2: Seiteninhalt crawlen und speichern

Verwenden Sie das Skript crawler.py, um die URLs aus sitemap_urls.txt zu lesen, die Seiteninhalte zu crawlen und die Inhalte in Markdown-Dateien zu speichern.

Führen Sie das Skript crawler.py aus:

bash

python crawler.py sitemap_urls.txt

Dieses Skript liest die Datei sitemap_urls.txt, ruft den Inhalt jeder URL ab, konvertiert ihn in Markdown und speichert ihn in einer entsprechenden .md-Datei.
Ausgabe

Für jede URL in der Sitemap wird eine Markdown-Datei mit dem Inhalt der Seite erstellt. Der Name der Datei basiert auf der URL, wobei spezielle Zeichen durch Unterstriche ersetzt werden. Zum Beispiel:

    URL: https://hoch3fotografie.com/blog/landhochzeit-in-aindling
    Datei: hoch3fotografie.com_blog_landhochzeit-in-aindling.md

Fehlerbehandlung

Falls eine Seite nicht abgerufen werden kann oder keine Blogeinträge gefunden werden, gibt das Skript eine entsprechende Fehlermeldung auf der Konsole aus.
Anpassungen

Falls die Struktur der Blogseite nicht dem Standard entspricht, müssen Sie möglicherweise den HTML-Selektor in der Funktion fetch_content in crawler.py anpassen.