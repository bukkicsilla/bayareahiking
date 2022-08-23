from flask import Blueprint,render_template,redirect,url_for
from hiking import db
from hiking.entrances.forms import AddEntrance, DeleteEntrance
from hiking.models import Entrance

entrances_blueprint = Blueprint('entrances', __name__, template_folder='templates/entrances')
@entrances_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    form = AddEntrance()

    if form.validate_on_submit():
        name = form.name.data
        driving_time = form.driving_time.data
        # Add new Entrance to database
        new_entrance = Entrance(name, driving_time)
        db.session.add(new_entrance)
        db.session.commit()

        return redirect(url_for('entrances.list_hikes'))

    return render_template('add_entrance.html',form=form)

@entrances_blueprint.route('/list')
def list_hikes():
    # Grab a list of entrances (hikes) from database.
    hikes = Entrance.query.all()
    return render_template('list_hikes.html', hikes=hikes)

@entrances_blueprint.route('/delete', methods=['GET', 'POST'])
def delete():
    form = DeleteEntrance()

    if form.validate_on_submit():
        id = form.id.data
        entrance = Entrance.query.get(id)
        db.session.delete(entrance)
        db.session.commit()

        return redirect(url_for('entrances.list_hikes'))
    return render_template('delete_entrance.html',form=form)
