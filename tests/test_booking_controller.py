import pytest

from src.assignment07.controllers import booking as bc
from src.assignment07.models import booking as b

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
              