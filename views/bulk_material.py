from flask import render_template

from . import views_bp, BulkMaterial, MaterialTracking


@views_bp.route('/bulk_material/<int:bulk_id>')
def bulk_material(bulk_id):
    bulk_material = BulkMaterial.query.get(bulk_id)
    tracking_records = MaterialTracking.query.filter_by(bulk_id=bulk_id).order_by(MaterialTracking.date_tracked).all()
    # if request.method == 'POST':
    #    return redirect(url_for('material_tracking.html', bulk_id=bulk_id))
    return render_template('bulk_material.html', bulk_material=bulk_material,
                           tracking_records=tracking_records)
