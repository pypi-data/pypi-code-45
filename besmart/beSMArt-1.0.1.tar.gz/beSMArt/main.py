import json
import requests

SOME_CONST_I_DONT_KNOW_THE_MEANING = "017A-B33B6D41"

# By `# my device` I marked fields accessible via my device API. Rest of the fields I get from https://github.com/kellerza/pysma
API_FIELDS = {
    "grid_power": "6100_40263F00",  # my device
    "frequency": "6100_00465700",
    "voltage_l1": "6100_00464800",
    "voltage_l2": "6100_00464900",
    "voltage_l3": "6100_00464A00",
    "current_l1": "6100_40465300",
    "current_l2": "6100_40465400",
    "current_l3": "6100_40465500",
    "pv_power": "6100_0046C200",
    "pv_voltage": "6380_40451F00",
    "pv_current": "6380_40452100",
    "pv_gen_meter": "6400_0046C300",
    "total_yield": "6400_00260100",  # my device
    "daily_yield": "6400_00262200",
    "grid_power_supplied": "6100_40463600",  # my device
    "grid_power_absorbed": "6100_40463700",  # my device
    "grid_total_yield": "6400_00462400",
    "grid_total_absorbed": "6400_00462500",  # my device
    "current_consumption": "6100_00543100",
    "total_consumption": "6400_00543A00"
}


def get_data(ip: str) -> dict:
    """
    Download and parse data from SMA API.

    Parameters:
        - ip: str - IP of SMA device
    """
    r = requests.get(f"https://{ip}/dyn/getDashValues.json", verify=False)
    return r.json()["result"][SOME_CONST_I_DONT_KNOW_THE_MEANING]


def get_attribute(data: dict, attribute_name: str):
    """
    Returns attribute value from downloaded data.

    Parameters:
        - data: dict - The result of `get_data` function
        - attribute_name: str - Attribute name from `API_FIELDS`
    """

    try:

        value = data[API_FIELDS[attribute_name]]['1'][0]

        if len(value.keys()) > 1:
            return value
        return value["val"]

    except (KeyError, IndexError):
        return value
