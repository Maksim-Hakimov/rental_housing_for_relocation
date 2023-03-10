from flask_restx import Resource, Namespace
from flask import request

from dao.model.place import PlaceSchema
from implemented import place_service

place_ns = Namespace('places')


@place_ns.route('/')
class PlaceView(Resource):

    def get(self):
        filter_city = request.args.get('city')
        price_from = request.args.get('from', 1)
        price_to = request.args.get('to', 1000)

        if price_from == "":
            price_from = 1

        if price_to == "":
            price_to = 1000

        if filter_city and price_from and price_to is not None and filter_city != '':
            return PlaceSchema(many=True).dump(place_service.get_by_city_and_price(filter_city, price_from, price_to))

        if filter_city is not None and filter_city != '':
            return PlaceSchema(many=True).dump(place_service.get_by_city(filter_city))

        if price_from and price_to is not None:
            return PlaceSchema(many=True).dump(place_service.get_by_price(price_from, price_to))

        places = place_service.get_all()
        result = PlaceSchema(many=True).dump(places)
        return result, 200


@place_ns.route('/<int:pk>')
class PlacesViews(Resource):
    def get(self, pk):
        place = place_service.get_one(pk)
        return PlaceSchema().dump(place)
