from datetime import datetime, timedelta
from app.database import SessionLocal
from app.models import Ride, User

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
    {"username": "risto", "name": "Risto Rautalanka", "routes": [0, 1]}, 
    {"username": "aimo", "name": "Aimo Mainio", "routes": [1, 2]},
    {"username": "sulo", "name": "Sulo Säihky", "routes": [0, 2]}
]

def create_users(db):
    """Ensure regular drivers exist in the database."""
    for driver in REGULAR_DRIVERS:
        user = db.query(User).filter(User.username == driver["username"]).first()
        if not user:
            user = User(
                username=driver["username"],
                email=f"{driver['username']}@example.com",
                password_hash="dummy_hash"  # Replace with hashed password if needed
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