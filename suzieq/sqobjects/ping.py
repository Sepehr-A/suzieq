from suzieq.sqobjects.basicobj import SqObject


class PingObj(SqObject):
    """The object providing access to the ping table"""

    def __init__(self, **kwargs):
        super().__init__(table='ping', **kwargs)
        self._valid_get_args = ['namespace', 'hostname', 'columns', 'query_str',
                                "device_type", "device_name", "target", "status", "transport_type"]
