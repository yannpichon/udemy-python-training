"""Module to generate random user"""
import faker
import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
logging.basicConfig(filename=BASE_DIR / "app.log", level=logging.WARNING)

fake = faker.Faker()

def get_user() -> str :
    """Generate a single random user

    Returns:
        str: User
    """
    logging.info("Generating user.")
    return f"{fake.first_name()} {fake.last_name()}"

def get_users(nb_user: int) -> list[str]:
    """Generate a list of user

    Args:
        nb_user (int): Number of user to generate
    Returns:
        list[str]: List of users
    """
    logging.info(f"Generating a list of {nb_user} users.")
    return [get_user() for _ in range(nb_user)]

if __name__ == "__main__":
    print(get_user())       
    print(get_users(5))