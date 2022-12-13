class SmhiGeometry:
    def __init__(self, smhi_type, coordinates):
        self.smhi_type: str = smhi_type
        self.coordinates: list[list[float]] = coordinates
        return
