from datetime import datetime, timedelta

from sqlalchemy.orm import query
from app.database import SessionLocal
from app.models import Ride, User

"""DUMMY DATA GENERATION SCRIPT"""
COMMON_ROUTES = [
    {
        "departure": "221B Baker ST.",
        "arrival": "Moriarty Lane",
        "typical_times": [9, 17]  # 9 AM and 5 PM
    },
    {
        "departure": "Shrine Lane",
        "arrival": "Mordor Heights",
        "typical_times": [8, 16]  # 8 AM and 4 PM
    },
    {
        "departure": "Never Gonna St.",
        "arrival": "Give You Up Ave.",
        "typical_times": [10, 14]  # 10 AM and 2 PM
    },
    {
        "departure": "Dark Side Ave.",
        "arrival": "Skylwalker Way.",
        "typical_times": [8, 17]
    }
]

REGULAR_DRIVERS = [
    {"username": "ric_o", "name": "Rick O'Shea", "routes": [0, 1]}, 
    {"username": "freeman", "name": "Vroomin'Freeman", "routes": [1, 0]},
    {"username": "rick", "name": "Rick Astley", "routes": [2, 2]},
    {"username": "darth", "name": "Darth Rader", "routes": [3, 3]}
]

def create_users(db):
    for driver in REGULAR_DRIVERS:
        user = db.query(User).filter(User.username == driver["username"]).first()
        if not user:
            user = User(
                username=driver["username"],
                email=f"{driver['username']}@alfredospizza.org",
                password_hash="dummy_hash"
            )
            db.add(user)
            print(f"Created user: {driver['username']}")
    db.commit()

def create_structured_dummy_rides():
    db = SessionLocal()
    start_date = datetime.now()
    
    try:
        # Ensure users exist
        create_users(db)

        for day in range(2):
            for driver in REGULAR_DRIVERS:
                user = db.query(User).filter(User.username == driver["username"]).first()
                if not user:
                    print(f"User {driver['username']} not found!")
                    continue

                for route_index in driver["routes"]:
                    route = COMMON_ROUTES[route_index]
                    
                    for hour in route["typical_times"]:
                        ride_time = start_date + timedelta(days=day, hours=hour)
                        
                        ride = Ride(
                            departure_location=route["departure"],
                            arrival_location=route["arrival"],
                            departure_time=ride_time,
                            available_seats=4,  # Standard 4 seats
                            driver_name=driver["name"],
                            driver_id=user.id  # Associate ride with user
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
