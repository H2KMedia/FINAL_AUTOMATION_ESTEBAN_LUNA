from selenium.webdriver.common.by import By
from selenium import webdriver
<<<<<<< HEAD
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
import time
import pytest
=======
import pytest

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
>>>>>>> 9922f3a0349ebcd68970d905daf976cabf3eedec

@pytest.mark.parametrize("usuario,password",[("standard_user","secret_sauce")])
def test_cart(login_in_driver,usuario,password):
    try:
        driver = login_in_driver
<<<<<<< HEAD
        
        LoginPage(driver).login_completo(usuario,password)

=======
>>>>>>> 9922f3a0349ebcd68970d905daf976cabf3eedec
        inventory_page = InventoryPage(driver)

        # Agregar al carrito el producto
        inventory_page.agregar_primer_producto()

        # Abrir el carrito
        inventory_page.abrir_carrito()

        # Validar el producto
        cartPage = CartPage(driver)
        
        productos_en_carrito = cartPage.obtener_productos_carrito()
<<<<<<< HEAD
        assert len(productos_en_carrito) == 50
        #assert False, "Fallo de prueba forzado"

    except Exception as e:
        print(f"Error en test_cart: {e}")
        raise
=======
        assert len(productos_en_carrito) == 1

    except Exception as e:
        print(f"Error en test_cart: {e}")
        raise
    finally:
        driver.quit()
>>>>>>> 9922f3a0349ebcd68970d905daf976cabf3eedec
