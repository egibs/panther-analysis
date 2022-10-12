from typing import Iterable

from panther_greynoise_helpers import (
    GreyNoiseAdvanced,
    GreyNoiseBasic,
    PantherIncorrectIPAddressMethodException
)



test_data_basic_list = [(
    {
        "ip_address": "2.2.2.2",
        "request_user":
        "test","request_time":
        "time","p_enrichment": {
            "greynoise_noise_basic": {
                "p_any_ip_addresses": [
                    "8.8.8.8",
                    "1.1.1.1",
                    "localhost",
                    "2.3.4.5",
                ],
            }
        }
    }
)]

test_data_basic_str = [(
    {
        "ip_address": "2.2.2.2",
        "request_user": "test",
        "request_time": "time",
        "p_enrichment": {
            "greynoise_noise_basic": {
                "p_any_ip_addresses": {
                    "actor": "unknown", "ip": "8.8.8.8","classification": "unknown"
                },
            }
        }
    }
)]

test_data_advanced_list = [(
    {
        "ip_address": "2.2.2.2",
        "request_user": "test",
        "request_time": "time",
        "p_enrichment": {
            "greynoise_noise_advanced": {
                "p_any_ip_addresses": [
                    {"actor": "unknown", "ip": "8.8.8.8","classification": "unknown"},
                ],
            }
        }
    }
)]
test_data_advanced_str = [(
    {
        "ip_address": "2.2.2.2",
        "request_user": "test",
        "request_time": "time",
        "p_enrichment": {
            "greynoise_noise_advanced": {
                "p_any_ip_addresses": {
                    "actor": "unknown", "ip": "8.8.8.8","classification": "unknown"
                },
            }
        }
    }
)]

test_data_basic_ip = [(
    {
        "ip_address": "2.2.2.2",
        "request_user": "test",
        "request_time": "time",
        "p_enrichment": {
            "greynoise_noise_basic": {
                "p_any_ip_address": {
                    "ip": "1.2.3.4.5"
                },
            }
        }
    }
)]

test_data_basic_ips = [(
    {
        "ip_address": "2.2.2.2",
        "request_user": "test",
        "request_time": "time",
        "p_enrichment": {
            "greynoise_noise_basic": {
                "p_any_ip_addresses": [
                    "1.2.3.4",
                    "0.6.5.4",
                    "9.8.7.6",
                ]
            }
        }
    }
)]

test_data_basic_none = [(
    {
        "ip_address": "2.2.2.2",
        "request_user": "test",
        "request_time": "time",
        "p_enrichment": {
            "greynoise_noise_basic": {
                "p_any_ip_address": {

                },
            }
        }
    }
)]

test_data_adv_ip = [(
    {
        "ip_address": "2.2.2.2",
        "request_user": "test",
        "request_time": "time",
        "p_enrichment": {
            "greynoise_noise_basic": {
                "p_any_ip_address": {
                    "ip": "1.2.3.4.5"
                },
            }
        }
    }
)]

test_data_adv_ips = [(
    {
        "ip_address": "2.2.2.2",
        "request_user": "test",
        "request_time": "time",
        "p_enrichment": {
            "greynoise_noise_basic": {
                "p_any_ip_addresses": [
                    "1.2.3.4",
                    "0.6.5.4",
                    "9.8.7.6",
                ]
            }
        }
    }
)]

test_data_adv_none = [(
    {
        "ip_address": "2.2.2.2",
        "request_user": "test",
        "request_time": "time",
        "p_enrichment": {
            "greynoise_noise_basic": {
                "p_any_ip_address": {

                },
            }
        }
    }
)]

def cast_test_data(data):
    return ImmutableCaseInsensitiveDict(data)

@pytest.mark.parametrize("data", test_data_basic_list)
def test_greynoise_basic_addresses(data):
    data = cast_test_data(data)
    noise = GreyNoiseBasic(data)
    try:
        noise.ip_address("p_any_ip_addresses")
    except PantherIncorrectIPAddressMethodException:
        pass
    ip_list = noise.ip_addresses("p_any_ip_addresses")
    assert isinstance(ip_list, Iterable)

    ctx = noise.context('p_any_ip_addresses')
    assert 'IPs' in ctx.keys()

@pytest.mark.parametrize("data", test_data_basic_str)
def test_greynoise_basic_address(data):
    data = cast_test_data(data)
    noise = GreyNoiseBasic(data)
    try:
        noise.ip_addresses("p_any_ip_addresses")
    except PantherIncorrectIPAddressMethodException:
        pass

    ip_str = noise.ip_address("p_any_ip_addresses")
    assert isinstance(ip_str, str)

    ctx = noise.context('p_any_ip_addresses')
    assert 'IP' in ctx.keys()

@pytest.mark.parametrize("data", test_data_advanced_list)
def test_greynoise_advanced_addresses(data):
    data = cast_test_data(data)
    noise = GreyNoiseAdvanced(data)
    try:
        noise.ip_address("p_any_ip_addresses")
    except PantherIncorrectIPAddressMethodException:
        pass

    ip_list = noise.ip_addresses("p_any_ip_addresses")
    assert isinstance(ip_list, ImmutableList)

    ctx = noise.context('p_any_ip_addresses')
    assert 'IPs' in ctx.keys()

@pytest.mark.parametrize("data", test_data_advanced_str)
def test_greynoise_advanced_address(data):
    data = cast_test_data(data)
    noise = GreyNoiseAdvanced(data)
    try:
        noise.ip_addresses("p_any_ip_addresses")
    except PantherIncorrectIPAddressMethodException:
        pass

    ip_str = noise.ip_address("p_any_ip_addresses")
    assert isinstance(ip_str, str)

    ctx = noise.context('p_any_ip_addresses')
    assert 'IP' in ctx.keys()

@pytest.mark.parametrize("data", test_data_basic_ip)
def test_greynoise_basic_ip(data):
    data = cast_test_data(data)
    noise = GreyNoiseBasic(data)

    ip_none_basic = noise.ip_address("p_any_ip_address")
    assert isinstance(ip_none_basic, str)


@pytest.mark.parametrize("data", test_data_basic_none)
def test_greynoise_basic_none(data):
    data = cast_test_data(data)
    noise = GreyNoiseBasic(data)

    ip_none_basic = noise.ip_address("p_any_ip_address")
    assert ip_none_basic is None

    ips_none_basic = noise.ip_addresses("p_any_ip_addresses")
    assert ips_none_basic is None

@pytest.mark.parametrize("data", test_data_adv_ip)
def test_greynoise_adv_ip(data):
    data = cast_test_data(data)
    adv = GreyNoiseAdvanced(data)

    ip_none_adv = adv.ip_address("p_any_ip_address")
    assert ip_none_adv is None

    ips_none_adv = adv.ip_addresses("p_any_ip_address")
    assert ips_none_adv is None


@pytest.mark.parametrize("data", test_data_adv_none)
def test_greynoise_adv_none(data):
    data = cast_test_data(data)
    adv = GreyNoiseAdvanced(data)

    ip_none_adv = adv.ip_address("p_any_ip_address")
    assert ip_none_adv is None

    ips_none_adv = adv.ip_addresses("p_any_ip_addresses")
    assert ips_none_adv is None