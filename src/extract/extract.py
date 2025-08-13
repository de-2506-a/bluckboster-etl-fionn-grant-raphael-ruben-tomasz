import pandas as pd
from src.extract.extract_actor import extract_actor
from src.extract.extract_address import extract_address
from src.extract.extract_category import extract_category
from src.extract.extract_city import extract_city
from src.extract.extract_country import extract_country
from src.extract.extract_customer import extract_customer
from src.extract.extract_film_actor import extract_film_actor
from src.extract.extract_film_category import extract_film_category
from src.extract.extract_film import extract_film
from src.extract.extract_inventory import extract_inventory
from src.extract.extract_payment import extract_payment
from src.extract.extract_rental import extract_rental


def extract_data() -> tuple[pd.DataFrame,pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    try:
        actor_table = extract_actor()
        address_table = extract_address()
        category_table = extract_category()
        city_table = extract_city()
        country_table = extract_country()
        customer_table = extract_customer()
        film_actor_table = extract_film_actor()
        film_category_table = extract_film_category()
        film_table = extract_film()
        inventory_table = extract_inventory()
        payment_table = extract_payment()
        rental_table = extract_rental()



        print(f"Data Extraction was completed successfully")
        print(f"Actor: {actor_table.shape}")
        print(f"Address: {address_table.shape}")
        print(f"Category: {category_table.shape}")
        print(f"City: {city_table.shape}")
        print(f"Country: {country_table.shape}")
        print(f"Customer: {customer_table.shape}")
        print(f"Film_actor: {film_actor_table.shape}")
        print(f"Film_category: {film_category_table.shape}")
        print(f"Film: {film_table.shape}")
        print(f"Inventory: {inventory_table.shape}")
        print(f"Payment: {payment_table.shape}")
        print(f"Rental: {rental_table.shape}")

        return (actor_table, address_table,category_table,city_table,country_table,customer_table,film_actor_table,film_category_table,film_table,inventory_table,payment_table,rental_table)
    except Exception as e:
        print(f"Data extraction has failed: {str(e)}")
        raise