from http import HTTPStatus

from jsonschema.validators import validate

from src.schemas.planet_schema import planet_schema


def find_planet_by_name(swapi_client, planet_name: str):
    """
    Helper function to iterate through all pages until `planet_name` is found, or we run out of pages.
    Validates each planet with `planet_schema`.
    Returns the planet data dict if found, else None.
    """
    page = 1
    found_planet = None

    while True:
        resp = swapi_client.get_planets(page=page)
        assert resp.status_code == HTTPStatus.OK, (
            f"Invalid status code: {resp.status_code}"
        )

        data = resp.json()
        for planet in data["results"]:
            validate(instance=planet, schema=planet_schema)

            if planet["name"].lower() == planet_name.lower():
                found_planet = planet
                break

        if found_planet or not data["next"]:
            break

        page += 1

    return found_planet
