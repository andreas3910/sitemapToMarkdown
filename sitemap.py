import requests
import xml.etree.ElementTree as ET
import sys

def read_sitemap(url):
    try:
        # Abrufen der Sitemap-Datei
        response = requests.get(url)
        response.raise_for_status()  # Überprüfen, ob der Abruf erfolgreich war

        # Sitemap-Daten parsen
        sitemap = ET.fromstring(response.content)

        # Extrahieren aller URLs
        urls = [url_element.text for url_element in sitemap.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]

        return urls
    except requests.exceptions.RequestException as e:
        print(f"Fehler beim Abrufen der Sitemap: {e}")
    except ET.ParseError as e:
        print(f"Fehler beim Parsen der Sitemap: {e}")

def save_urls_to_file(urls, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for url in urls:
                f.write(url + "\n")
        print(f"URLs wurden erfolgreich in {filename} gespeichert.")
    except IOError as e:
        print(f"Fehler beim Schreiben in die Datei {filename}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Verwendung: python sitemap.py <Sitemap-URL>")
        sys.exit(1)

    sitemap_url = sys.argv[1]  # Die Sitemap-URL aus dem ersten Parameter lesen
    urls = read_sitemap(sitemap_url)

    if urls:
        print("Gefundene URLs in der Sitemap:")
        for url in urls:
            print(url)
        
        # Speichern der URLs in eine .txt-Datei
        save_urls_to_file(urls, "results/sitemap_urls.txt")
