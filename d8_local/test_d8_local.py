"""IRF with the D8Local component."""
import os
from topoflow.components.d8_local import d8_component as Model


component = Model()
print component.get_component_name()

out_dir = 'out'
if os.path.exists(out_dir) is False:
    os.mkdir(out_dir)

component.initialize('D8_Local.cfg')
component.update()
component.finalize()
