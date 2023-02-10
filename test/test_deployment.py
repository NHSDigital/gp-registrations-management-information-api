"""
Example tests that show all the features of pytest_nhsd_apim.
"""
import json
import pytest
import requests

from pytest_nhsd_apim import pytest_nhsd_apim

def test_ping_endpoint(nhsd_apim_proxy_url):
    """
    Send a request to an open access endpoint.
    """

    # The nhsd_apim_proxy_url will return the URL of the proxy under test.
    # The ping endpoint should have no authentication on it.

    resp = requests.get(nhsd_apim_proxy_url + "/_ping")
    assert resp.status_code == 200
    ping_data = json.loads(resp.text)
    assert "version" in ping_data


def test_status_endpoint(nhsd_apim_proxy_url, status_endpoint_auth_headers):
    """
    Send a request to the _status endpoint, protected by a platform-wide.
    """
    # The status_endpoint_auth_headers fixture returns a dict like
    # {"apikey": "thesecretvalue"} Use it to access your proxy's
    # _status endpoint.

    resp = requests.get(
        nhsd_apim_proxy_url + "/_status", headers=status_endpoint_auth_headers
    )
    status_json = resp.json()
    assert resp.status_code == 200
    assert status_json["status"] == "pass"
