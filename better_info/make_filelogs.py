from datetime import datetime

class SaveInfoLogs:
    def __init__(self, file_name):
        self.hoy = datetime.today().strftime("%d-%m-%Y")
        self.file_name = f"{file_name} {self.hoy}.log".replace("-","")
    
    def tabs_count(self,tabs):
        return "\t" * tabs
    
    def mk_file(self, msg):
        hoy = datetime.today().strftime("%d-%m-%Y/%H:%M")
        file = open(self.file_name, "a",-1,"utf-8")
        file.write(f"[{hoy}]\t{msg}\n")
        file.close()
    
    def exec(self, msg, tabs=0):
        tb = self.tabs_count(tabs)
        self.mk_file(f"{tb}[+] Log: {msg}")
    
    def doing(self, msg, tabs=1):
        tb = self.tabs_count(tabs)
        self.mk_file(f"{tb}[+] Succes: {msg}")

    def warning(self, msg, tabs=1):
        tb = self.tabs_count(tabs)
        self.mk_file(f"{tb}[!] Warning: {msg}")

    def problem(self, msg, tabs=1):
        tb = self.tabs_count(tabs)
        self.mk_file(f"{tb}[X] Error: {msg}")

    def info(self, msg, tabs=2):
        tb = self.tabs_count(tabs)
        self.mk_file(f"{tb}[i] Info: {msg}") 