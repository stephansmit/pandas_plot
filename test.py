import pandas as pd
from plot import *
import os
df = pd.read_csv("test.csv")
print(df.columns)
plot3Yaxis(df,      
              "NumberBlades", "Blades", "#", "{0:.2f}",
               "RotationSpeedHz", "Rotational Speed", "Hz", "%0.2f",
               "Outflow_beta", "Rel.Flow Angle at Outlet", "Deg.", "%0.2f",
               "Outflow_alpha", "Abs. Flow Angle at Outlet", "Deg.", "%0.2f", 
               "Interface_beta", "Rel. Flow Angle at Interface", "Deg.",  "%0.2f",
               os.getcwd(), 'test', color=False)


#print(df)
