import pytest
import pathlib
import time
from selenium import webdriver
from pages.login_page import LoginPage
from selenium.webdriver.chrome.options import Options
<<<<<<< HEAD
from datetime import datetime

target = pathlib.Path("reports/screens")
target.mkdir(parents=True, exist_ok=True)
=======
>>>>>>> 9922f3a0349ebcd68970d905daf976cabf3eedec

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--incognito")
<<<<<<< HEAD
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--headless=new")
    
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
    
@pytest.fixture
def login_in_driver(driver):
    LoginPage(driver).abrir_pagina() 
    return driver    
    
@pytest.fixture
def url_base():
    return "https://reques.in/api/users"

@pytest.fixture
def header_request():
    return {"x-api-key": "reqres-free-v1"}

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when in ("setup","call") and rep.failed:
        driver = item.funcargs.get['driver',None]
        if driver:
            timestamp_comun=datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            timestamp_unix=int(time.time())
            file_name= target / f"{rep.when}_{item.name}_{timestamp_unix}.png"
            driver.save_screenshot(str(file_name))
            
=======

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture
def login_in_driver(driver,usuario,password):
    LoginPage(driver).abrir_pagina().login_completo(usuario,password)
    return driver
>>>>>>> 9922f3a0349ebcd68970d905daf976cabf3eedec
