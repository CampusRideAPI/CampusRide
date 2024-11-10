from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Ride

"""DUMMY DATA GENERATION SCRIPT"""
COMMON_ROUTES = [
    {
        "departure": "Kupittaa CAMPUS",
        "arrival": "Centrum, Keskusta",
        "typical_times": [9, 17]  # 9 AM and 5 PM
    },
    {
        "departure": "Centrum, Keskusta",
        "arrival": "Kupittaa CAMPUS",
        "typical_times": [8, 16]  # 8 AM and 4 PM
    },
    {
        "departure": "Ylioppilaskylä",
        "arrival": "Kupittaa CAMPUS",
        "typical_times": [10, 14]  # 10 AM and 2 PM
    }
]

REGULAR_DRIVERS = [
    {"name": "Risto Rautalanka", "routes": [0, 1]}, 
    {"name": "Aimo Mainio", "routes": [1, 2]},
    {"name": "Sulo Säihky", "routes": [0, 2]}
]

def create_structured_dummy_rides():
    db = SessionLocal()
    start_date = datetime.now()
    """Dummy dataa 7 päiväksi"""
    try:
        for day in range(7):
            for driver in REGULAR_DRIVERS:
                for route_index in driver["routes"]:
                    route = COMMON_ROUTES[route_index]
                    
                    for hour in route["typical_times"]:
                        ride_time = start_date + timedelta(days=day, hours=hour)
                        
                        ride = Ride(
                            departure_location=route["departure"],
                            arrival_location=route["arrival"],
                            departure_time=ride_time,
                            available_seats=4,  # Standard 4 seats
                            driver_name=driver["name"]
                        )
                        db.add(ride)
        
        db.commit()
        print("Structured dummy data created successfully!")
        
    except Exception as e:
        print(f"Error creating dummy data: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    create_structured_dummy_rides()