from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from utils.screenshot import take_screenshot

# --- KONFIGURASI ---
CHROMEDRIVER_PATH = r"C:\chromedriver\chromedriver.exe"

URL_LOGIN = "https://simkuliah.usk.ac.id/index.php/login"
URL_ABSEN = "https://simkuliah.usk.ac.id/index.php/absensi"
URL_LOGOUT = "https://simkuliah.usk.ac.id/index.php/login/logout"

# --- DATA USER (ISI MANUAL DI SINI) ---
users = [
    ("Nabil Mahbub", "2404111010055", "15927386"),
    ("Muhammad Afzalul Affan", "2404108010067", "48159367"),
    ("Luna Selviana","2404106010001","luna181920"),
    ("Naufal Aziz","2406102010046","24139758"),
    ("Febrilia Ananda Putri","2404106010070","febri070"),
    ("Adrian Rezky Duana ","Rezky","Alish@275"),
    ("balqis athira djumayardi ","2406104030044","58674231"),
    ("Muhammad Aidil Fashsha","2404111010045","56378941"),
]

# --- SETUP CHROME DRIVER ---
# chrome_service = Service()  # Hapus baris ini
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

def login(driver, nama, username, password):
    try:
        driver.get(URL_LOGIN)
        time.sleep(2)
        take_screenshot(driver, f"{nama}_login_page.png")
        driver.find_element(By.XPATH, "//input[@placeholder='NIP/NPM']").send_keys(username)
        driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(password)
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)
        take_screenshot(driver, f"{nama}_post_login.png")
        if "login" in driver.current_url.lower():
            print(f"❌ Login gagal: {nama}")
            return False
        print(f"✅ Login berhasil: {nama}")
        return True
    except Exception as e:
        print(f"❌ Login gagal: {nama} - {e}")
        return False

def absen(driver, nama):
    try:
        driver.get(URL_ABSEN)
        time.sleep(1)
        take_screenshot(driver, f"{nama}_absen_page.png")
        driver.find_element(By.XPATH, "//button[contains(.,'Konfirmasi Kehadiran')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[contains(.,'Konfirmasi')]").click()
        time.sleep(2)
        print(f"🟢 Absen sukses: {nama}")
    except Exception as e:
        print(f"🔴 Gagal absen: {nama} - {e}")
    finally:
        driver.get(URL_LOGOUT)
        time.sleep(1)

def main():
    driver = webdriver.Chrome(options=chrome_options)  # Hapus argumen service
    driver.set_window_size(1280, 800)
    try:
        for nama, username, password in users:
            if login(driver, nama, username, password):
                absen(driver, nama)
    finally:
        driver.quit()
        print("✅ Proses selesai dan browser ditutup.")

if __name__ == "__main__":
    main()