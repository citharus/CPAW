from CPAW.models.service import *
from CPAW.models import Miner


def convert_services(client: Client, service_list: dict) -> List[Service]:
    """
    Convert a list with services as dicts into a list with services.
    :param Client client: The client used by the user
    :param dict service_list: The services represented as dicts in a list
    :return: A list of services
    :rtype: list[Service]
    """
    services: List[Service] = []

    for service in service_list:
        if service["name"] == "ssh":
            services.append(SSHService(client, service))
        elif service["name"] == "telnet":
            services.append(TelnetService(client, service))
        elif service["name"] == "portscan":
            services.append(PortscanService(client, service))
        elif service["name"] == "bruteforce":
            services.append(BruteforceService(client, service))
        elif service["name"] == "miner":
            services.append(Miner(client, service))

    return services
