from controlador import *
import time
import os
import subprocess


if __name__ == "__main__":
    cmd_server = subprocess.Popen(
        ["start", "cmd", "/c", "python", "servidor.py"], shell=True
    )
    time.sleep(1)
    app = Controller()
    db = OperacionesDB()
    app.ventana.mainloop()
    cmd_server.kill()
