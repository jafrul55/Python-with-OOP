class Airport:
    def __init__(self,name,country,lat,lon,rate) -> None:
        self.name = name
        self.country = country
        self.lat = lat
        self.lon = lon
        self.rate = rate

    def __repr__(self) -> str:
        return f"Airport: {self.name} in: {self.country} lat: {self.lat} lon: {self.lon} rate: {self.rate}"
    