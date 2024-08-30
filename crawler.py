import requests
from bs4 import BeautifulSoup
import sys
import os
from markdownify import markdownify as md

def fetch_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        # HTML-Inhalt der Seite parsen
        soup = BeautifulSoup(response.content, 'html.parser')

        # Beispiel für das Extrahieren von Blogeinträgen
        # Passen Sie diesen Selektor an die tatsächliche Struktur der Seite an
        content = soup.find('article')  # Verwenden Sie den richtigen Tag oder die richtige Klasse

        # Überprüfen, ob Inhalte gefunden wurden
        if not content:
            print(f"Keine Blogeinträge auf der Seite {url} gefunden.")
            return None

        # Den HTML-Inhalt in Markdown umwandeln
        text_content = md(str(content))

        return text_content
    except requests.exceptions.RequestException as e:
        print(f"Fehler beim Abrufen der Seite {url}: {e}")
    return None

def save_to_markdown(url, content):
    try:
        if not content:
            print(f"Kein Inhalt für {url} zum Speichern.")
            return

        # Konvertiert die URL in einen gültigen Dateinamen
        filename = "results/" + url.replace("https://", "").replace("http://", "").replace("/", "_") + ".md"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Inhalt von {url} gespeichert in {filename}")
    except IOError as e:
        print(f"Fehler beim Speichern der Datei {filename}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Verwendung: python crawler.py <Dateiname mit URLs>")
        sys.exit(1)

    urls_file = sys.argv[1]

    if not os.path.exists(urls_file):
        print(f"Datei {urls_file} nicht gefunden!")
        sys.exit(1)

    # URLs aus der Datei lesen
    with open(urls_file, 'r') as f:
        urls = [line.strip() for line in f.readlines()]

    for url in urls:
        print(f"Verarbeite URL: {url}")
        content = fetch_content(url)
        if content:
            save_to_markdown(url, content)
