from datetime import datetime

import os

from . import views_bp, MaterialTracking, db, UPLOAD_FOLDER, BulkMaterial
from flask import render_template, redirect, url_for, request
from werkzeug.utils import secure_filename
from detection.yolov8 import YOLOCount


@views_bp.route('/material_tracking_detection/<int:bulk_id>', methods=['GET', 'POST'])
def material_tracking_detection(bulk_id):
    if request.method == 'POST':
        date_tracked = datetime.now()
        date_tracked_str = date_tracked.strftime('%y-%m-%dT%H:%M:%S')
        picture = request.files['picture']
        bulk_material = BulkMaterial.query.filter_by(id=bulk_id).first()
        site_id = bulk_material.site_id

        # Save the uploaded picture to the "uploads" directory
        if picture:
            filename = secure_filename(date_tracked_str + '.jpg')
            picture_dir = os.path.join(os.path.join(UPLOAD_FOLDER, str(site_id)), str(bulk_id))
            if not os.path.isdir(picture_dir):
                os.mkdir(picture_dir)
            picture_url = os.path.join(picture_dir, filename)
            picture.save(picture_url)
        else:
            picture_url = None

        counter = YOLOCount()
        obj_count, picture_detection_url = counter(picture_url)

        return redirect(url_for('views.material_tracking', bulk_id=bulk_id, site_id=site_id,
                                date_tracked=date_tracked_str, picture_url=picture_url,
                                picture_detection_url=picture_detection_url, obj_count=obj_count))

    return render_template('material_tracking_detection.html', bulk_id=bulk_id)


@views_bp.route('/material_tracking/<int:bulk_id>', methods=['GET', 'POST'])
def material_tracking(bulk_id):
    date_tracked_str = request.args['date_tracked']
    # date_tracked_str = date_tracked
    date_tracked = datetime.strptime(date_tracked_str, '%y-%m-%dT%H:%M:%S')
    picture_url = request.args['picture_url']
    picture_detection_url = request.args['picture_detection_url']
    obj_count = request.args['obj_count']
    site_id = request.args['site_id']

    if request.method == 'POST':
        quantity = request.form['quantity']
        responsible_person = request.form['responsible_person']

        new_material_tracking = MaterialTracking(bulk_id=bulk_id, site_id=site_id, date_tracked=date_tracked,
                                                 quantity=quantity, responsible_person=responsible_person,
                                                 picture_url=picture_url, picture_detection_url=picture_detection_url)
        db.session.add(new_material_tracking)
        db.session.commit()

        return redirect(url_for('views.bulk_material', bulk_id=bulk_id))

    return render_template('material_tracking.html', bulk_id=bulk_id, date_tracked=date_tracked_str,
                           picture_url=picture_url, picture_detection_url=picture_detection_url, obj_count=obj_count)
