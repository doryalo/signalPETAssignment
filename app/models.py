class Animal:
    def __init__(self, id, name, specie, age, breed, xray_image_urls=None):
        if not isinstance(id, int) or id < 0:
            raise ValueError("ID must be a non-negative integer.")
        self.id = id

        if self.validate_property(name, str):
            raise ValueError("Name must be a non-empty string.")
        self.name = name

        if self.validate_property(specie, str):
            raise ValueError("Specie must be a non-empty string.")
        self.specie = specie

        if not isinstance(age, int) or age < 0:
            raise ValueError("Age must be a non-negative integer.")
        self.age = age

        if self.validate_property(breed, str):
            raise ValueError("Breed must be a non-empty string.")
        self.breed = breed

        self.xray_image_urls = xray_image_urls if xray_image_urls is not None else []
    
    def validate_property(property: str, type: str):
        return not property or not isinstance(property, type)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "specie": self.specie,
            "age": self.age,
            "breed": self.breed,
            "xray_image_urls": self.xray_image_urls
         }
