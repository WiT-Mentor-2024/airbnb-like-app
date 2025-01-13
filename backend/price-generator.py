import time
import random
from sqlalchemy.orm import Session
from models import Apartment
from database import get_db
import threading
from contextlib import contextmanager


def generate_random_price() -> float:
    """
    Generate random price for apartment.
    """
    min_price = 20.00
    max_price = 200.00
    return round(random.uniform(min_price, max_price), 2)


def update_prices_periodically(interval_seconds: int):
    """
    Update price for all available apartments every `interval_seconds` seconds.
    """
    stop_event = threading.Event()

    def update_loop():
        while not stop_event.is_set():
            try:
                with Session(get_db()) as db:
                    apartments = db.query(Apartment).filter(Apartment.is_available == True).all()
                    for apartment in apartments:
                        new_price = generate_random_price()
                        apartment.price_per_night = new_price
                    db.commit()
                    print("Prices updated successfully")
            except Exception as e:
                print(f"Error updating prices: {e}")
            
            time.sleep(interval_seconds)

    update_thread = threading.Thread(target=update_loop, daemon=True)
    update_thread.start()
    return stop_event


if __name__ == "__main__":
    stop_event = update_prices_periodically(60)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        stop_event.set()
        print("Stopping price updates...")
