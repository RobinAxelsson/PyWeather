from .smhi_geometry import SmhiGeometry
from .smhi_time_series import SmhiTimeSeries


class SmhiPointRequest:
    def __init__(self, approved_time, reference_time, geometry, time_series):
        self.approved_time: str = approved_time
        self.reference_time: str = reference_time
        self.geometry: SmhiGeometry = geometry
        self.time_series: list[SmhiTimeSeries] = time_series
        return
