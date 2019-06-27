from urllib.parse import urljoin

import requests
from IPython.core.magic import (Magics, cell_magic, line_cell_magic,
                                line_magic, magics_class)

try:
    from traitlets.config.configurable import Configurable
    from traitlets import Unicode
except ImportError:
    from IPython.config.configurable import Configurable


@magics_class
class GSQLMagics(Magics, Configurable):
    server = Unicode(default_value="http://tigergraph:tigergraph@localhost:14240",
                     config=True, help="TigerGraph Server Address")

    @line_magic('gsql')
    @cell_magic('gsql')
    def cmagic(self, line, cell=''):
        url = urljoin(self.server, '/gsqlserver/interpreted_query')
        r = requests.post(url, data=cell)
        return r.json()


def load_ipython_extension(ip):
    ip.register_magics(GSQLMagics)
