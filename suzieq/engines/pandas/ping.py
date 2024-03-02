from suzieq.engines.pandas.engineobj import SqPandasEngine


class PingObj(SqPandasEngine):
    """Backend class to handle manipulating PING table with pandas"""

    @staticmethod
    def table_name():
        """Table name"""
        return 'ping'

    def get(self, **kwargs):
        view = kwargs.get('view', self.iobj.view)
        columns = kwargs.pop('columns', ['default'])
        user_query = kwargs.pop('query_str', '')
        device_name = kwargs.pop('device_name', '')
        status = kwargs.pop('status', '')
        transport_type = kwargs.get('transport_type', '')
        device_type = kwargs.get('device_type', '')

        addnl_fields = []
        fields = self.schema.get_display_fields(columns)
        self._add_active_to_fields(view, fields, addnl_fields)

        user_query_cols = self._get_user_query_cols(user_query)
        addnl_fields += [x for x in user_query_cols if x not in addnl_fields]

        df = super().get(addnl_fields=addnl_fields, columns=fields, **kwargs)

        if device_name:
            df = df[df['deviceName'] == device_name]

        if status:
            df = df[df['status'] == status]

        if transport_type:
            df = df[df['transportType'] == transport_type]

        if device_type:
            df = df[df['deviceType'] == device_type]

        return df[fields]

    def summarize(self, **kwargs):

        self._init_summarize(**kwargs)
        if self.summary_df.empty:
            return self.summary_df

        # todo not finished
        return self.summary_df

