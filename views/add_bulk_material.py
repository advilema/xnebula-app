from datetime import datetime

from flask import render_template, redirect, url_for, request

from . import views_bp, BulkMaterial, db


@views_bp.route('/add_bulk_material/<int:site_id>', methods=['GET', 'POST'])
def add_bulk_material(site_id):
    if request.method == 'POST':
        material_type = request.form['material_type']
        date_received_str = request.form['date_received']
        date_received = datetime.strptime(date_received_str, '%Y-%m-%d').date()
        picture_url = request.form['picture_url']

        new_bulk_material = BulkMaterial(site_id=site_id, material_type=material_type, date_received=date_received, picture_url=picture_url)
        db.session.add(new_bulk_material)
        db.session.commit()

        return redirect(url_for('views.construction_site', site_id=site_id))

    return render_template('add_bulk_material.html', site_id=site_id)
