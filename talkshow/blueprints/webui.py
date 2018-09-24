import datetime

from flask import current_app as app, abort, request
from flask import Blueprint, render_template
from flask_wtf import FlaskForm
import wtforms as wtf

bp = Blueprint("webui", __name__)

@bp.route("/")
def index():
    """View to list all registred events"""
    events = app.db['events'].find()
    return render_template('index.html', events=events)


class ProposalForm(FlaskForm):
    """Form to register new proposals to events"""
    name = wtf.StringField('name', validators=[wtf.validators.DataRequired()])
    email = wtf.StringField('email', validators=[wtf.validators.Email()])
    title = wtf.StringField('title', validators=[wtf.validators.DataRequired()])
    description = wtf.TextAreaField(
        'description', validators=[wtf.validators.DataRequired()]
    )
    submit = wtf.SubmitField("Enviar")


@bp.route("/<event_id>/", methods=['GET', 'POST'])
def event(event_id):
    """A form to submit a talk to the selected event"""
    event = app.db['events'].find_one({'_id': event_id})
    if not event:
        abort(404, 'Evento não encontrado')

    form = ProposalForm(request.form)

    if form.validate_on_submit():
        # Se estamos no meio de um submit válido preparamos os dados
        proposal = form.data.copy()
        proposal['event_id'] = event_id
        proposal['date'] = datetime.datetime.today().date().isoformat()
        proposal['approved'] = False
        # e gravamos no banco de dados
        app.db['talks'].insert_one(proposal)

        return render_template('thanks.html', proposal=proposal, event=event)

    # exibimos o formulário limpo
    return render_template('event.html', form=form, event=event)


def configure(app):
    app.register_blueprint(bp)