from flask import render_template

from . import ConstructionSite, BulkMaterial
from . import views_bp


@views_bp.route('/construction_site/<int:site_id>')
def construction_site(site_id):
    construction_site = ConstructionSite.query.get(site_id)
    bulk_materials = BulkMaterial.query.filter_by(site_id=site_id).all()
    return render_template('construction_site.html', construction_site=construction_site, bulk_materials=bulk_materials)
