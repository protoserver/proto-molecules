
from cement import Controller, ex


class NginxMolecule(Controller):

    class Meta:
        label = 'nginx'
        stacked_on = 'base'
        stacked_type = 'nested'

    def _default(self):
        self._parser.print_help()

    @ex(
        help='example sub command1',
        arguments=[
            ### add a sample foo option under subcommand namespace
            ( [ '-f', '--foo' ],
              { 'help' : 'notorious foo option',
                'action'  : 'store',
                'dest' : 'foo' } ),
        ],
    )
    def command1(self):
        """Example sub-command."""

        data = {
            'foo' : 'bar',
        }

        ### do something with arguments
        if self.app.pargs.foo is not None:
            data['foo'] = self.app.pargs.foo

        self.app.render(data, 'plugins/nginx/command1.jinja2')
