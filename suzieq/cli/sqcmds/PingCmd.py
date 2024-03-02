from nubia import command
from suzieq.cli.nubia_patch import argument

from suzieq.cli.sqcmds.command import SqTableCommand
from suzieq.sqobjects.ping import PingObj


@command("ping", help="Act on ping data")
@argument("device_name", description="Filter by device name")
@argument("target", description="Filter by target IP/DNS name")
@argument("status", description="Filter by ping status", choices=["Success", "Timeout", "Unreachable"])
@argument("transport_type", description="Filter by transport_type")
@argument("device_type", description="Filter by device_type")

class PingCmd(SqTableCommand):
    """Ping information such as serial number, cable info etc"""

    def __init__(
            self,
            engine: str = "",
            hostname: str = "",
            start_time: str = "",
            end_time: str = "",
            view: str = "",
            namespace: str = "",
            format: str = "",  # pylint: disable=redefined-builtin
            query_str: str = ' ',
            columns: str = "default",
            device_name: str = "",
            target: str = "",  # A string for the IP address or DNS name that was pinged.
            status: str = "",  # the result of the ping ("Success", "Timeout", "Unreachable")
            transport_type: str = "",  # can be derived from the url(e.g., "SSH", "HTTPS")
            device_type: str = "" # the type of device from which the ping was initiated

    ) -> None:
        super().__init__(
            engine=engine,
            hostname=hostname,
            start_time=start_time,
            end_time=end_time,
            view=view,
            namespace=namespace,
            columns=columns,
            format=format,
            query_str=query_str,
            sqobj=PingObj,
        )

        self.lvars = {
            'device_name': device_name,
            'target': target,
            'status': status,
            'transport_type': transport_type,
            'device_type': device_type,
        }
