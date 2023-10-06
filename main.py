import requests
import json


headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
}

URL = "https://uk.api.just-eat.io/restaurants/bypostcode/"


class Restaurants:
    def __init__(self) -> None:
        self._postcode = None

    def start(self) -> None:
        self._postcode = input("Enter UK postcode: ")

        if not self._postcode:
            print("Please enter a valid UK postcode.")
            self.start()

        self._by_postcode()

    def _by_postcode(self) -> None:
        response = requests.get(f"{URL + self._postcode}", headers=headers)

        if response.status_code != 200:
            raise Exception(f"{response.status_code}")

        try:
            restaurants = response.json()["Restaurants"]
        except KeyError:
            raise "KeyError 'Restaurants': Could not parse JSON response."

        self._write_json_file(restaurants)

    @staticmethod
    def _write_json_file(restaurants: json) -> None:

        restaurant_data = [
            {
                "name": restaurant["Name"],
                "rating": restaurant["RatingStars"],
                "cuisine_types": [
                    cuisine["Name"] for cuisine in restaurant["CuisineTypes"]
                ],
            } for restaurant in restaurants
        ]

        try:
            with open("restaurants.json", "w") as f:
                json.dump(restaurant_data, f, indent=4)
        except Exception as e:
            raise f"Error: Could not write JSON file: {e}"


if __name__ == "__main__":
    client = Restaurants()
    client.start()
