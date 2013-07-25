r"""paraviewweb_wamp is the paraview-specific subclass
    of vtkweb_wamp that provides the PVWeb Application
"""

from vtkweb import vtkweb_wamp
from vtkParaViewWebCorePython import vtkPVWebApplication

class PVServerProtocol(vtkweb_wamp.ServerProtocol):
    def initApplication(self):
        return vtkPVWebApplication()
