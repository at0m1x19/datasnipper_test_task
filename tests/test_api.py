from http import HTTPStatus
from jsonschema import validate

from src.helper import find_planet_by_name
from src.schemas.people_schema import person_schema
from src.schemas.planet_schema import planet_schema


def test_total_counts(swapi_client):
    """
    Test case 1:
      - total planets should be 60
      - total people should be 82
    """
    expected_planet_count = 60
    expected_people_count = 82

    planet_resp = swapi_client.get_planets()
    assert planet_resp.status_code == HTTPStatus.OK, (
        f"Invalid status code: {planet_resp.status_code}"
    )
    planet_data = planet_resp.json()
    assert planet_data["count"] == expected_planet_count, (
        f"Expected {expected_planet_count} planets, got {planet_data['count']}"
    )

    people_resp = swapi_client.get_people()
    assert people_resp.status_code == HTTPStatus.OK, (
        f"Invalid status code: {people_resp.status_code}"
    )
    people_data = people_resp.json()
    assert people_data["count"] == expected_people_count, (
        f"Expected {expected_people_count} people, got {people_data['count']}"
    )


def test_planets_in_anew_hope(swapi_client):
    """
    Test case 2:
      - The film with ID=1 is "A New Hope"
      - It should list exactly ["Tatooine", "Alderaan", "Yavin IV"] as planets
    """
    film_id = 1
    expected_film_name = "A New Hope"
    expected_planets = ["Tatooine", "Alderaan", "Yavin IV"]

    film_resp = swapi_client.get_film_by_id(film_id)
    assert film_resp.status_code == HTTPStatus.OK, (
        f"Invalid status code: {film_resp.status_code}"
    )
    film_data = film_resp.json()

    actual_film_name = film_data["title"]
    assert actual_film_name == expected_film_name, (
        f"Expected film title '{expected_film_name}', got '{actual_film_name}'"
    )

    actual_planets = []
    for planet_url in film_data["planets"]:
        planet_id = planet_url.rstrip("/").split("/")[-1]
        p_resp = swapi_client.get_planet_by_id(planet_id)
        assert p_resp.status_code == HTTPStatus.OK, (
            f"Invalid status code: {p_resp.status_code}"
        )

        p_data = p_resp.json()
        validate(instance=p_data, schema=planet_schema)

        actual_planets.append(p_data["name"])

    assert actual_planets == expected_planets, (
        f"Mismatch in planets.\nExpected: {expected_planets}\nGot: {actual_planets}"
    )


def test_luke_skywalker_vehicles(swapi_client):
    """
    Test case 3:
      - Person #1 should be "Luke Skywalker"
      - Vehicles => "Snowspeeder" (speed=650), "Imperial Speeder Bike" (speed=360)
    """
    person_id = 1
    expected_name = "Luke Skywalker"
    expected_vehicles = {
        "Snowspeeder": "650",
        "Imperial Speeder Bike": "360",
    }

    luke_resp = swapi_client.get_person_by_id(person_id)
    assert luke_resp.status_code == HTTPStatus.OK, (
        f"Invalid status code: {luke_resp.status_code}"
    )
    luke_data = luke_resp.json()

    validate(instance=luke_data, schema=person_schema)

    assert luke_data["name"] == expected_name, (
        f"Expected '{expected_name}', got '{luke_data['name']}'"
    )

    actual_vehicles = {}
    for vehicle_url in luke_data["vehicles"]:
        v_resp = swapi_client.get_vehicle_by_url(vehicle_url)
        assert v_resp.status_code == HTTPStatus.OK, (
            f"Invalid status code: {v_resp.status_code}"
        )
        v_data = v_resp.json()

        v_name = v_data["name"]
        v_speed = v_data["max_atmosphering_speed"]
        actual_vehicles[v_name] = v_speed

    for veh_name, veh_speed in expected_vehicles.items():
        assert veh_name in actual_vehicles, f"{veh_name} not found among Luke's vehicles"
        assert actual_vehicles[veh_name] == veh_speed, (
            f"{veh_name} speed mismatch. Expected {veh_speed}, got {actual_vehicles[veh_name]}"
        )


def test_dorin_planet(swapi_client):
    """
    Test case 4:
      - Planet "Dorin" => diameter=13400
      - exactly 1 resident => "Plo Koon"
    """
    planet_name = "dorin"
    expected_diameter = "13400"
    expected_resident_count = 1
    expected_resident_name = "Plo Koon"

    found_dorin = find_planet_by_name(swapi_client, planet_name)
    assert found_dorin, f"Planet '{planet_name}' not found in all pages"

    assert found_dorin["diameter"] == expected_diameter, (
        f"Expected diameter={expected_diameter}, got {found_dorin['diameter']}"
    )

    residents = found_dorin["residents"]
    assert len(residents) == expected_resident_count, (
        f"Expected exactly {expected_resident_count} resident(s), got {len(residents)}"
    )

    resident_url = residents[0]
    resident_id = resident_url.rstrip("/").split("/")[-1]
    r_resp = swapi_client.get_person_by_id(resident_id)
    assert r_resp.status_code == HTTPStatus.OK, (
        f"Invalid status code: {r_resp.status_code}"
    )
    r_data = r_resp.json()
    validate(instance=r_data, schema=person_schema)

    assert r_data["name"] == expected_resident_name, (
        f"Expected resident '{expected_resident_name}', got {r_data['name']}"
    )
