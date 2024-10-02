import sys

class BetterPrints:
    def __init__(self):
        pass
    def tabs_count(self, tabs=0):
        return "\t" * tabs
    def sysprint(self, message=""):
        sys.stdout.write(message)
        sys.stdout.flush()
    def println(self, message=""):
        self.sysprint(f"{message}\n")

class LogPrint(BetterPrints):
    def __init__(self, message=" "):
        self.blanco = chr(27) + "[0;37m"
        self.verde = chr(27) + "[0;32m"
        self.message = message
        self.current_string = ""

    def status(self, message):#Sube
        self.println("\n")
        self.sysprint("\033[F"*2)
        self.sysprint("\033[K") #Limpia la linea
        self.current_string = f"{self.blanco}{self.message}{message}"
        self.sysprint(self.current_string)

    def write(self, message):
        self.println("\033[F")
        self.sysprint("\033[K")
        self.println(f"{self.blanco}{message}")
        self.sysprint(self.current_string)

    def barra(self,iterable, total=None, longitud=100, fill='█', vacío='-', print_end="\r"):
        if total is None:
            total = len(iterable)
        def actualizar_barra(iteracion):
            porcentaje = iteracion / float(total)
            llenado = int(longitud * porcentaje)
            barra = fill * llenado + vacío * (longitud - llenado)
            barra = f'\r{self.blanco}|{barra}| {int(porcentaje * 100)}% {self.verde}{self.message}{self.current_string}'
            self.sysprint("\r\033[K")
            self.sysprint(barra)
        for i, item in enumerate(iterable):
            yield item 
            self.current_string = item
            actualizar_barra(i + 1)
        self.println(print_end)

class ColorPrints(BetterPrints):
    def __init__(self):
        self.verde = chr(27) + "[0;32m"
        self.rojo = chr(27) + "[0;31m"
        self.amarillo = chr(27) + "[0;33m"
        self.azul = chr(27) + "[0;34m"
        self.blanco = chr(27) + "[0;37m"
    
    def red_msg(self,msg):
        out = f"{self.rojo}{msg}"
        return out
    def green_msg(self,msg):
        out = f"{self.verde}{msg}"
        return out
    def yellow_msg(self,msg):
        out = f"{self.amarillo}{msg}"
        return out
    def blue_msg(self,msg):
        out = f"{self.azul}{msg}"
        return out
    def normal_msg(self, msg, tabs=0, prefj=""):
        tb = self.tabs_count(tabs)
        self.println(f"{self.blanco}{tb}{prefj}{msg}")
    
    def succes(self, msg, tabs=0, prefj="Succes: "):
        tb = self.tabs_count(tabs)
        self.println(self.green_msg(f"{tb}[+] {prefj}{msg}"))
    def log(self, msg, tabs=0, prefj="Log: "):
        tb = self.tabs_count(tabs)
        self.println(self.blue_msg(f"{tb}[+] {prefj}{msg}"))
    def warning(self, msg, tabs=0, prefj="Warning: "):
        tb = self.tabs_count(tabs)
        self.println(self.yellow_msg(f"{tb}[!] {prefj}{msg}"))
    def failure(self, msg, tabs=0, prefj="Error: "):
        tb = self.tabs_count(tabs)
        self.println(self.red_msg(f"{tb}[X] {prefj}{msg}"))
    def info(self, msg, tabs=0, prefj="Info: "):
        tb = self.tabs_count(tabs)
        self.println(f"{tb}[i] {prefj}{msg}")