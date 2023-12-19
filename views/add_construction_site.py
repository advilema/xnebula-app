from flask import render_template, redirect, url_for, request

from . import views_bp, ConstructionSite, db


@views_bp.route('/add_construction_site', methods=['GET', 'POST'])
def add_construction_site():
    if request.method == 'POST':
        site_name = request.form['site_name']
        location = request.form['location']
        manager = request.form['manager']
        surface = request.form['surface']

        new_construction_site = ConstructionSite(site_name=site_name, location=location, manager=manager, surface=surface)
        db.session.add(new_construction_site)
        db.session.commit()

        return redirect(url_for('views.index'))

    return render_template('add_construction_site.html')