from flask import render_template, Blueprint, abort
from jinja2 import TemplateNotFound

content = Blueprint("content", __name__,
                    template_folder="templates", static_folder="static")


@content.route('/', defaults={'page': 'index'})
@content.route('/<page>')
def show(page):
    try:
        return render_template('%s.html' % page)
    except TemplateNotFound:
        abort(404)
