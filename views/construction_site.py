from flask import render_template

from . import ConstructionSite, BulkMaterial, MaterialTracking
from . import views_bp


@views_bp.route('/construction_site/<int:site_id>')
def construction_site(site_id):
    construction_site = ConstructionSite.query.get(site_id)
    bulk_materials = BulkMaterial.query.filter_by(site_id=site_id).all()
    material_types_quantities = quantities_per_material_type(bulk_materials)
    return render_template('construction_site.html', construction_site=construction_site,
                           bulk_materials=bulk_materials, material_types_quantities=material_types_quantities)


def quantities_per_material_type(bulk_materials: list[BulkMaterial]):
    material_types = []
    quantities = []

    for bulk_material in bulk_materials:
        quantity = MaterialTracking.query.filter_by(bulk_id=bulk_material.id).all()[-1].quantity
        if bulk_material.material_type in material_types:
            material_idx = material_types.index(bulk_material.material_type)
            quantities[material_idx] += quantity
        else:
            material_types.append(bulk_material.material_type)
            quantities.append(quantity)

    return zip(material_types, quantities)
