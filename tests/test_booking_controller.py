import pytest

from src.assignment07.controllers import booking as bc
from src.assignment07.models import booking as b, route as r

def test_get_route_dangerous_not_by_air_pass():
    booking = b.Booking(destination_country='Spain', is_urgent=True, is_dangerous=True, weight=3, volume=3)
    route  = bc.get_route(booking)
    assert not route.is_air
    booking = b.Booking(destination_country='Spain', is_urgent=False, is_dangerous=True, weight=3, volume=3)
    route  = bc.get_route(booking)
    assert not route.is_air    
    booking = b.Booking(destination_country='Spain', is_urgent=True, is_dangerous=True, weight=9, volume=125)
    route  = bc.get_route(booking)
    assert not route.is_air  
    booking = b.Booking(destination_country='United States of America', is_urgent=True, is_dangerous=True, weight=9, volume=125)
    route  = bc.get_route(booking)    
    assert not route.is_air    

def test_get_route_via_air_when_urgent_not_dangerous_pass():
    booking = b.Booking(destination_country='Spain', is_urgent=True, is_dangerous=False, weight=3, volume=3)
    route  = bc.get_route(booking)
    assert route.is_air
    booking = b.Booking(destination_country='United States of America', is_urgent=True, is_dangerous=False, weight=3, volume=3)
    route  = bc.get_route(booking)
    assert route.is_air    
    booking = b.Booking(destination_country='Spain', is_urgent=True, is_dangerous=False, weight=9, volume=4.99)
    route  = bc.get_route(booking)
    assert route.is_air    

def test_get_route_heavy_not_urgent_by_ground_domestic_pass():
    booking = b.Booking(destination_country='United States of America', is_urgent=False, is_dangerous=False, weight=9, volume=1)
    route  = bc.get_route(booking)    
    assert route.is_ground      
    booking = b.Booking(destination_country='United States of America', is_urgent=False, is_dangerous=True, weight=9, volume=1)
    route  = bc.get_route(booking)    
    assert route.is_ground  

def test_get_route_large_not_urgent_by_ground_domestic_pass():
    booking = b.Booking(destination_country='United States of America', is_urgent=False, is_dangerous=False, weight=1, volume=125)
    route  = bc.get_route(booking)    
    assert route.is_ground      
    booking = b.Booking(destination_country='United States of America', is_urgent=False, is_dangerous=True, weight=1, volume=125)
    route  = bc.get_route(booking)    
    assert route.is_ground     


def test_get_route_heavy_not_urgent_by_ocean_international_pass():
    booking = b.Booking(destination_country='Spain', is_urgent=False, is_dangerous=False, weight=9, volume=1)
    route  = bc.get_route(booking)    
    assert route.is_ocean    
    booking = b.Booking(destination_country='Spain', is_urgent=False, is_dangerous=True, weight=9, volume=1)
    route  = bc.get_route(booking)    
    assert route.is_ocean    

def test_get_route_large_not_urgent_by_ocean_international_pass():
    booking = b.Booking(destination_country='Spain', is_urgent=False, is_dangerous=False, weight=1, volume=125)
    route  = bc.get_route(booking)    
    assert route.is_ocean       
    booking = b.Booking(destination_country='Spain', is_urgent=False, is_dangerous=True, weight=1, volume=125)
    route  = bc.get_route(booking)    
    assert route.is_ocean           
              
def test_get_air_cost_pass():
    booking = b.Booking(weight=1, volume=10)
    route = r.Route(is_air = True)
    booking.set_route(route)
    cost = bc.get_air_cost(booking)
    assert cost == 200
    booking = b.Booking(weight=10, volume=1)
    route = r.Route(is_air = True)
    booking.set_route(route)
    cost = bc.get_air_cost(booking)
    assert cost == 100    
    booking = b.Booking(weight=10, volume=1)
    route = r.Route(is_air = False)
    booking.set_route(route)
    cost = bc.get_air_cost(booking)
    assert cost == -1      

def test_get_ground_cost_pass():
    booking = b.Booking(is_urgent=False)
    route = r.Route(is_ground=True)
    booking.set_route(route)
    cost = bc.get_ground_cost(booking)
    assert cost == 25
    booking = b.Booking(is_urgent= True)
    route = r.Route(is_ground=True)
    booking.set_route(route)
    cost = bc.get_ground_cost(booking)
    assert cost == 45    
    booking = b.Booking(is_urgent= True)
    route = r.Route(is_ground=False)
    booking.set_route(route)
    cost = bc.get_ground_cost(booking)
    assert cost == -1  

def test_get_ocean_cost_pass():
    booking = b.Booking()
    route = r.Route(is_ocean=True)
    booking.set_route(route)
    cost = bc.get_ocean_cost(booking)
    assert cost == 30
    booking = b.Booking()
    route = r.Route(is_ocean=False)
    booking.set_route(route)
    cost = bc.get_ocean_cost(booking)
    assert cost == -1

def test_get_route_prices():
    booking = b.Booking(is_urgent=False, weight=1, volume=10)
    route = r.Route(is_ground=True, is_air=True, is_ocean=True)
    booking.set_route(route)
    air_cost = bc.get_route_prices(booking).air_price
    ground_cost = bc.get_route_prices(booking).ground_price
    ocean_cost =bc.get_route_prices(booking).ocean_price
    assert air_cost == 200
    assert ground_cost == 25
    assert ocean_cost == 30