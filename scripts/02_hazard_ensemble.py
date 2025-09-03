import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

ncolumm=0
name_file0=['ENSEMBLE','CMCC', 'CNRM', 'EC-Eart','HadGEM3']
RP_column=['rt_CMCC', 'rt_CNRM', 'rt_EC-Eart','rt_HadGEM3']
COLUMN=['rt_CMCC', 'rt_CNRM', 'rt_EC-Eart','rt_HadGEM3']
name_file=name_file0[0]

path=os.getcwd()
subfolder1='1_Hazard'
subfolder2=subfolder1+'/'+name_file+'/'

path_HAZADAR= os.path.join(path, subfolder1)
pathOut=os.path.join(path, subfolder2)
os.makedirs(pathOut, exist_ok=True) 

n_samples = 1000  


gcm1=gpd.read_file(path_HAZADAR+'/'+name_file0[1]+'/'+'0_hazard_'+name_file0[1]+'_v1.shp')
gcm2=gpd.read_file(path_HAZADAR+'/'+name_file0[2]+'/'+'0_hazard_'+name_file0[2]+'_v1.shp')
gcm3=gpd.read_file(path_HAZADAR+'/'+name_file0[3]+'/'+'0_hazard_'+name_file0[3]+'_v1.shp')
gcm4=gpd.read_file(path_HAZADAR+'/'+name_file0[4]+'/'+'0_hazard_'+name_file0[4]+'_v1.shp')

gdp1=gcm1.copy()
gdp2=gcm2.copy()
gdp3=gcm3.copy()
gdp4=gcm4.copy()

columns1=[ 'RPH1', 'WindS1', 'RPCC1', 'RPH2', 'WindS2', 'RPCC2', 'RPH3', 'WindS3', 'RPCC3', 'RPH4', 'WindS4', 'RPCC4', 'RPH5', 'WindS5', 'RPCC5',
           'H_cat', 'H_hist_min', 'H_hist_maj', 'H_CC_minor', 'H_CC_major', 'HF_minor', 'HF_major', 'A', 'B', 'C']

columns2=['GID_0', 'NAME_0', 'NAME_1', 'VARNAME_1', 'TYPE_1', 'NAME_2', 'VARNAME_3', 'NAME_4', 'SOVEREIGN', 'LATITUDE', 'LONGITUDE', 'BASIN', 'Name','RPH1', 'WindS1', 'RPCC1', 'RPH2', 'WindS2', 'RPCC2', 'RPH3', 'WindS3', 'RPCC3', 'RPH4', 'WindS4', 'RPCC4', 'RPH5', 'WindS5', 'RPCC5',
           'H_cat', 'H_hist_min', 'H_hist_maj', 'H_CC_minor', 'H_CC_major', 'HF_minor', 'HF_major', 'A', 'B', 'C']

gcm1 = gcm1.drop(columns=columns1)
gcm2 = gcm2.drop(columns=columns2)
gcm3 = gcm3.drop(columns=columns2)
gcm4 = gcm4.drop(columns=columns2)

# column contents no need to be the same, it will append
gcm1 = gcm1.rename(columns=lambda col: col + '_1' if col not in ['index','LONGITUDE','LATITUDE','GID_0','NAME_0','NAME_1','VARNAME_1','TYPE_1','NAME_2','VARNAME_3','NAME_4','SOVEREIGN','BASIN','Name','geometry'] else col)
gcm2 = gcm2.rename(columns=lambda col: col + '_2'if col not in ['index'] else col)
gcm3 = gcm3.rename(columns=lambda col: col + '_3'if col not in ['index'] else col)
gcm4 = gcm4.rename(columns=lambda col: col + '_4'if col not in ['index'] else col)

GCM = pd.merge(gcm1, gcm2, on=['index'],how="outer")
GCM = pd.merge(GCM, gcm3, on =['index'],how="outer")
GCM = pd.merge(GCM, gcm4, on =['index'],how="outer")

GCM=GCM[['index','class_1','class_2','class_3','class_4']]


columns2delete=['H_cat', 'H_hist_min', 'H_hist_maj', 'H_CC_minor', 'H_CC_major',
       'HF_minor', 'HF_major', 'A', 'B', 'C', 'class', 'TC3_hazard']

gdp1 = gdp1.drop(columns=columns2delete)
gdp2 = gdp2.drop(columns=columns2delete)
gdp3 = gdp3.drop(columns=columns2delete)
gdp4 = gdp4.drop(columns=columns2delete)

columns2delete=['GID_0', 'NAME_0', 'NAME_1', 'VARNAME_1', 'TYPE_1', 'NAME_2',
       'VARNAME_3', 'NAME_4', 'SOVEREIGN', 'LATITUDE', 'LONGITUDE', 'BASIN',
       'Name']

