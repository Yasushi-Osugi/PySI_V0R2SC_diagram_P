# make_Common_Plan_Unit2diagram()

import pandas as pd
import csv

# ******************************
# making the list of "node_name" from 'SCMTREE_profile010.csv'
# ******************************
from PySILib.PySI_search_LEAF_in_SCMTREE import *

# ******************************
# passing "node_name" list
# ******************************
postorder_node = node_name


# ******************************
# adding "root" node in the list
# ******************************
postorder_node.append('root')


# 
# Dpt_entityとArv_entityをkeyとしてcountする。
#
#seq_no	control_flag	priority_no	modal	LT	Dpt_entity	Dpt_week#	Dpt_step	Arv_entity	Arv_week	Arv_step
#ZRHLEAF202312014	F	1202312014	B	2	ZRH	49	#0	ZRHLEAF	51	0
#ZRHLEAF202312019	F	1202312019	B	2	ZRH	49	#1	ZRHLEAF	51	1
#ZRHLEAF202312021	F	1202312021	B	2	ZRH	49	#2	ZRHLEAF	51	2
#ZRHLEAF202312022	F	1202312022	B	2	ZRH	49	#3	ZRHLEAF	51	3
#ZRHLEAF202312025	F	1202312025	B	2	ZRH	50	#0	ZRHLEAF	52	0
#ZRH202301002	F	1202301002	B	9	JPN	-8	0	#ZRH	1	0
#ZRH202301003	F	1202301003	B	9	JPN	-8	1	#ZRH	1	1
#ZRH202301004	F	1202301004	B	9	JPN	-8	2	#ZRH	1	2
#ZRH202301005	F	1202301005	B	9	JPN	-8	3	#ZRH	1	3
#

print('Dpt_entityとArv_entityをkeyとして、Common_Plan_Unitをcountする。')


def make_common_plan_unit2sankey_data( file_name ):

    # **********************************
    # start of reading 'common_plan_unit.csv'
    # **********************************
    
    df = pd.read_csv( file_name )
    #df = pd.read_csv('common_plan_unit.csv')
    #df = pd.read_csv('common_plan_unit.csv',encoding='shift-jis',sep=',')

    df4sankey = df.groupby(['Dpt_entity', 'Arv_entity']).count()
    
    df4sankey_list = df4sankey.reset_index().values.tolist()

    return df4sankey, df4sankey_list


# **************************************:
# run making diagram data  "node_from"  "node_to"  "value"
# **************************************:

file_name = 'common_plan_unit.csv'

df4sankey, df4sankey_list = make_common_plan_unit2sankey_data( file_name )

print('df4sankey',df4sankey)
print('df4sankey_list',df4sankey_list)

sankey_path_list = []

for from_to_value in df4sankey_list :

    sankey_ftv = from_to_value[:3]

    sankey_path_list.append(sankey_ftv)

print('sankey_list',sankey_path_list)


# ****************************************************
# making supply chain nodes profile 2 postpoder_node_list
# ****************************************************

#postorder_node = ['YTOLEAF', 'YTO', 'NYC_N', 'NYC_D', 'NYC_I', 'NYC', 'LAX_N', 'LAX_D', 'LAX_I', 'SFOLEAF', 'LAX', 'MEXLEAF', 'MEX', 'SAOLEAF', 'SAO', 'BUELEAF', 'BUE', 'KULLEAF', 'KUL', 'BKKLEAF', 'BKK', 'SINLEAF', 'SIN', 'SGNLEAF', 'SGN', 'ISTLEAF', 'IST', 'JKTLEAF', 'JKT', 'SELLEAF', 'SEL', 'SYDLEAF', 'SYD', 'DELLEAF', 'DEL', 'RUHLEAF', 'RUH', 'SWELEAF', 'NORLEAF', 'DENLEAF', 'HELLEAF', 'GOT', 'LONLEAF', 'LON', 'PARLEAF', 'PAR', 'HAM_N', 'HAM_D', 'HAM_I', 'MUC_N', 'MUC_D', 'MUC_I', 'MUC', 'FRALEAF', 'HAM', 'MXPLEAF', 'MXP', 'JNBLEAF', 'JNB', 'SHA_N', 'SHA_D', 'SHA_I', 'BJS_N', 'BJS_D', 'BJS_I', 'SHA', 'CAN_N', 'CAN_D', 'CAN_I', 'CAN', 'LEDLEAF', 'LED', 'BRULEAF', 'BRU', 'TYOLEAF', 'TYO', 'OSALEAF', 'OSA', 'AMSLEAF', 'AMS', 'AKLLEAF', 'AKL', 'WAWLEAF', 'WAW', 'LISLEAF', 'LIS', 'MADLEAF', 'MAD', 'ZRHLEAF', 'ZRH', 'JPN','root']


# ****************************************************
#                "source": path_from ,
#                "target": path_to   ,
#
#                "value": path_value ,
#
#                "color": path_color ,
#
#                "label": path_label 
# ****************************************************

path_from     = []
path_to       = []
path_value    = []
path_color    = []
path_label    = []



for  i, f_t_v in enumerate(sankey_path_list):

    node_from  = f_t_v[0]
    node_to    = f_t_v[1]
    node_value = f_t_v[2]


    pos_from = postorder_node.index(node_from)
    path_from.append( pos_from )

    pos_to   = postorder_node.index(node_to)
    path_to.append( pos_to )

    path_value.append(node_value)

    path_color.append("rgba(0,0,96,0.2)")

    path_label.append("dummy for PSI analizing")


