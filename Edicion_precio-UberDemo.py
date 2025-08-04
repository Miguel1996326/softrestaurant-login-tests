import unittest
import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

@allure.feature("Gestión de productos")
class TestProducto(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://appmanager.softrestaurant.com/Authentication/Account/Login?token=NzAyNDg2NzYtMUU5OC00REVDLTk3NEMtQjI0RTAxMjk5RENF&companyId=5C540156-265F-430B-8637-B08B0150C1B5&applicationId=6C26ACCA-5764-4BB4-9140-A9E2F5766929")
        time.sleep(2)

    @allure.story("Caso 1 - Editar producto existente")
    def test_01_editar_producto(self):
        driver = self.driver
        wait = self.wait

        with allure.step("Abrir filtros"):
            filtros_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[span[text()="Filtros"]]')))
            filtros_btn.click()
            time.sleep(2)
            allure.attach(driver.get_screenshot_as_png(), name="Abrir_filtros", attachment_type=allure.attachment_type.PNG)

        with allure.step("Aplicar filtros de búsqueda"):
            Select(driver.find_element(By.ID, "Visibility")).select_by_visible_text("Todos")
            Select(driver.find_element(By.ID, "Category")).select_by_visible_text("Bebidas [00002]")
            Select(driver.find_element(By.ID, "Group")).select_by_visible_text("Todos")
            time.sleep(2)
            allure.attach(driver.get_screenshot_as_png(), name="Filtros_aplicados", attachment_type=allure.attachment_type.PNG)

        with allure.step("Editar precio del producto"):
            editar_icono = wait.until(EC.element_to_be_clickable((By.XPATH, '//i[contains(@class, "fe-edit")]')))
            editar_icono.click()
            time.sleep(2)

            price_input = wait.until(EC.element_to_be_clickable((By.ID, "Price")))
            price_input.click()
            time.sleep(1)
            price_input.send_keys(Keys.CONTROL, "a", Keys.BACKSPACE)
            price_input.send_keys("55.00")
            price_input.send_keys(Keys.TAB)
            time.sleep(1)
            allure.attach(driver.get_screenshot_as_png(), name="Editar_precio", attachment_type=allure.attachment_type.PNG)

        with allure.step("Editar modificadores"):
            driver.find_element(By.XPATH, '//button[normalize-space()="Modificadores"]').click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//button[normalize-space()="SABOR"]').click()
            time.sleep(2)

            editar_mod_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='btnEditModifier pointer me-1']")))
            editar_mod_btn.click()
            time.sleep(2)

            modif_input = wait.until(EC.element_to_be_clickable((By.ID, "modifierPrice")))
            modif_input.click()
            modif_input.send_keys(Keys.CONTROL, "a", Keys.BACKSPACE)
            modif_input.send_keys("5.10")
            modif_input.send_keys(Keys.TAB)
            time.sleep(1)

            allure.attach(driver.get_screenshot_as_png(), name="Editar_modificador", attachment_type=allure.attachment_type.PNG)

            guardar_mod_btn = driver.find_element(By.XPATH, "//form[@id='form_UpdateModifier']//button[contains(., 'Guardar')]")
            guardar_mod_btn.click()
            time.sleep(3)

        with allure.step("Guardar cambios generales"):
            driver.find_element(By.ID, "SaveProductButton").click()
            time.sleep(3)
            allure.attach(driver.get_screenshot_as_png(), name="Guardar_producto", attachment_type=allure.attachment_type.PNG)

    @allure.story("Caso 2 - Actualizar catálogo de SR")
    def test_02_actualizar_catalogo(self):
        driver = self.driver
        wait = self.wait

        with allure.step("Actualizar catálogo"):
            button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[contains(text(), 'Actualizar catálogo')]]")))
            button.click()
            time.sleep(7)
            allure.attach(driver.get_screenshot_as_png(), name="Actualizar_catalogo", attachment_type=allure.attachment_type.PNG)

    @allure.story("Caso 3 - Subir productos a Uber")
    def test_03_subir_producto(self):
        driver = self.driver
        wait = self.wait

        with allure.step("Subir productos a UBER"):
            upload_icon = wait.until(EC.element_to_be_clickable((By.XPATH, "//i[contains(@class, 'fe-upload')]")))
            upload_icon.click()
            time.sleep(7)
            allure.attach(driver.get_screenshot_as_png(), name="Subir_a_uber", attachment_type=allure.attachment_type.PNG)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestProducto("test_01_editar_producto"))
    suite.addTest(TestProducto("test_02_actualizar_catalogo"))
    suite.addTest(TestProducto("test_03_subir_producto"))

    runner = unittest.TextTestRunner()
    runner.run(suite)
