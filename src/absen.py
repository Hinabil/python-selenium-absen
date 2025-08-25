from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from utils.screenshot import take_screenshot
import pg8000
import os

# --- KONFIGURASI ---
CHROMEDRIVER_PATH = r"C:\chromedriver\chromedriver.exe"

URL_LOGIN = "https://simkuliah.usk.ac.id/index.php/login"
URL_ABSEN = "https://simkuliah.usk.ac.id/index.php/absensi"
URL_LOGOUT = "https://simkuliah.usk.ac.id/index.php/login/logout"


# --- SETUP CHROME DRIVER ---
# chrome_service = Service()  # Hapus baris ini
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

def login(driver, nama, username, password):
    try:
        driver.get(URL_LOGIN)
        time.sleep(2)
        take_screenshot(driver, f"screenshots/{nama}_login_page.png")
        driver.find_element(By.XPATH, "//input[@placeholder='NIP/NPM']").send_keys(username)
        driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(password)
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)
        take_screenshot(driver, f"screenshots/{nama}_post_login.png")
        if "login" in driver.current_url.lower():
            print(f"[FAIL] Login gagal: {nama}")
            return False
        print(f"[OK] Login berhasil: {nama}")
        return True
    except Exception as e:
        print(f"[FAIL] Login gagal: {nama} - {e}")
        return False

def absen(driver, nama):
    try:
        driver.get(URL_ABSEN)
        time.sleep(1)
        take_screenshot(driver, f"screenshots/{nama}_absen_page.png")
        driver.find_element(By.XPATH, "//button[contains(.,'Konfirmasi Kehadiran')]").click()
        time.sleep(1)
        take_screenshot(driver, f"screenshots/{nama}_Konfirmasi_kehadiran.png")
        driver.find_element(By.CSS_SELECTOR, "button.confirm").click()
        time.sleep(2)
        print(f"[ABSEN OK] Absen sukses: {nama}")
        take_screenshot(driver, f"screenshots/{nama}_absen_sukses.png")
    except Exception as e:
        print(f"[ABSEN FAIL] Gagal absen: {nama} - {e}")
        take_screenshot(driver, f"screenshots/{nama}_absen_failed.png")
    finally:
        driver.get(URL_LOGOUT)
        time.sleep(1)

def get_users_from_db():
    #Hanya koneksi saat diperlukan
    try:
        with pg8000.connect(
            user=os.environ["PGUSER"],
            password=os.environ["PGPASSWORD"],
            host=os.environ["PGHOST"],
            database=os.environ["PGDATABASE"],
            ssl_context=True
        ) as conn:
            with conn.cursor() as cur:
                cur.execute('SELECT nama, username, password FROM "data absen"')
                return cur.fetchall()
    except Exception as e:
        print(f"Gagal koneksi ke database: {e}")
        return []
    
def main():
    users = get_users_from_db()
    if not users:
        print("Tidak ada data user ditemukan.")
        return
    
    os.makedirs("screenshots", exist_ok=True)
    for nama, username, password in users:
        driver = webdriver.Chrome(options=chrome_options)
        driver.set_window_size(1280, 800)
        try:
            if login(driver, nama, username, password):
                absen(driver, nama)
        finally:
            driver.quit()
            print(f"[OK] Proses selesai dan browser ditutup untuk {nama}.")

if __name__ == "__main__":
    main()
