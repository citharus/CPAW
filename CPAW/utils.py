from CPAW.models.service import *
from CPAW.models import Miner


def convert_services(client: Client, service_list: List[Dict[str, Union[str, int, bool]]]) -> List[Service]:
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
