from selenium import webdriver
import os
from selenium.webdriver.chrome.options import Options
from colorama import Fore, init
import sys
import time
init()

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('window-size=1920x1080')
driver = webdriver.Chrome(chrome_options=chrome_options)
driverdni = webdriver.Chrome(chrome_options=chrome_options)
os.system("cls")
#driver = webdriver.Chrome()
#driverdni = webdriver.Chrome()



urlname = "https://eldni.com/index.php/pe/buscar-por-nombres"

driver.get(urlname)




def text(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(10. / 100)

def home():
    time.sleep(2.5)
    os.system("cls")
    text(Fore.YELLOW+"Bienvenido al programa de WebScraping, automatizamos el uso de herramientas para mejorar vidas y notas\n"+Fore.RESET)
    print("""
          [1] Busqueda por dni
          [2] Busqueda por nombres
          """)
    var = input("Tipo de busqueda: ")
    if var == "1":
        dni()
    elif var == "2":
        names()
    else:
        text("Error de entrada...")
    
    



def dni():
    urldni = "https://eldni.com/index.php/pe/buscar-por-dni"
    
    driverdni.get(urldni)
    #coord = driverdni.find_element_by_xpath("//button")
    #coord.click()
#################################################################
#POR DNI
    dni = driverdni.find_element_by_id("dni")
    dnisend = input(Fore.YELLOW+"Ingrese DNI: "+Fore.RESET)
    dni.send_keys(dnisend)
    datos = driverdni.find_element_by_xpath("//*[@class='btn btn-success']")
    datos.click()
    bodysss = driverdni.find_element_by_xpath("//*[@class='column col-md-12']")
    #tr = body.find_element_by_xpath("./*/th")

    print(Fore.YELLOW+str(bodysss.text)+Fore.RESET)
    dni()
##############################################################3###
#POR NOMBRES
def names():
    
        
    name = driver.find_element_by_id("nombres")
    apellido_p = driver.find_element_by_id("apellido_p")
    apellido_m = driver.find_element_by_id("apellido_m")

    nameSend = input(Fore.YELLOW+"Ingrese solo nombres(ejm: maria alejandra):")
    apellidoPSend = input("Ingrese Apellido Paterno: ")
    apellidoMSend = input("Ingrese Apellido Materno: "+Fore.RESET)

    name.send_keys(nameSend)
    apellido_p.send_keys(apellidoPSend)
    apellido_m.send_keys(apellidoMSend)

    dat = driver.find_element_by_tag_name("button")
    dat.click()
    id = "column-center"
    table = driver.find_element_by_id(id)
    tr = table.find_element_by_xpath("//thead")
    td = table.find_element_by_xpath("//tbody")
    
    print ("\n"+Fore.YELLOW+str(tr.text)+Fore.RESET)
    print (Fore.YELLOW+str(td.text+Fore.RESET+"\n"))
    
    names()


home()

#classe = driver.find_elemet_by_class_name("table table-striped table-scroll")
#print(classe.text)