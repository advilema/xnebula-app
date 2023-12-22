from flask import render_template, redirect, url_for, request
from werkzeug.utils import secure_filename
import os

from . import views_bp, ConstructionSite, db, UPLOAD_FOLDER


@views_bp.route('/add_construction_site', methods=['GET', 'POST'])
def add_construction_site():
    if request.method == 'POST':
        site_name = request.form['site_name']
        location = request.form['location']
        manager = request.form['manager']
        surface = request.form['surface']
        site_map = request.files['site_map']
        site_id = ConstructionSite.query.count() + 1

        if site_map:
            filename = secure_filename('site-map' + '.jpg')
            map_dir = os.path.join(UPLOAD_FOLDER, str(site_id))
            if not os.path.isdir(map_dir):
                os.mkdir(map_dir)
            map_url = os.path.join(map_dir, filename)
            site_map.save(map_url)
        else:
            map_url = None

        new_construction_site = ConstructionSite(id=site_id, site_name=site_name, location=location, manager=manager,
                                                 surface=surface, map_url=map_url)
        db.session.add(new_construction_site)
        db.session.commit()

        return redirect(url_for('views.index'))

    return render_template('add_construction_site.html')