column_name=['index','GID_0', 'NAME_0', 'NAME_1', 'VARNAME_1', 'TYPE_1', 'NAME_2',
       'VARNAME_3', 'NAME_4', 'SOVEREIGN', 'LATITUDE', 'LONGITUDE', 'BASIN',
       'Name','geometry']

g2_name=gdp2[column_name]
g3_name=gdp3[column_name]
g4_name=gdp4[column_name]

gdp2 = gdp2.drop(columns=columns2delete)
gdp3 = gdp3.drop(columns=columns2delete)
gdp4 = gdp4.drop(columns=columns2delete)

# column contents no need to be the same, it will append
gdp1 = gdp1.rename(columns=lambda col: col + '_1' if col not in ['index','LONGITUDE','LATITUDE','GID_0','NAME_0','NAME_1','VARNAME_1','TYPE_1','NAME_2','VARNAME_3','NAME_4','SOVEREIGN','BASIN','Name','geometry'] else col)
gdp2 = gdp2.rename(columns=lambda col: col + '_2'if col not in ['index'] else col)
gdp3 = gdp3.rename(columns=lambda col: col + '_3'if col not in ['index'] else col)
gdp4 = gdp4.rename(columns=lambda col: col + '_4'if col not in ['index'] else col)

gdp1 = gdp1.rename(columns={'index_1': 'index'})
gdp2 = gdp2.rename(columns={'index_2': 'index'})
gdp3 = gdp3.rename(columns={'index_3': 'index'})
gdp4 = gdp4.rename(columns={'index_4': 'index'})

CAT = pd.merge(gdp1, gdp2, on=['index'],how="outer")
CAT = pd.merge(CAT, gdp3, on =['index'],how="outer")
CAT = pd.merge(CAT, gdp4, on =['index'],how="outer")

CAT.columns = [col.replace('Return Per_', 'RPH') for col in CAT.columns]
CAT.columns = [col.replace('Wind Speed_', 'WindS') for col in CAT.columns]

CAT = CAT.merge(g4_name[['index'] + columns2delete], on='index', how='left', suffixes=('', '_new'))

# Replace NaN values in original columns with the new values
for col in columns2delete:
    CAT[col] = CAT[col].combine_first(CAT[col + '_new'])

# Drop the extra columns
CAT = CAT.drop(columns=[col + '_new' for col in columns2delete])

CAT0 = pd.merge(CAT, GCM, on=['index'],how="left")

a=CAT0['class_1']/CAT0['class_1']
b=CAT0['class_2']/CAT0['class_2']
c=CAT0['class_3']/CAT0['class_3']
d=CAT0['class_4']/CAT0['class_4']

a=np.round(a, 0)
b=np.round(b, 0)
c=np.round(c, 0)
d=np.round(d, 0)

CAT0['class_1']=a
CAT0['class_2']=b
CAT0['class_3']=c
CAT0['class_4']=d

CAT0['nmodels']=np.nansum(CAT0[['class_1','class_2','class_3','class_4']],axis=1)


column=['RPH1_1','RPH1_2','RPH1_3','RPH1_4']
df0=CAT[column].copy()
df0['RPH1'] = df0.apply(lambda row: row.iloc[0] if row.nunique() == 1 else row.first_valid_index(), axis=1)
CAT['RPH1']=df0['RPH1'].copy()
CAT = CAT.drop(columns=column)
df0 = df0.drop(columns=column)

column=['RPH2_1','RPH2_2','RPH2_3','RPH2_4']
df0=CAT[column].copy()
df0['RPH2'] = df0.apply(lambda row: row.iloc[0] if row.nunique() == 1 else row.first_valid_index(), axis=1)
df0 = df0.drop(columns=column)
CAT['RPH2']=df0['RPH2'].copy()
CAT = CAT.drop(columns=column)

column=['RPH3_1','RPH3_2','RPH3_3','RPH3_4']
df0=CAT[column].copy()
df0['RPH3'] = df0.apply(lambda row: row.iloc[0] if row.nunique() == 1 else row.first_valid_index(), axis=1)
df0 = df0.drop(columns=column)
CAT['RPH3']=df0['RPH3'].copy()
CAT = CAT.drop(columns=column)

column=['RPH4_1','RPH4_2','RPH4_3','RPH4_4']
df0=CAT[column].copy()
df0['RPH4'] = df0.apply(lambda row: row.iloc[0] if row.nunique() == 1 else row.first_valid_index(), axis=1)
df0 = df0.drop(columns=column)
CAT['RPH4']=df0['RPH4'].copy()
CAT = CAT.drop(columns=column)

