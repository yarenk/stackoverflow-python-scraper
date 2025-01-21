from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

try:
    # Chrome options ayarları
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    
    # Chrome servisini başlat
    service = Service()
    
    # Tarayıcı başlatma
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # TikTok sayfasına git
    driver.get("https://www.tiktok.com/@papayaho.cat")
    
    # Sayfanın yüklenmesini bekle (maksimum 10 saniye)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    
    # HTML içeriğini parse et
    soup = BeautifulSoup(driver.page_source, "html.parser")
    
    # İçeriği yazdır
    print(soup.prettify())

except Exception as e:
    print(f"Bir hata oluştu: {str(e)}")

finally:
    # Tarayıcıyı kapat
    if 'driver' in locals():
        driver.quit()