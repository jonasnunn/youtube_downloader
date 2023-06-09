import pytest
from downloader import *

# Test that their are no errors in the file.
def test_everrything():
    assert main() == True

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])