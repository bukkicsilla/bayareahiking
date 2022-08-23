from flask import Blueprint,render_template,redirect,url_for
from hiking import db
from hiking.models import Trail
from hiking.trails.forms import AddTrail

trails_blueprint = Blueprint('trails', __name__, template_folder='templates/trails')

@trails_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    form = AddTrail()

    if form.validate_on_submit():
        name = form.name.data
        entrance_id = form.entrance_id.data
        # Add new trail to database
        new_trail = Trail(name,entrance_id)
        db.session.add(new_trail)
        db.session.commit()

        return redirect(url_for('entrances.list_hikes'))

    return render_template('add_trail.html',form=form)
