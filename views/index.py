from flask import render_template

from . import ConstructionSite
from . import views_bp


@views_bp.route('/')
def index():
    construction_sites = ConstructionSite.query.all()
    return render_template('index.html', construction_sites=construction_sites)