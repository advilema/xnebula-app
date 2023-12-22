from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class ConstructionSite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    site_name = db.Column(db.String(255), unique=True, nullable=False)
    location = db.Column(db.String(255), nullable=False)
    manager = db.Column(db.String(255), nullable=False)
    surface = db.Column(db.Float)
    map_url = db.Column(db.String(255))


class BulkMaterial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    site_id = db.Column(db.Integer, db.ForeignKey('construction_site.id'), nullable=False)
    material_type = db.Column(db.String(255), nullable=False)
    date_received = db.Column(db.Date, nullable=False)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)


class MaterialTracking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bulk_id = db.Column(db.Integer, db.ForeignKey('bulk_material.id'), nullable=False)
    site_id = db.Column(db.Integer, db.ForeignKey('construction_site.id'), nullable=False)
    date_tracked = db.Column(db.DateTime, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    responsible_person = db.Column(db.String(255), nullable=False)
    picture_url = db.Column(db.String(255))
    picture_detection_url = db.Column(db.String(255))
