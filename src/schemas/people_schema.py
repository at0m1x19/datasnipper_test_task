person_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "height": {"type": "string"},
        "mass": {"type": "string"},
        "hair_color": {"type": "string"},
        "skin_color": {"type": "string"},
        "eye_color": {"type": "string"},
        "birth_year": {"type": "string"},
        "gender": {"type": "string"},
        "homeworld": {"type": "string"},
        "films": {
            "type": "array",
            "items": {"type": "string"}
        },
        "species": {
            "type": "array",
            "items": {"type": "string"}
        },
        "vehicles": {
            "type": "array",
            "items": {"type": "string"}
        },
        "starships": {
            "type": "array",
            "items": {"type": "string"}
        },
        "created": {"type": "string"},
        "edited": {"type": "string"},
        "url": {"type": "string"}
    },
    "required": ["name", "url"]
}
