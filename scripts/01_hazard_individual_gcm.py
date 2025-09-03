import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

ncolumm=3
COLUMN_names=['rt_CMCC', 'rt_CNRM', 'rt_EC-Eart','rt_HadGEM3']
name_file0=['CMCC', 'CNRM', 'EC-Eart','HadGEM3']

COLUMN=COLUMN_names[ncolumm]
name_file=name_file0[ncolumm]
RP_column=COLUMN

basin='WORLD'

path=os.getcwd()
subfolder1='return_periods/'
subfolder0='1_Hazard/'
subfolder2=subfolder0+name_file+'/'
subfolder3=subfolder0+subfolder1

path_HAZADAR= os.path.join(path, subfolder1)
pathOut=os.path.join(path, subfolder2)
os.makedirs(pathOut, exist_ok=True) 
nround=7
variable='velocity'
categories=[29,37.6,43.4,51.1,61.6] # for 10 min maximum wind speed

category='1'
gdp_basin00=gpd.read_file(path_HAZADAR+basin+'_'+variable+'_Category'+category+'.shp')
gdp_basin00['LONGITUDE']= round(gdp_basin00.LONGITUDE,nround)
gdp_basin00['LATITUDE']= round(gdp_basin00.LATITUDE,nround)
gdp_basin=gdp_basin00.copy()
gdp_basin=gdp_basin[gdp_basin['LATITUDE']>-42]
gdp_basin=gdp_basin[gdp_basin['LATITUDE']<42]
gdp1=gdp_basin.reset_index()

category='2'
gdp_basin00=gpd.read_file(path_HAZADAR+basin+'_'+variable+'_Category'+category+'.shp')
gdp_basin00['LONGITUDE']= round(gdp_basin00.LONGITUDE,nround)
gdp_basin00['LATITUDE']= round(gdp_basin00.LATITUDE,nround)
gdp_basin=gdp_basin00.copy()
gdp_basin=gdp_basin[gdp_basin['LATITUDE']>-42]
gdp_basin=gdp_basin[gdp_basin['LATITUDE']<42]
gdp2=gdp_basin.reset_index()

category='3'
gdp_basin00=gpd.read_file(path_HAZADAR+basin+'_'+variable+'_Category'+category+'.shp')
gdp_basin00['LONGITUDE']= round(gdp_basin00.LONGITUDE,nround)
gdp_basin00['LATITUDE']= round(gdp_basin00.LATITUDE,nround)
gdp_basin=gdp_basin00.copy()
gdp_basin=gdp_basin[gdp_basin['LATITUDE']>-42]
gdp_basin=gdp_basin[gdp_basin['LATITUDE']<42]
gdp3=gdp_basin.reset_index()

category='4'
gdp_basin00=gpd.read_file(path_HAZADAR+basin+'_'+variable+'_Category'+category+'.shp')
nround=5
gdp_basin00['LONGITUDE']= round(gdp_basin00.LONGITUDE,nround)
gdp_basin00['LATITUDE']= round(gdp_basin00.LATITUDE,nround)
gdp_basin=gdp_basin00.copy()
gdp_basin=gdp_basin[gdp_basin['LATITUDE']>-42]
gdp_basin=gdp_basin[gdp_basin['LATITUDE']<42]
gdp4=gdp_basin.reset_index()

category='5'
gdp_basin00=gpd.read_file(path_HAZADAR+basin+'_'+variable+'_Category'+category+'.shp')
nround=5
gdp_basin00['LONGITUDE']= round(gdp_basin00.LONGITUDE,nround)
gdp_basin00['LATITUDE']= round(gdp_basin00.LATITUDE,nround)
gdp_basin=gdp_basin00.copy()
gdp_basin=gdp_basin[gdp_basin['LATITUDE']>-42]
gdp_basin=gdp_basin[gdp_basin['LATITUDE']<42]
gdp5=gdp_basin.reset_index()

columns2delete = ['rt_CMCC', 'rt_CNRM', 'rt_EC-Eart', 'rt_HadGEM3', 'ensemble_y', 'ensemble_d', 'ensemble_1', 'spatial_ag', 'agreement']
columns2delete = [m for m in columns2delete if m != COLUMN]

