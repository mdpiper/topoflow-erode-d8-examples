"""IRF with the ErodeD8Local component."""
import os
from topoflow.components.erode_d8_local import erosion_component as Model


component = Model()
print component.get_component_name()

out_dir = 'out'
if os.path.exists(out_dir) is False:
    os.mkdir(out_dir)

component.initialize('Erode_D8_Local.cfg')
component.update(1.0)
component.finalize()