column=['RPH5_1','RPH5_2','RPH5_3','RPH5_4']
df0=CAT[column].copy()
df0['RPH5'] = df0.apply(lambda row: row.iloc[0] if row.nunique() == 1 else row.first_valid_index(), axis=1)
df0 = df0.drop(columns=column)
CAT['RPH5']=df0['RPH5'].copy()
CAT = CAT.drop(columns=column)


column1=['RPCC1_1','RPCC1_2','RPCC1_3','RPCC1_4']
column2=['RPCC2_1','RPCC2_2','RPCC2_3','RPCC2_4']
column3=['RPCC3_1','RPCC3_2','RPCC3_3','RPCC3_4']
column4=['RPCC4_1','RPCC4_2','RPCC4_3','RPCC4_4']
column5=['RPCC5_1','RPCC5_2','RPCC5_3','RPCC5_4']

std1        = np.nanstd(CAT[column1], axis=1)
mean1       = np.nanmean(CAT[column1], axis=1)

std2        = np.nanstd(CAT[column2], axis=1)
mean2       = np.nanmean(CAT[column2], axis=1)

std3        = np.nanstd(CAT[column3], axis=1)
mean3       = np.nanmean(CAT[column3], axis=1)

std4        = np.nanstd(CAT[column4], axis=1)
mean4       = np.nanmean(CAT[column4], axis=1)

std5        = np.nanstd(CAT[column5], axis=1)
mean5       = np.nanmean(CAT[column5], axis=1)

#samples = np.random.normal(mean1, std1, size=(len(mean1), n_samples))
samples1 = np.random.normal(mean1[:, np.newaxis], std1[:, np.newaxis], size=(len(mean1), n_samples))
samples2 = np.random.normal(mean2[:, np.newaxis], std2[:, np.newaxis], size=(len(mean2), n_samples))
samples3 = np.random.normal(mean3[:, np.newaxis], std3[:, np.newaxis], size=(len(mean3), n_samples))
samples4 = np.random.normal(mean4[:, np.newaxis], std4[:, np.newaxis], size=(len(mean4), n_samples))
samples5 = np.random.normal(mean5[:, np.newaxis], std5[:, np.newaxis], size=(len(mean5), n_samples))


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

CAT['class']=CAT['RPH1'].copy()+np.nan

index_HCAT   = np.empty((len(CAT), n_samples))
index_Hminor = np.empty((len(CAT), n_samples))
index_Hmajor = np.empty((len(CAT), n_samples))
result_class = np.empty((len(CAT), n_samples))
result_TC3   = np.empty((len(CAT), n_samples))

for nsample in range(n_samples):

    CAT['RPCC1']=samples1[:,nsample]
    CAT['RPCC2']=samples2[:,nsample]
    CAT['RPCC3']=samples3[:,nsample]
    CAT['RPCC4']=samples4[:,nsample]
    CAT['RPCC5']=samples5[:,nsample]

    #identify category
    #with HIST and the four GCM tr 
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

    CAT['H_cat'] = np.where(cat_hist['max_CAT'].isna() & cat_cc['max_CAT'].isna(), np.nan, cat_cc['max_CAT'].fillna(0)-cat_hist['max_CAT'].fillna(0))

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

    CAT['H_cat'] = np.where(cat_hist['max_CAT'].isna() & cat_cc['max_CAT'].isna(), np.nan, cat_cc['max_CAT'].fillna(0)-cat_hist['max_CAT'].fillna(0))

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

    for nclass in range(len (class0)):
        df.loc[	(df['A'] == a[nclass]) & (df['B'] == b[nclass]) & 	(df['C'] == c[nclass]) , 'class'] = class0[nclass]

    #unique_rows = np.unique(df[['A', 'B', 'C']].values, axis=0)
    unique_rows = df[['A', 'B', 'C','class']].drop_duplicates()
    
    #df['Dispersion']=dispersion
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

    result_class[:,nsample]=df['class'].values

    ##########################################################################
    #for each smaple calculate the tropical climate change hazard 
    #df['H_cat']=df['H_cat'].replace([np.inf, -np.inf], np.nan, inplace=True)
    a0=abs(CAT['H_cat']).min(skipna=True)
    a1=abs(CAT['H_cat']).max(skipna=True)
    a_sign=np.sign(CAT['H_cat'])
    H_cat=a_sign*(abs(CAT['H_cat'])-a0)/(a1-a0)

    #df['HF_major']=df['HF_major'].replace([np.inf, -np.inf], np.nan, inplace=True)
    b0=CAT['HF_major'].min(skipna=True)
    b1=CAT['HF_major'].max(skipna=True)
    b_sign=np.sign(CAT['HF_major'])
    HF_major=b_sign*(abs(CAT['HF_major'])-b0)/(b1-b0)

    #df['HF_minor']=CAT['HF_minor'].replace([np.inf, -np.inf], np.nan, inplace=True)
    c0=CAT['HF_minor'].min(skipna=True)
    c1=CAT['HF_minor'].max(skipna=True)
    c_sign=np.sign(CAT['HF_minor'])
    HF_minor=c_sign*(abs(CAT['HF_minor'])-c0)/(c1-c0)

    #df['TC3_hazard']=np.where(H_cat.isna() |   HF_minor.isna() |    HF_major.isna(),  np.nan,  H_cat.fillna(0)+HF_minor.fillna(0)+HF_major.fillna(0))
    TC3_hazard=H_cat.fillna(0)+HF_minor.fillna(0)+HF_major.fillna(0)
    TC3_hazard=H_cat.fillna(0)+HF_minor.fillna(0)+HF_major.fillna(0)
    d0=abs(TC3_hazard).min(skipna=True)
    d1=abs(TC3_hazard).max(skipna=True)
    d_sign=np.sign(TC3_hazard)

    index_HCAT[:,nsample]   = H_cat
    index_Hminor[:,nsample] = HF_minor
    index_Hmajor[:,nsample] = HF_major
    result_TC3[:,nsample]   = d_sign*(abs(TC3_hazard)-d0)/(d1-d0)