gdp1 = gdp1.drop(columns=columns2delete)
gdp2 = gdp2.drop(columns=columns2delete)
gdp3 = gdp3.drop(columns=columns2delete)
gdp4 = gdp4.drop(columns=columns2delete)
gdp5 = gdp5.drop(columns=columns2delete)

gdp1[RP_column] = gdp1[RP_column].replace(0, np.nan)
gdp2[RP_column] = gdp2[RP_column].replace(0, np.nan)
gdp3[RP_column] = gdp3[RP_column].replace(0, np.nan)
gdp4[RP_column] = gdp4[RP_column].replace(0, np.nan)
gdp5[RP_column] = gdp5[RP_column].replace(0, np.nan)

gdp1[RP_column] = gdp1[RP_column].replace(0, np.nan)
gdp2[RP_column] = gdp2[RP_column].replace(0, np.nan)
gdp3[RP_column] = gdp3[RP_column].replace(0, np.nan)
gdp4[RP_column] = gdp4[RP_column].replace(0, np.nan)
gdp5[RP_column] = gdp5[RP_column].replace(0, np.nan)

gdp1['Return Per'] = gdp1['Return Per'].replace(0, np.nan)
gdp2['Return Per'] = gdp2['Return Per'].replace(0, np.nan)
gdp3['Return Per'] = gdp3['Return Per'].replace(0, np.nan)
gdp4['Return Per'] = gdp4['Return Per'].replace(0, np.nan)
gdp5['Return Per'] = gdp5['Return Per'].replace(0, np.nan)

gdp1.loc[gdp1['Return Per'] > 3000, 'Return Per'] = np.nan
gdp2.loc[gdp2['Return Per'] > 3000, 'Return Per'] = np.nan
gdp3.loc[gdp3['Return Per'] > 3000, 'Return Per'] = np.nan
gdp4.loc[gdp4['Return Per'] > 3000, 'Return Per'] = np.nan
gdp5.loc[gdp5['Return Per'] > 3000, 'Return Per'] = np.nan

gdp1[COLUMN]  = gdp1[COLUMN].replace(0, np.nan)
gdp2[COLUMN]  = gdp2[COLUMN].replace(0, np.nan)
gdp3[COLUMN] = gdp3[COLUMN].replace(0, np.nan)
gdp4[COLUMN] = gdp4[COLUMN].replace(0, np.nan)
gdp5[COLUMN] = gdp5[COLUMN].replace(0, np.nan)

gdp1.loc[gdp1[COLUMN] > 3000, COLUMN] = np.nan
gdp2.loc[gdp2[COLUMN] > 3000, COLUMN] = np.nan
gdp3.loc[gdp3[COLUMN] > 3000, COLUMN] = np.nan
gdp4.loc[gdp4[COLUMN] > 3000, COLUMN] = np.nan
gdp5.loc[gdp5[COLUMN] > 3000, COLUMN] = np.nan

gdp1 = gdp1.dropna(subset=[RP_column], how='all')
gdp2 = gdp2.dropna(subset=[RP_column], how='all')
gdp3 = gdp3.dropna(subset=[RP_column], how='all')
gdp4 = gdp4.dropna(subset=[RP_column], how='all')
gdp5 = gdp5.dropna(subset=[RP_column], how='all')

gdp1 = gdp1.rename(columns={'index_1': 'index'})
gdp2 = gdp2.rename(columns={'index_2': 'index'})
gdp3 = gdp3.rename(columns={'index_3': 'index'})
gdp4 = gdp4.rename(columns={'index_4': 'index'})
gdp5 = gdp5.rename(columns={'index_5': 'index'})

 # Columns to drop
columns_to_drop = ['GID_0', 'NAME_0', 'NAME_1', 'VARNAME_1', 'TYPE_1', 'NAME_2', 'VARNAME_3', 'NAME_4', 'SOVEREIGN', 'LATITUDE', 'LONGITUDE', 'BASIN','Name','geometry']
# Drop the specified columns
gdp2 = gdp2.drop(columns=columns_to_drop)
gdp3 = gdp3.drop(columns=columns_to_drop)
gdp4 = gdp4.drop(columns=columns_to_drop)
gdp5 = gdp5.drop(columns=columns_to_drop)

