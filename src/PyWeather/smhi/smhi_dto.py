class SmhiPointRequest:
    def __init__(self, approved_time, reference_time, geometry, time_series):
        self.approved_time: str = approved_time
        self.reference_time: str = reference_time
        self.geometry: SmhiGeometry = geometry
        self.time_series: list[SmhiTimeSeries] = time_series
        return


class SmhiGeometry:
    def __init__(self, smhi_type, coordinates):
        self.smhi_type: str = smhi_type
        self.coordinates: list[list[float]] = coordinates
        return


class SmhiTimeSeries:
    def __init__(self, valid_time, parameters):
        self.valid_time: str = valid_time
        self.parameters: list[SmhiParameter] = parameters
        return


class SmhiParameter:
    def __init__(self, name, level_type, level, unit, values):
        self.name: str = name
        self.level_type: str = level_type
        self.level: int = level
        self.unit: str = unit
        self.values: list[float] = values
        return