climatic_region = []
probabilities   = []
dispersion      = []

for row in result_class:
    # Find unique values and their counts in the row
    unique, counts = np.unique(row, return_counts=True)
    prob = counts / n_samples  # Probability of occurrence
    max_count = np.nanmax(counts)
    max_value = unique[counts == max_count]    # Get unique values with max count
    max_prob = prob[counts == max_count]       # Get corresponding probabilities
    max_prob = prob[counts == max_count]       # Get corresponding probabilities
    H = -np.sum(prob * np.log2(prob + 1e-10))  # Dispersion de la probabilidad (entropia) +1e-10 para evitar log(0)
    dispersion.append(H)
    climatic_region.append(max_value[0])
    probabilities.append(max_prob[0])
    
a1=max(dispersion)
b1=min(dispersion)
dispersion=(dispersion-b1)/(a1-b1)

df['region']=climatic_region
df['prob_region']=probabilities
df['Disp_region']=dispersion

## con los valores de toda la muestra calculo 
# Cálculo de la desviación estándar (std) del índice de peligro
df['TC3_mean'] = np.nanmean(result_TC3,axis=1)
df['TC3_std'] = np.nanstd(result_TC3,axis=1)

# Cálculo de los intervalos de confianza del 95% (percentiles)
df['TC3_cilower'] = np.nanpercentile(result_TC3, 2.5,axis=1)
df['TC3_ciupper'] = np.nanpercentile(result_TC3, 97.5,axis=1)

df['HCAT_mean'] = np.nanmean(index_HCAT,axis=1)
df['HCAT_std'] = np.nanstd(index_HCAT,axis=1)

df['Hmajor_mean'] = np.nanmean(index_Hmajor,axis=1)
df['Hmajor_std'] = np.nanstd(index_Hmajor,axis=1)

df['Hminor_mean'] = np.nanmean(index_Hminor,axis=1)
df['Hminor_std'] = np.nanstd(index_Hminor,axis=1)

columns=['geometry_2','geometry_3','geometry_4']
df = df.drop(columns=columns)
gdf = df.to_crs(epsg=3857)  # Reproject to a meter-based CRS
df['area'] = gdf.geometry.area

list_continent=pd.read_excel(r'D:\01.Papers\2023_Trans_NEO_TCsETCs/ListCountries.xlsx')
df['CONTINENT']=df['GID_0'].copy()
df['SUBREGION']=df['GID_0'].copy()

for i in range(len(list_continent)):
      df.loc[df['GID_0'] == list_continent.loc[i, 'GID_0'], 'CONTINENT']  = list_continent.loc[i, 'Continent']
      df.loc[df['GID_0'] == list_continent.loc[i, 'GID_0'], 'SUBREGION'] = list_continent.loc[i, 'Subregion']
      #df.loc[	df['A'] == a[nclass] , 'class'] = class0[nclass]



df.to_file(pathOut+'\\climatic_regions_ENSEMBLE_monte_carlo_v1.shp')
TC_regions=classification_list[classification_list['class'].isin(np.unique(df['region']))]
TC_regions.to_excel(pathOut+'\\TC_regions_list_ENSEMBLE_monte_carlo_v1.xlsx', index=False)
classification_list.to_excel(pathOut+'TC_regions.xlsx', sheet_name='List_climatic_regions', index=False)