# column contents no need to be the same, it will append
gdp1 = gdp1.rename(columns=lambda col: col + '_1' if col not in ['index','LONGITUDE','LATITUDE','GID_0','NAME_0','NAME_1','VARNAME_1','TYPE_1','NAME_2','VARNAME_3','NAME_4','SOVEREIGN','BASIN','Name','geometry'] else col)
gdp2 = gdp2.rename(columns=lambda col: col + '_2'if col not in ['index'] else col)
gdp3 = gdp3.rename(columns=lambda col: col + '_3'if col not in ['index'] else col)
gdp4 = gdp4.rename(columns=lambda col: col + '_4'if col not in ['index'] else col)
gdp5 = gdp5.rename(columns=lambda col: col + '_5'if col not in ['index'] else col)

CAT = pd.merge(gdp1, gdp2, on=['index'],how="left")
CAT = pd.merge(CAT, gdp3, on=['index'],how="left")
CAT = pd.merge(CAT, gdp4, on=['index'],how="left")
CAT = pd.merge(CAT, gdp5, on=['index'],how="left")

CAT.columns = [col.replace(COLUMN+'_', 'RPCC') for col in CAT.columns]
CAT.columns = [col.replace('Return Per_', 'RPH') for col in CAT.columns]
CAT.columns = [col.replace('Wind Speed_', 'WindS') for col in CAT.columns]



#  identifiy the maximum category
cat_hist=CAT[['RPH1','RPH2','RPH3','RPH4','RPH5']]
cat_cc=CAT[['RPCC'+'1','RPCC'+'2','RPCC'+'3','RPCC'+'4','RPCC'+'5']]
#cat_cc=CAT[[folder_out[ncolumm]+'1',folder_out[ncolumm]+'2',folder_out[ncolumm]+'3',folder_out[ncolumm]+'4',folder_out[ncolumm]+'5']]

cat_hist=cat_hist/cat_hist
cat_hist[cat_hist.columns[0]]=cat_hist[cat_hist.columns[0]]-cat_hist[cat_hist.columns[0]]+1
cat_hist[cat_hist.columns[1]]=cat_hist[cat_hist.columns[1]]-cat_hist[cat_hist.columns[1]]+2
cat_hist[cat_hist.columns[2]]=cat_hist[cat_hist.columns[2]]-cat_hist[cat_hist.columns[2]]+5
cat_hist[cat_hist.columns[3]]=cat_hist[cat_hist.columns[3]]-cat_hist[cat_hist.columns[3]]+10
cat_hist[cat_hist.columns[4]]=cat_hist[cat_hist.columns[4]]-cat_hist[cat_hist.columns[4]]+20
cat_hist['max_CAT']=cat_hist.max(axis=1)

cat_cc=cat_cc/cat_cc
cat_cc[cat_cc.columns[0]]=cat_cc[cat_cc.columns[0]]-cat_cc[cat_cc.columns[0]]+1
cat_cc[cat_cc.columns[1]]=cat_cc[cat_cc.columns[1]]-cat_cc[cat_cc.columns[1]]+2
cat_cc[cat_cc.columns[2]]=cat_cc[cat_cc.columns[2]]-cat_cc[cat_cc.columns[2]]+5
cat_cc[cat_cc.columns[3]]=cat_cc[cat_cc.columns[3]]-cat_cc[cat_cc.columns[3]]+10
cat_cc[cat_cc.columns[4]]=cat_cc[cat_cc.columns[4]]-cat_cc[cat_cc.columns[4]]+20
cat_cc['max_CAT']=cat_cc.max(axis=1)

CAT['H_cat'] = np.where(
    cat_hist['max_CAT'].isna() & cat_cc['max_CAT'].isna(),
    np.nan,
    cat_cc['max_CAT'].fillna(0)-cat_hist['max_CAT'].fillna(0))


#CALCULATING THE FREQUENCY OF HISTORICAL TROPICAL CYCLONES ###########################################################
H=CAT[['RPH1','RPH2','RPH3','RPH4','RPH5']]
H=1/H

H.replace([np.inf, -np.inf], np.nan, inplace=True)

CAT['H_hist_minor'] = np.where(H.iloc[:, 0].isna() & H.iloc[:, 1].isna(), np.nan,
    H.iloc[:, 0].fillna(0) * 1 + H.iloc[:, 1].fillna(0) * 2)

CAT['H_hist_major'] = np.where(H.iloc[:, 2].isna() & H.iloc[:, 3].isna()  & H.iloc[:, 4].isna(), np.nan,
    H[H.columns[2]].fillna(0) * 5 + H[H.columns[3]].fillna(0) * 10 + H[H.columns[4]].fillna(0) * 20)

