import pyautogui as py
import pygetwindow as gw
import subprocess
import time

# Passo 1: Abrir o navegador com o caminho completo do Chrome
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
subprocess.Popen([chrome_path, "--guest"])  # Isso abre o navegador Chrome

# Passo 2: Esperar alguns segundos para a janela abrir completamente
time.sleep(2)

# Passo 3: Encontrar a janela do navegador
windows = gw.getWindowsWithTitle('Chrome')  # Encontre a janela com o nome 'Chrome'

if windows:
    browser_window = windows[0]

    # Passo 4: Redimensionar e reposicionar a janela
    browser_window.moveTo(0, 0)  # Move a janela para a posição (100, 100) na tela
    browser_window.resizeTo(950, 1045)  # Redimensiona a janela para 800x600 pixels

else:
    print("Janela do navegador não encontrada")

py.PAUSE = 1

py.click(402, 67)
py.write('https://github.com/MW-Limah')
py.press('enter')


#       Este código está OK
