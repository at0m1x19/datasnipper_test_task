import requests


class SwapiClient:
    BASE_URL = "https://swapi.dev/api"

    def __init__(self, base_url=None):
        """
        Allow overriding base_url for tests/mocks if needed.
        """
        self.base_url = base_url or self.BASE_URL

    def get_people(self, page=1):
        """
        GET /people/?page={page}
        """
        url = f"{self.base_url}/people/?page={page}"
        return requests.get(url)

    def get_planets(self, page=1):
        """
        GET /planets/?page={page}
        """
        url = f"{self.base_url}/planets/?page={page}"
        return requests.get(url)

    def get_person_by_id(self, person_id: int):
        """
        GET /people/{person_id}/
        """
        url = f"{self.base_url}/people/{person_id}/"
        return requests.get(url)

    def get_planet_by_id(self, planet_id: int):
        """
        GET /planets/{planet_id}/
        """
        url = f"{self.base_url}/planets/{planet_id}/"
        return requests.get(url)

    @staticmethod
    def get_vehicle_by_url(vehicle_url: str):
        """
        GET the vehicle by the full URL (e.g. https://swapi.dev/api/vehicles/14/)
        """
        return requests.get(vehicle_url)

    def get_film_by_id(self, film_id: int):
        """
        GET /films/{film_id}/
        """
        url = f"{self.base_url}/films/{film_id}/"
        return requests.get(url)
