
import os
from .controllers.sonarr import SonarrMolecule

def add_template_dir(app):
    path = os.path.join(os.path.dirname(__file__), 'templates')
    app.add_template_dir(path)

def load(app):
    app.handler.register(SonarrMolecule)
    app.hook.register('post_setup', add_template_dir)
