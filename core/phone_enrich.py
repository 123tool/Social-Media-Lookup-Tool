import requests
import json
from config import HEADERS, NUMVERIFY_API_KEY

class PhoneEnricher:
    def __init__(self, phone_number):
        self.phone = phone_number.replace("+", "").replace(" ", "").replace("-", "")

    def lookup_numverify(self):
        """
        Mendapatkan data negara, provider, dan lokasi nomor telepon (Gratis)
        """
        if not NUMVERIFY_API_KEY:
            return {"note": "Numverify API Key kosong, skip basic lookup."}
            
        url = f"http://apilayer.net/api/validate?access_key={NUMVERIFY_API_KEY}&number={self.phone}"
        try:
            res = requests.get(url, timeout=10)
            data = res.json()
            if data.get('valid'):
                return {
                    "valid": data.get("valid"),
                    "local_format": data.get("local_format"),
                    "carrier": data.get("carrier"),
                    "location": data.get("location"),
                    "country_name": data.get("country_name")
                }
        except:
            return {"error": "Gagal terhubung ke Numverify"}
        return {"valid": False}

    def google_search_name(self):
        """
        Mencari nama alternatif atau kebocoran nama nomor telepon di halaman web publik
        """
        query = f'"{self.phone}" OR "{self.phone[:4]}-{self.phone[4:8]}-{self.phone[8:]}"'
        url = f"https://www.google.com/search?q={query}"
        
        try:
            res = requests.get(url, headers=HEADERS, timeout=10)
            # Logika dorking mentah untuk melihat apakah nomor ini pernah dipajang di web/olshop
            if res.status_code == 200:
                return {"info": "Dorking nomor selesai. Lanjut ke pencarian sosmed."}
        except:
            pass
        return {"info": "No public footprint directly from phone number."}
