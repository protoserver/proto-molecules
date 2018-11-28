
import os
from .controllers.nginx import NginxMolecule

def add_template_dir(app):
    path = os.path.join(os.path.dirname(__file__), 'templates')
    app.add_template_dir(path)

def load(app):
    app.handler.register(NginxMolecule)
    app.hook.register('post_setup', add_template_dir)
    app.log.debug("Nginx ProtoServer Molecule loaded.")
