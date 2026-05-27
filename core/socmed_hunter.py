import requests
import urllib.parse
from bs4 import BeautifulSoup
from config import HEADERS

class SocmedHunter:
    def __init__(self, target_name):
        """
        target_name: Nama atau username yang didapatkan dari hasil enrichment/input manual
        """
        self.target_name = target_name

    def hunt_instagram(self):
        """
        Melakukan Google Dorking khusus untuk mencari profil Instagram
        """
        query = f"site:instagram.com \"{self.target_name}\""
        url = f"https://www.google.com/search?q={urllib.parse.quote(query)}"
        results = []

        try:
            response = requests.get(url, headers=HEADERS, timeout=10)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                # Mencari link hasil pencarian Google
                for g in soup.find_all('div', class_='yuRUbf'):
                    a_tag = g.find('a')
                    if a_tag and 'instagram.com/' in a_tag['href']:
                        title = g.find('h3').text if g.find('h3') else "Instagram Profile"
                        link = a_tag['href']
                        # Filter agar tidak mengambil link login/register/tags
                        if not any(x in link for x in ['/p/', '/explore/', '/tags/', '/login']):
                            results.append({"title": title, "link": link})
            return results
        except Exception as e:
            return [{"error": f"Gagal crawling Instagram: {str(e)}"}]

    def hunt_facebook(self):
        """
        Melakukan Google Dorking khusus untuk mencari profil Facebook
        """
        query = f"site:facebook.com \"{self.target_name}\""
        url = f"https://www.google.com/search?q={urllib.parse.quote(query)}"
        results = []

        try:
            response = requests.get(url, headers=HEADERS, timeout=10)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                for g in soup.find_all('div', class_='yuRUbf'):
                    a_tag = g.find('a')
                    if a_tag and 'facebook.com/' in a_tag['href']:
                        title = g.find('h3').text if g.find('h3') else "Facebook Profile"
                        link = a_tag['href']
                        # Filter tautan yang tidak relevan
                        if not any(x in link for x in ['/sharer/', '/recover/', '/pages/']):
                            results.append({"title": title, "link": link})
            return results
        except Exception as e:
            return [{"error": f"Gagal crawling Facebook: {str(e)}"}]
