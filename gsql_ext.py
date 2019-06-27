from urllib.parse import urljoin

import requests
from IPython.core.magic import (Magics, cell_magic, line_cell_magic,
                                line_magic, magics_class)


@magics_class
class GSQLMagics(Magics):
    tg_server = None

    @line_magic('gsql')
    def lmagic(self, line):
        self.tg_server = line

    @cell_magic('gsql')
    def cmagic(self, line, cell):
        url = urljoin(self.tg_server, '/gsqlserver/interpreted_query')
        r = requests.post(url, data=cell)
        return r.json()


def load_ipython_extension(ip):
    ip.register_magics(GSQLMagics)
