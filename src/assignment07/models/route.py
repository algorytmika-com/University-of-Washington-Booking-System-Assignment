class Route:
    GROUND = 'ground'
    OCEAN = 'ocean'
    AIR = 'air'

    def __init__(self, is_ground : bool = False, is_air : bool = False, is_ocean : bool = False, 
                 ground_price : float = None, air_price : float = None, 
                 ocean_price : float = None, preferred_route : str = None):
        self.is_ground = is_ground
        self.is_air = is_air
        self.is_ocean = is_ocean
        self.ground_price = ground_price
        self.air_price = air_price
        self.ocean_price = ocean_price
        self.preferred_route = preferred_route

    def set_ground_route(self, is_ground : bool):
        self.is_ground = is_ground

    def set_air_route(self, is_air : bool):
        self.is_air = is_air

    def set_ocean_route(self, is_ocean : bool):
        self.is_ocean = is_ocean       

    def set_preferred_route(self, preferred_route : str):
        self.preferred_route = preferred_route           