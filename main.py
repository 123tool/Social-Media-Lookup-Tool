import os
import sys
from colorama import init, Fore, Style
import pyfiglet

# Import core modules
from core.wa_checker import WhatsAppChecker
from core.phone_enrich.py import PhoneEnricher if os.path.exists("core/phone_enrich.py") else None
# fallback jika struktur folder langsung dimasukkan
try:
    from core.wa_checker import WhatsAppChecker
    from core.phone_enrich import PhoneEnricher
    from core.socmed_hunter import SocmedHunter
except ImportError:
    print("Pastikan struktur file core/ sudah benar!")
    sys.exit()

# Inisialisasi Colorama untuk Windows/Linux
init(autoreset=True)

def print_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = pyfiglet.figlet_format("SPY-E OSINT", font="slant")
    print(Fore.CYAN + banner)
    print(Fore.GREEN + "==================================================")
    print(Fore.YELLOW + "  Phone Number to Social Media Lookup Tool Pro    ")
    print(Fore.GREEN + "==================================================")
    print()

def main():
    print_banner()
    
    # Input nomor telepon
    phone_input = input(Fore.WHITE + "[-] Masukkan Nomor Telepon (Contoh: 628123xxx): ")
    if not phone_input:
        print(Fore.RED + "[!] Nomor tidak boleh kosong.")
        return

    print(Fore.BLUE + "\n[*] Menjalankan Langkah 1: Validasi WhatsApp...")
    wa = WhatsAppChecker(phone_input)
    wa_res = wa.check_wa_link()
    print(Fore.GREEN + f"[+] Status WA: {wa_res['status']}")
    if wa_res['wa_link']:
        print(Fore.GREEN + f"[+] Tautan Chat: {wa_res['wa_link']}")

    print(Fore.BLUE + "\n[*] Menjalankan Langkah 2: Basic Enrichment & Footprint...")
    enricher = PhoneEnricher(phone_input)
    basic_info = enricher.lookup_numverify()
    if "valid" in basic_info and basic_info["valid"]:
        print(Fore.GREEN + f"[+] Provider: {basic_info.get('carrier')}")
        print(Fore.GREEN + f"[+] Lokasi: {basic_info.get('location')}, {basic_info.get('country_name')}")
    
    enricher.google_search_name()

    print(Fore.YELLOW + "\n[?] Untuk mencari Instagram & Facebook, kita butuh Nama/Username Target.")
    print(Fore.WHITE + "    (Tips: Cek nama target dulu di GetContact / Truecaller Anda)")
    target_name = input(Fore.WHITE + "[-] Masukkan Nama Lengkap / Username Target: ")

    if target_name:
        print(Fore.BLUE + f"\n[*] Menjalankan Langkah 3: Hunting Profile untuk '{target_name}'...")
        hunter = SocmedHunter(target_name)
        
        # Hunt Instagram
        print(Fore.CYAN + "\n[~] Mencari di Instagram...")
        ig_results = hunter.hunt_instagram()
        if ig_results:
            for idx, res in enumerate(ig_results, 1):
                if "error" in res:
                    print(Fore.RED + f"    {res['error']}")
                else:
                    print(Fore.GREEN + f"    [{idx}] {res['title']}")
                    print(Fore.WHITE + f"        Link: {res['link']}")
        else:
            print(Fore.RED + "    [-] Tidak ditemukan profil Instagram publik yang cocok.")

        # Hunt Facebook
        print(Fore.CYAN + "\n[~] Mencari di Facebook...")
        fb_results = hunter.hunt_facebook()
        if fb_results:
            for idx, res in enumerate(fb_results, 1):
                if "error" in res:
                    print(Fore.RED + f"    {res['error']}")
                else:
                    print(Fore.GREEN + f"    [{idx}] {res['title']}")
                    print(Fore.WHITE + f"        Link: {res['link']}")
        else:
            print(Fore.RED + "    [-] Tidak ditemukan profil Facebook publik yang cocok.")
    else:
        print(Fore.RED + "\n[!] Proses pencarian sosmed dibatalkan karena nama kosong.")

    print(Fore.GREEN + "\n=================== PROSES SELESAI ===================")

if __name__ == "__main__":
    main()
