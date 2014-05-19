from flask import Flask, render_template
from flask.ext.wtf import Form
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from unipath import Path

from parser import Parser


app = Flask(
	__name__,
	template_folder=Path(__file__).ancestor(1).child("templates"),
)
app.config['SECRET_KEY'] = 'something cool and hard'

Bootstrap(app)


class ParseForm(Form):
	code = StringField('Code to parse', validators=[Required()])
	phrase = StringField('Phrase to use', validators=[Required()])
	submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
	result = None
	form = ParseForm()
	if form.validate_on_submit():
		code = form.code.data
		phrase = form.phrase.data
		form.phrase.data = ''
		form.code.data = ''
		result = Parser(code=code, phrase=phrase).run()
	return render_template('index.html', form=form, result=result)


if __name__ == '__main__':
	app.run(debug=True)