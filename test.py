import pandas as pd
from plot import *
import os
df = pd.read_csv("test.csv")

plot3Yaxis(df,  "NumberBlades", "Blades", "#", "{0:.2f}",
               "RotationSpeedHz", "Rotational Speed", "Hz", "%0.2f",
               "Interface_alpha", "Abs.Flow Angle at Interface", "Deg", "%0.2f",
               "Interface_beta", "Rel. Flow Angle at Interface", "Deg", "%0.2f", 
               "Interface_Static_P", "Static Pressure at Outlet", "Pa",  "%0.2f",
               os.getcwd(), 'angles_interface', color=True)
plot3Yaxis(df,  "NumberBlades", "Blades", "#", "{0:.2f}",
               "RotationSpeedHz", "Rotational Speed", "Hz", "%0.2f",
               "Outflow_beta", "Rel.Flow Angle at Outlet", "Deg.", "%0.2f",
               "Outflow_alpha", "Abs. Flow Angle at Outlet", "Deg.", "%0.2f", 
               "Interface_beta", "Rel. Flow Angle at Interface", "Deg.",  "%0.2f",
               os.getcwd(), 'angles', color=True)

plot3Yaxis(df, "NumberBlades", "Blades", "#", "{0:.2f}",
               "RotationSpeedHz", "Rotational Speed", "Hz", "%0.2f",
               "Outflow_Static_P", "Static Pressure Outlet", "Pa", "%0.2f",
               "Interface_Static_P", "Static Pressure at Interface", "Pa", "%0.2f", 
               "DegreeOfReaction", "Degree of Reaction", '-',  "%0.2f",
               os.getcwd(), 'pressures', color=True)

plot3Yaxis(df, "NumberBlades", "Blades", "#", "{0:.2f}",
               "RotationSpeedHz", "Rotational Speed", "Hz", "%0.2f",
               "TotalToStatic", "Total-to-Static Efficiency", "%", "%0.2f",
               "TotalToTotal", "Total-to-Total Efficiency", "%", "%0.2f", 
               "Power", "Specific Power", 'kJ/kg',  "%0.2f",
               os.getcwd(), 'power', color=True)

plot2Yaxis(df, "NumberBlades", "Blades", "#", "{0:.2f}",
               "RotationSpeedHz", "Rotational Speed", "Hz", "%0.2f",
               "Outflow_Absolute_thetavel", "Outflow Abs. Tang. Velocity:","m/s", "%0.2f",
               "Outflow_Relative_thetavel", "Outflow Rel. Tang. Velocity", "m/s", "%0.2f",
               os.getcwd(), 'velocity', color=True)
