from marshmallow import Schema, fields

from setup_db import db


class Place(db.Model):
    __tablename__ = 'place'
    pk = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    picture_url = db.Column(db.String)
    price = db.Column(db.Integer)
    country = db.Column(db.String(100))
    city = db.Column(db.String(100))
    features_on = db.Column(db.String(255))
    features_off = db.Column(db.String(255))
    host_name = db.Column(db.String(100))
    host_phone = db.Column(db.String(100))
    host_location = db.Column(db.String(100))


class PlaceSchema(Schema):
    pk = fields.Int()
    title = fields.Str()
    description = fields.Str()
    picture_url = fields.Str()
    price = fields.Int()
    country = fields.Str()
    city = fields.Str()
    features_on = fields.Str()
    features_off = fields.Str()
    host_name = fields.Str()
    host_phone = fields.Str()
    host_location = fields.Str()
