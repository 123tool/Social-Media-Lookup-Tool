import requests
from config import HEADERS

class WhatsAppChecker:
    def __init__(self, phone_number):
        """
        Format nomor harus internasional tanpa tanda '+' atau Spasi. Contoh: 628123456789
        """
        self.phone = phone_number.replace("+", "").replace(" ", "").replace("-", "")
        
    def check_wa_link(self):
        """
        Memeriksa validitas nomor via WhatsApp API publik
        """
        url = f"https://api.whatsapp.com/send/?phone={self.phone}&text=&type=phone_number&app_absent=0"
        try:
            response = requests.get(url, headers=HEADERS, timeout=10)
            if response.status_code == 200 and 'action-button' in response.text:
                return {
                    "status": "Aktif / Terdaftar",
                    "wa_link": f"https://wa.me/{self.phone}"
                }
            else:
                return {"status": "Tidak Terdeteksi/Private", "wa_link": None}
        except Exception as e:
            return {"status": f"Error: {str(e)}", "wa_link": None}
