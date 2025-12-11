import pytest

<<<<<<< HEAD
pytest.main(["tests/","--html=reports/report.html","--self-contained-html","-v"])
=======
# Lista de archivos de pruebas a ejecutar
test_files = [
    "tests/test_login.py",
    "tests/test_inventory.py",
    "tests/test_cart.py",
    "tests/test_cart_json.py"
]

# Argumentos para ejecutar las pruebas: archivos + reporte HTML
pytest_args = test_files + ["--html=report.html","--self-contained-html","-v"]

pytest.main(pytest_args)
>>>>>>> 9922f3a0349ebcd68970d905daf976cabf3eedec
