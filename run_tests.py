import pytest
import pyt

pytest.main(["tests/","--html=reports/report.html","--self-contained-html","-v"])
