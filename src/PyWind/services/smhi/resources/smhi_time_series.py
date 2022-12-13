from .smhi_parameter import SmhiParameter


class SmhiTimeSeries:
    def __init__(self, valid_time, parameters):
        self.valid_time: str = valid_time
        self.parameters: list[SmhiParameter] = parameters
        return
