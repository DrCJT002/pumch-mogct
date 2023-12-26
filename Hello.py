# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st

def calculate_endometrial_cancer_stage(myometrial_invasion, cervical_stroma, extrauterine_diffusion,
                                               LVSI, aggressive_histological_type, lymph_nodes_involved, lymph_nodes, 
                                               distant_metastasis, molecular_subtype):
    if "腹股沟淋巴结" in lymph_nodes_involved:
            return "Stage IVC"    
    elif distant_metastasis != []:
        if "其他远处转移" in distant_metastasis:
            return "Stage IVC"
        elif "腹股沟淋巴结" in lymph_nodes_involved:
            return "Stage IVC"        
        elif "肺" in distant_metastasis:
            return "Stage IVC"
        elif "肝" in distant_metastasis:
            return "Stage IVC"
        elif "骨" in distant_metastasis:
            return "Stage IVC" 
        elif "腹腔腹膜" in distant_metastasis:
            return "Stage IVB" 
        elif "腹腔内癌" in distant_metastasis:
            return "Stage IVB" 
        else :
            return "Stage IVA"
    elif (extrauterine_diffusion != []) or (lymph_nodes_involved != []) :
        if "腹主动脉旁淋巴结" in lymph_nodes_involved:
            if "宏转移" in lymph_nodes:
                return "Stage IIIC2ii"
            elif lymph_nodes == []:
                return "Stage IIIC2"
            else:
                return "Stage IIIC2i"
        elif "盆腔淋巴结" in lymph_nodes_involved:
            if "宏转移" in lymph_nodes:
                return "Stage IIIC1ii"
            elif lymph_nodes == []:
                return "Stage IIIC1"
            else:
                return "Stage IIIC1i"
        elif "盆腔腹膜" in extrauterine_diffusion:
            return "Stage IIIB2"
        elif "宫旁" in extrauterine_diffusion:
            return "Stage IIIB1"    
        elif "阴道" in extrauterine_diffusion:
            return "Stage IIIB1"
        elif "子宫浆膜层" in extrauterine_diffusion:
            return "Stage IIIA2"
        else: 
            if "低级别子宫内膜样" in aggressive_histological_type:
                return "Stage IA3"    
            else:
                return "Stage IIIA1"    
    elif (cervical_stroma == "是") or (LVSI == "大量"):
        if "p53abn" in molecular_subtype:
            return "Stage IICm-p53abn"
        elif "POLEmut" in molecular_subtype:     
            return "Stage IAm-POLEmut"
        elif LVSI == "大量":
            return "Stage IIB"
        else:
            return "Stage IIA"
    else:
        if "p53abn" in molecular_subtype:
            return "Stage IICm-p53abn"
        elif "POLEmut" in molecular_subtype:     
            return "Stage IAm-POLEmut"
        elif (aggressive_histological_type in ['高级别子宫内膜样','浆液性','透明细胞','癌肉瘤','未分化','混合性','其他少见类型癌']) and ("局限于内膜" not in myometrial_invasion):
            return "Stage IIC"
        elif (aggressive_histological_type in ['高级别子宫内膜样','浆液性','透明细胞','癌肉瘤','未分化','混合性','其他少见类型癌']) and ("局限于内膜" in myometrial_invasion):
            return "Stage IC"
        elif "肌层浸润大于等于1/2" in myometrial_invasion:     
            return "Stage IB"
        elif "局限于内膜" in myometrial_invasion:     
            return "Stage IA1"
        else:
            return "Stage IA2"

# Streamlit 应用程序代码
st.title('FIGO 2023 子宫内膜癌分期')

# 创建用户输入框和下拉菜单等组件
myometrial_invasion = st.radio("肌层浸润: ",['局限于内膜','肌层浸润小于1/2','肌层浸润大于等于1/2'])

cervical_stroma = st.radio("宫颈间质浸润: ", ["否","是"])

LVSI = st.radio("LVSI: ", ["无或局灶性","大量"])

aggressive_histological_type = st.radio("组织病理: ", ['低级别子宫内膜样','中级别子宫内膜样','高级别子宫内膜样','浆液性','透明细胞','癌肉瘤','未分化','混合性','其他少见类型癌'])

extrauterine_diffusion = st.multiselect("局部扩散: ",['子宫浆膜层','附件','阴道','宫旁','盆腔腹膜'])

lymph_nodes_involved = st.multiselect("淋巴结转移:",['盆腔淋巴结', '腹主动脉旁淋巴结', '腹股沟淋巴结'])

lymph_nodes = st.multiselect("淋巴结状况:",['微转移', '宏转移'])
    
distant_metastasis = st.multiselect("肿瘤播散:",['肝','肺','骨','其他远处转移','腹腔腹膜','腹腔内癌','膀胱','肠粘膜'])
    
molecular_subtype = st.radio("分子分型: ", ["未分型", "p53abn", "dMMR", "NSMP", "POLEmut"])

# 其他组件的创建方式类似...

# 当用户点击按钮时，调用算法函数并显示结果
if st.button('计算分期'):
    stage = calculate_endometrial_cancer_stage(myometrial_invasion, cervical_stroma, extrauterine_diffusion,
                                               LVSI, aggressive_histological_type, lymph_nodes_involved, lymph_nodes, 
                                               distant_metastasis, molecular_subtype)
    st.write(f"分期为: {stage}")
