class WindForecast:
    def __init__(self, mean_wsp, max_wsp, direction, lat, long, reference_time, target_time, source):

        self.mean_wsp: float = mean_wsp
        self.max_wsp: float = max_wsp
        self.direction: int = direction
        self.latitude: float = lat
        self.longitude: float = long
        self.reference_time = reference_time
        self.target_time = target_time
        self.source = source
