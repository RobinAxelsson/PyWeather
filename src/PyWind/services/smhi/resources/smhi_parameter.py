class SmhiParameter:
    def __init__(self, name, level_type, level, unit, values):
        self.name: str = name
        self.level_type: str = level_type
        self.level: int = level
        self.unit: str = unit
        self.values: list[float] = values
        return
