import time
import os
import socket

def main():
    print("Hardware simulator starting...")
    
    # Очікуємо, поки основний додаток буде готовий
    app_host = "app"
    app_port = 5000
    
    ready = False
    while not ready:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((app_host, app_port))
            s.close()
            ready = True
        except:
            print("Waiting for main app to be available...")
            time.sleep(2)
    
    print("Main app is available. Hardware simulator is running.")
    
    # Симуляція роботи апаратного забезпечення
    while True:
        print("Hardware simulator is working...")
        time.sleep(10)

if __name__ == "__main__":
    main()