#HAZARD CLIMATE CHANGE ###############################################################################################
HCC=CAT[['RPCC1','RPCC2','RPCC3','RPCC4','RPCC5']]
HCC=1/HCC
HCC.replace([np.inf, -np.inf], np.nan, inplace=True)

CAT['H_CC_minor'] = np.where(HCC.iloc[:, 0].isna() & HCC.iloc[:, 1].isna(), np.nan,
    HCC.iloc[:, 0].fillna(0) * 1 + HCC.iloc[:, 1].fillna(0) * 2)

CAT['H_CC_major'] = np.where(HCC.iloc[:, 2].isna() & HCC.iloc[:, 3].isna()  & HCC.iloc[:, 4].isna(), np.nan,
    HCC[HCC.columns[2]].fillna(0) * 5 + HCC[HCC.columns[3]].fillna(0) * 10 + HCC[HCC.columns[4]].fillna(0) * 20)

CAT['HF_minor'] = np.subtract(CAT['H_CC_minor'], CAT['H_hist_minor'])
CAT['HF_major'] = np.subtract(CAT['H_CC_major'], CAT['H_hist_major'])

#Classification in climatic regions
dif_Hminor=CAT['HF_minor'].copy()
dif_Hminor[dif_Hminor<0]=-1
dif_Hminor[dif_Hminor>0]=1
dif_Hminor[dif_Hminor==0]=0
dif_Hminor[(CAT['H_CC_minor'].isna()) & (~CAT['H_hist_minor'].isna())] = 2
dif_Hminor[(~CAT['H_CC_minor'].isna()) & (CAT['H_hist_minor'].isna())] = 3
dif_Hminor[np.isnan(dif_Hminor)]=-999

dif_Hmajor=CAT['HF_major'].copy()
dif_Hmajor[dif_Hmajor<0]=-1
dif_Hmajor[dif_Hmajor>0]=1
dif_Hmajor[dif_Hmajor==0]=0
dif_Hmajor[(CAT['H_CC_major'].isna()) & (~CAT['H_hist_major'].isna())] = 2
dif_Hmajor[(~CAT['H_CC_major'].isna()) & (CAT['H_hist_major'].isna())] = 3
dif_Hmajor[np.isnan(dif_Hmajor)]=-999

df=CAT.copy()
df['A']=CAT['H_cat'].copy()
df['B']=dif_Hmajor.copy()
df['C']=dif_Hminor.copy()
df['class']=df['A'].copy()
df['class']=np.nan
df.loc[np.isnan(df['A']), 'A'] = -999

df['CATtext']=df['class'].copy()
df['HMtext']=df['class'].copy()
df['Hmtext']=df['class'].copy()


class0=[0]
a=[-999]
b=[-999]
c=[-999]
atext=['none TC in any scenario']
btext=['No major TC in any scenario']
ctext=['No minor TC in any scenario']

A=[-20,-19,-18,-15,-10,-9,-8,-5,-4,-3,-2,-1,0,1,2,3,4,5,8,9,10,15,18,19,20]
B=[-999,-1,0,1,2,3]
C=[-999,-1,0,1,2,3]

""" Atext=['from 5 to 1','from 5 to 2','from 5 to 3','from 5 to 2','from 4 to 1', 'from 4 to 2', 'from 4 to 3', 'from 3 to 1','from 3 to 2', 'from 2 to none', 'from 1 to none','without changes',
'from none to 1', 'from none to 2',	'from 2 to 3',	 'from 1 to 3',	 'from 3 to 4',	 'from 2 to 4',	'from 1 to 4',	'from 2 to 5',	'from 3 to 5',	'from 2 to 5',	'from 1 to 5'] """

Atext=['from 5 to none','from 5 to 1','from 5 to 2','from 5 to 3','from 5 to 2/4 to none','from 4 to 1','from 4 to 2','from 4 to 3/3 to none','from 3 to 1','from 3 to 2', 'from 2 to none', 'from 1 to none','without changes','from none to 1', 'from none to 2'
	 ,'from 2 to 3','from 1 to 3','from 3 to 4/none to 3','from 2 to 4','from 1 to 4','from 2 to 5/none to 4','from 3 to 5','from 2 to 5','from 1 to 5','from none to 5']

