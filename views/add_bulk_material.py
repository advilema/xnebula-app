from datetime import datetime

from flask import render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField

from . import views_bp, BulkMaterial, db, Config


class BulkMaterialForm(FlaskForm):
    material_type = SelectField('Material Type', choices=Config.BULK_MATERIAL_CATEGORIES)
    submit = SubmitField('Add Bulk Material')


@views_bp.route('/add_bulk_material/<int:site_id>', methods=['GET', 'POST'])
def add_bulk_material(site_id):
    form = BulkMaterialForm()
    if form.validate_on_submit():
        material_type = form.material_type.data
        #material_type = request.form['material_type']
        date_received = datetime.now()
        latitude = request.form['latitude']
        longitude = request.form['longitude']

        new_bulk_material = BulkMaterial(site_id=site_id, material_type=material_type, date_received=date_received,
                                         latitude=latitude, longitude=longitude)
        db.session.add(new_bulk_material)
        db.session.commit()

        return redirect(url_for('views.material_tracking_detection', bulk_id=new_bulk_material.id))

    return render_template('add_bulk_material.html', site_id=site_id, form=form)
