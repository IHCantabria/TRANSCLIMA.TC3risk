import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os



ncolumm=0
COLUMN_names=['ensemble_y','rt_CMCC', 'rt_CNRM', 'rt_EC-Eart','rt_HadGEM3']
name_file0=['ensemble_hazard','CMCC', 'CNRM', 'EC-Eart','HadGEM3']
folder_out=['ENSEMBLE','CMCC', 'CNRM', 'EC-Eart','HadGEM3']

COLUMN=COLUMN_names[ncolumm]
name_file=folder_out[ncolumm]

basin='WORLD'

path=os.getcwd()

subfolder1='1_Hazard'
subfolder2=subfolder1+'/'+name_file+'/'+''
path_h= os.path.join(path, subfolder2)

subfolder1='2_Exposure'
subfolder2=subfolder1+'/'+name_file+'/'+''
path_EXP= os.path.join(path, subfolder1)

subfolder1='3_Adaptive_Capacity'
subfolder2=subfolder1+'/'+name_file+'/'+''
path_AC= os.path.join(path, subfolder1)

subfolder1='4_Risk'
pathOut= os.path.join(path, subfolder1)
os.makedirs(pathOut, exist_ok=True) 

path_HAZARD=path_h+'/climatic_regions_ENSEMBLE_monte_carlo_v1.shp'
path_EXP2020=path_EXP+'/Worldpop_coastal_adm04.shp'
path_popgrowth=path_EXP+'/WORLD__popGrowth_SSP5_2020_adm04.shp'
path_AC=path_AC+'/Adaptive_indicators_1.shp'

nround=7
hazard=gpd.read_file(path_HAZARD)
pop=gpd.read_file(path_EXP2020)
popgrowth=gpd.read_file(path_popgrowth)
adaptive_capacity=gpd.read_file(path_AC)


popgrowth=popgrowth[['LATITUDE', 'LONGITUDE', 'popgrowth']]
pop=pop[['LATITUDE', 'LONGITUDE', 'population']]
adaptive_capacity=adaptive_capacity[['LATITUDE', 'LONGITUDE', 'Ind_norm']]

#################################################################################################

hazard['LONGITUDE']= round(hazard.LONGITUDE,nround)
hazard['LATITUDE']= round(hazard.LATITUDE,nround)

######################################################################################################
pop['LONGITUDE']= round(pop.LONGITUDE,nround)
pop['LATITUDE']= round(pop.LATITUDE,nround)
pop=pop[pop['population']>0]
pop=pop[pop['LATITUDE']>-42]
pop=pop[pop['LATITUDE']<42]

######################################################################################################
popgrowth['LONGITUDE']= round(popgrowth.LONGITUDE,nround)
popgrowth['LATITUDE']= round(popgrowth.LATITUDE,nround)
popgrowth=popgrowth[popgrowth['popgrowth']>0]
popgrowth=popgrowth[popgrowth['LATITUDE']>-42]
popgrowth=popgrowth[popgrowth['LATITUDE']<42]

######################################################################################################
adaptive_capacity=adaptive_capacity[adaptive_capacity['Ind_norm']>0]
adaptive_capacity=adaptive_capacity[adaptive_capacity['LATITUDE']>-42]
adaptive_capacity=adaptive_capacity[adaptive_capacity['LATITUDE']<42]
adaptive_capacity['LONGITUDE']= round(adaptive_capacity.LONGITUDE,nround)
adaptive_capacity['LATITUDE']= round(adaptive_capacity.LATITUDE,nround)

pop0=pd.merge(pop, popgrowth, on=['LATITUDE','LONGITUDE'],how="left")
pop0['poptotal'] = pop0[['population', 'popgrowth']].sum(axis=1, min_count=1)


car = pd.merge(pop0, adaptive_capacity, on=['LATITUDE','LONGITUDE'],how="left")
hazard['LATITUDE'] = hazard['LATITUDE'].astype(float)
hazard['LONGITUDE'] = hazard['LONGITUDE'].astype(float)
car['LATITUDE'] = car['LATITUDE'].astype(float)
car['LONGITUDE'] = car['LONGITUDE'].astype(float)
hazard['LATITUDE'] = hazard['LATITUDE'].round(5)
hazard['LONGITUDE'] = hazard['LONGITUDE'].round(5)
car['LATITUDE'] = car['LATITUDE'].round(5)
car['LONGITUDE'] = car['LONGITUDE'].round(5)
risk = pd.merge(hazard, car, on=['LATITUDE','LONGITUDE'],how="left")


# #VULNERABILITY ###################################################################################
V=risk['Ind_norm']  # from 0 to 1

#EXPOSURE ########################################################################################
# convierto la población a escala logaritmica para filtrar la diferencia entre poblaciones
risk['pop20log'] = np.log(risk['poptotal']+1)
maxEXP=np.nanmax(risk['pop20log'])
maxEXP=maxEXP.max()
minEXP=0

E_2020=(risk['pop20log']-minEXP)/(maxEXP-minEXP) # convert from 0 to 1
risk['popG_2020']=E_2020

#RISK ########################################################################################
risk['TC3_risk']=risk['TC3_mean']*risk['popG_2020']/risk['Ind_norm']

a0=abs(risk['TC3_risk']).min(skipna=True)
a1=abs(risk['TC3_risk']).max(skipna=True)
a_sign=np.sign(risk['TC3_risk'])
risk['TC3_riskn']=a_sign*(abs(risk['TC3_risk'])-a0)/(a1-a0)

#save #######################################################################################
risk.to_file(pathOut+'/TC3_risk.shp')



