from flask import Blueprint
from models.models import ConstructionSite, BulkMaterial, MaterialTracking, db

views_bp = Blueprint('views', __name__)
UPLOAD_FOLDER = 'static/images'

from . import index, construction_site, add_construction_site, add_bulk_material, bulk_material, material_tracking
