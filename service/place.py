from dao.place import PlaceDAO


class PlaceService:
    def __init__(self, dao: PlaceDAO):
        self.dao = dao

    def get_one(self, pid):
        return self.dao.get_one(pid)

    def get_all(self):
        data = self.dao.get_all()
        for key, value in data:
            if key == "features_on":
                data[key] = value.split(",")

        for key, value in data:
            if key == "features_off":
                data[key] = value.split(",")
        return data

    def get_by_city(self, city):
        return self.dao.get_by_city(city)

    def get_by_price(self, price_from, price_to):
        return self.dao.get_by_price(price_from, price_to)

    def get_by_city_and_price(self, city, price_from, price_to):
        return self.dao.get_by_city_and_price(city, price_from, price_to)
