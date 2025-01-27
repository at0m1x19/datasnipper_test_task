planet_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "rotation_period": {"type": "string"},
        "orbital_period": {"type": "string"},
        "diameter": {"type": "string"},
        "climate": {"type": "string"},
        "gravity": {"type": "string"},
        "terrain": {"type": "string"},
        "surface_water": {"type": "string"},
        "population": {"type": "string"},
        "residents": {
            "type": "array",
            "items": {"type": "string"}
        },
        "films": {
            "type": "array",
            "items": {"type": "string"}
        },
        "created": {"type": "string"},
        "edited": {"type": "string"},
        "url": {"type": "string"}
    },
    "required": ["name", "url", "diameter"]
}