Btext = [ 'No major TC in any scenario', 'Major TC frequency decreases in SSP5-8.5 scenario',    'Major TC frequency remains the same',
    'Major TC frequency increases in SSP5-8.5 scenario',    'Major TCs exist in the historical period but not in the SSP5-8.5 scenario', 'Major TCs exist in the SSP5-8.5 period but not in the historical scenario']

Ctext= ['No minor TC in any scenario','Minor TC frequency decreases in SSP5-8.5 scenario','Minor TC frequency remains the same','Minor TC frequency increases in SSP5-8.5 scenario',
    'Minor TCs exist in the historical period but not in the SSP5-8.5 scenario', 'Minor TCs exist in the SSP5-8.5 period but not in the historical scenario']

iclass=1

for ia in range(len (A)):
    for ib in range(len (B)):
        for ic in range(len (C)):
            a.append(A[ia])
            b.append(B[ib])
            c.append(C[ic])
            atext.append(Atext[ia])
            btext.append(Btext[ib])
            ctext.append(Ctext[ic])
            iclass=iclass+1
            class0.append(iclass)

df['class']=df['H_cat'].copy()+np.nan
for nclass in range(len (class0)):
    df.loc[	(df['A'] == a[nclass]) & (df['B'] == b[nclass]) & (df['C'] == c[nclass]) , 'class'] = class0[nclass]
    df.loc[	(df['CATtext'] == a[nclass]) & (df['HMtext'] == b[nclass]) & (df['Hmtext'] == c[nclass]) , 'class'] = class0[nclass]

#unique_rows = np.unique(df[['A', 'B', 'C']].values, axis=0)
unique_rows = df[['A', 'B', 'C','class']].drop_duplicates()

# Count the number of unique rows
num_unique_rows = unique_rows.shape[0]

classification_list = pd.DataFrame({
    'class': class0,
    'HCat': a,
    'HCat (description)': atext,
    'HFmajor': b,
    'HFmajor (description)': btext,
    'HFminor': c,
    'HFminor (description)': ctext,
})

unique_classes = np.unique(df['class'])
climatic_regions_GCM=classification_list[classification_list['class'].isin(unique_classes)]
classification_list.to_excel(pathOut+'TC_regions.xlsx', sheet_name='List_climatic_regions', index=False)
climatic_regions_GCM.to_excel(pathOut+'TC_regions_'+name_file+'.xlsx',sheet_name=name_file, index=False)

# categoriza the hazard 

a0=abs(CAT['H_cat']).min(skipna=True)
a1=abs(CAT['H_cat']).max(skipna=True)
a_sign=np.sign(CAT['H_cat'])

b0=abs(CAT['HF_major']).min(skipna=True)
b1=abs(CAT['HF_major']).max(skipna=True)
b_sign=np.sign(CAT['HF_major'])

c0=abs(CAT['HF_minor']).min(skipna=True)
c1=abs(CAT['HF_minor']).max(skipna=True)
c_sign=np.sign(CAT['HF_minor'])

H_cat=a_sign*(abs(CAT['H_cat'])-a0)/(a1-a0)
HF_minor=c_sign*(abs(CAT['HF_minor'])-c0)/(c1-c0)
HF_major=b_sign*(abs(CAT['HF_major'])-b0)/(b1-b0)

#df['TC3_hazard']=np.where(H_cat.isna() |   HF_minor.isna() |    HF_major.isna(),  np.nan,  H_cat.fillna(0)+HF_minor.fillna(0)+HF_major.fillna(0))
df['TC3_hazard']=H_cat.fillna(0)+HF_minor.fillna(0)+HF_major.fillna(0)

d0=df['TC3_hazard'].min(skipna=True)
d1=df['TC3_hazard'].max(skipna=True)

d0=abs(df['TC3_hazard']).min(skipna=True)
d1=abs(df['TC3_hazard']).max(skipna=True)
d_sign=np.sign(df['TC3_hazard'])

df['TC3_hazard']=d_sign*(abs(df['TC3_hazard'])-d0)/(d1-d0)

df['H_cat']    = H_cat
df['HF_major'] = HF_major
df['HF_minor'] = HF_minor

df.to_file(pathOut+'\\0_hazard_'+name_file+'_v1.shp')


