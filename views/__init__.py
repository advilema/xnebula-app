from flask import Blueprint
from models.models import ConstructionSite, BulkMaterial, MaterialTracking, db
from config import Config

views_bp = Blueprint('views', __name__)

from . import index, construction_site, add_construction_site, add_bulk_material, bulk_material, material_tracking