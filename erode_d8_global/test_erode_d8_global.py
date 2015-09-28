"""IRF with the ErodeD8Global component."""
import os
from topoflow.components.erode_d8_global import erosion_component as Model


component = Model()
print component.get_component_name()

out_dir = 'out'
if os.path.exists(out_dir) is False:
    os.mkdir(out_dir)

component.initialize('Erode_D8_Global.cfg')
component.update(1.0)
component.finalize()
