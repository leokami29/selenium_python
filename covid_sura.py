from selenium import webdriver
# from selenium.webdriver.common.keys import 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time, json

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

with open("employees.json") as json_file:
    
    data = json.load(json_file)

    for p in data["keys"]:

        # print(p["namepet"] + " is loading!")

        driver.get("https://henry-sanchez.com/gbm/")

        # start = driver.find_element(By.XPATH,  "/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button")
        # start.click()
        time.sleep(3)

        # print(start)

        usuario= driver.find_element(By.NAME, "usuario")
        usuario.send_keys(p["usu"])
        time.sleep(3)
        
        npass = driver.find_element(By.NAME, "clave")
        npass.send_keys(p["pass"])
        time.sleep(3)
        
        buttlogin = driver.find_element(By.CLASS_NAME, "login100-form-btn")
        buttlogin.click()
        
        nuevo = driver.find_element(By.XPATH, "/html/body/div/div/main/div[2]/div[1]/div/a")
        nuevo.click()
        # email = driver.find_element(By.ID, "Email")
        # email.send_keys(p["email"])
        
        # alta = driver.find_element(By.ID, "Alta")
        # alta.send_keys(p["alta"])
        
        # alta = driver.find_element(By.ID, "Sintomas")
        # alta.send_keys(p["sin"])
        
        # agregar = driver.find_element(By.ID, "Agregar")
        # agregar.click()
        time.sleep(3)
        
        
        # Submit = driver.find_element(By.XPATH, "/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input")
        # Submit.click()
        # nextPageBtn = driver.find_element_by_name("data[page3SiAutorizo]")
        # nextPageBtn.click()

        # userId = driver.find_element_by_name("data[identificacion_usuario]")
        # userId.send_keys(p["id"])

        # userName = driver.find_element_by_name("data[nombre_usuario]")
        # userName.send_keys(p["name"])

        # nextPage2Btn = driver.find_element_by_name("data[page1Siguiente]")
        # nextPage2Btn.click()

        # submitBtn = driver.find_element_by_name("data[page2Finalizar]")
        # submitBtn.click()

        # print(p["namepet"] + " is done!")

        time.sleep(3)

driver.close()