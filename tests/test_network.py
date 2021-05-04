import pytest
import requests
import requests_mock
from page_loader import text
from page_loader import error


STATUS_BC = [400 + x for x in range(18)]
STATUS_BS = [500 + x for x in range(6)]
TEST_LINK = 'http://test.com'


@pytest.mark.parametrize("status", STATUS_BC + STATUS_BS)
def test_response(status):
    """Testing 3xx response.
    Args:
        url : (str) test URL
    """
    with pytest.raises(error.Error):
        with requests_mock.Mocker() as m:
            m.get(TEST_LINK, status_code=status)
            text.get(TEST_LINK)