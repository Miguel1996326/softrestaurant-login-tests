#Login prueba
import os
import time
import pytest
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
 

class testlogin(unittest.TestCase):
    def setUp(self):
                                    #Configurar el entorno antes de las pruebas
            self.driver=webdriver.Chrome()
            driver = self.driver

    def test_login1(self): #Credenciales no validas
        driver = self.driver 
        driver.get("https://admin-srcloud.dev.national-soft.com")
        driver.maximize_window()
        time.sleep(2)

        # Ingresar datos
        login = driver.find_element(By.ID, "UserNameOrEmail").send_keys('test003@softrestaurant.com')
        contraseña = driver.find_element(By.ID, "Password").send_keys('1235')
        iniciar = driver.find_element(By.ID, "btnSignin").click()
        time.sleep(2)

        try: # Utilizamos el try para revisar los errores que deben aparecer durante la ejecución
            error = driver.find_element(By.ID, "floating-top-right").text
            assert error == "Las credenciales proporcionados no son validos"
            self.driver.get_screenshot_as_file(r"C:\\Users\\PC\\Desktop\\cap\\error_credenciales.png")
            print("Las credenciales proporcionados no son validos  .-.-.-.-CORRECTO.-.-.-.-")
        except NoSuchElementException: #En caso de que no se haya encontrado el mensaje esperado entonces: 
            print("No se encontró el mensaje de error")

         
    def test_login2(self):  # El correo no es válido
        driver = self.driver
        driver.get("https://admin-srcloud.dev.national-soft.com")
        driver.maximize_window()
        time.sleep(2)
        
        # Ingresar datos
        #driver.find_element(By.ID, "UserNameOrEmail").send_keys('test003@softrestaurant.com')
        driver.find_element(By.ID, "").send_keys('12345')
        driver.find_element(By.ID, "btnSignin").click()
        time.sleep(5)

        try:  # Utilizamos el try para revisar los errores que deben aparecer durante la ejecución
            error = driver.find_element(By.XPATH, "(//small[contains(@class,'help-block')])[1]").text
            assert error == "El correo electrónico es requerido"
            self.driver.get_screenshot_as_file(r"C:\\Users\\PC\\Desktop\\cap\\error_correo.png")
            print("El correo electrónico es requerido  .-.-.-.-CORRECTO.-.-.-.-")
        except NoSuchElementException:  # En caso de que no se haya encontrado el mensaje esperado
            print("No se encontró el mensaje de error")

                                     
    def test_login3(self):  # Contraseña vacía
        driver = self.driver
        driver.get("https://admin-srcloud.dev.national-soft.com")
        driver.maximize_window()
        time.sleep(2)

         # Ingresar correo y dejar la contraseña vacía
        driver.find_element(By.ID, "UserNameOrEmail").send_keys('test003@softrestaurant.com')
        driver.find_element(By.ID, "Password").send_keys('')  # Contraseña vacía
        driver.find_element(By.ID, "btnSignin").click()
        time.sleep(5)

        try:
            # Verificar el mensaje de error
            passw = driver.find_element(By.XPATH, "(//small[contains(@class,'help-block')])[3]").text
            # Verificar si el mensaje de error es el esperado
            assert passw == "La contraseña es requerida"
            self.driver.get_screenshot_as_file(r"C:\\Users\\PC\\Desktop\\cap\\error_contraseña.png")
            print("Falta capturar contraseña  .-.-.-.-CORRECTO.-.-.-.-")
        except NoSuchElementException:
            # Si no se encuentra el mensaje de error, se captura un error
            print("No se encontró el mensaje de error de contraseña requerida")


    def test_login4(self):  # Inicio correcto
        driver = self.driver
        driver.get("https://admin-srcloud.dev.national-soft.com")
        driver.maximize_window()
        time.sleep(2)

         # Ingresar correo y dejar la contraseña vacía
        driver.find_element(By.ID, "UserNameOrEmail").send_keys('test003@softrestaurant.com')
        driver.find_element(By.ID, "Password").send_keys('Bismuto01')
        driver.find_element(By.ID, "btnSignin").click()
        time.sleep(5)

        try:
             inicio = driver.find_element(By.XPATH, "(//img[contains(@alt,'Soft Restaurant CLOUD')])[1]")
             inicio.is_enabled
             self.driver.get_screenshot_as_file(r"C:\\Users\\PC\\Desktop\\cap\\inicio_correcto.png")
             print("El inicio de sesion fue exitoso .-.-.-.-CORRECTO.-.-.-.-")
        except NoSuchElementException:
            print("Error al iniciar sesion")

        


    def tearDown(self):
           driver=self.driver
           driver.close()

if __name__ == "__main__":
    unittest.main()