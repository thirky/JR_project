#
 # @Date: 2025-04-15 12:05:30
 # @Author: thirky
 # @Description: 
 #
import sys
sys.path.append(r'.\adapters')
from ExcelUtil import ExcelUtil
import os

site_data= ExcelUtil.get_PlatformPage_form('Sheet1')
site_region=site_data['site_region']
site_name=site_data['site_name']
site_addr=site_data['site_addr']
all_id=site_data['all_id']
power_id=site_data['power_id']
air1_name=site_data['air1_name']
air2_name=site_data['air2_name']
gw_aid=site_data['gw_aid']
powerA_mfg=site_data['powerA_mfg']
powerA_model=site_data['powerA_model']
acn_AH=site_data['acn_AH']
aby_AH=site_data['aby_AH']
old=site_data['old']
base_dir=r"C:\Users\26485\Desktop\站点大屏模板.txt"

for i in range(len(site_name)):
        # 读取原始txt文件内容
    with open(base_dir, 'r', encoding='utf-8') as f:
        content = f.read()
    # 新内容列表
    new_values = [
        site_region[i],site_name[i],site_addr[i],all_id[i],power_id[i],air1_name[i],air2_name[i],
        gw_aid[i],powerA_mfg[i],powerA_model[i],acn_AH[i],aby_AH[i]
    ]
    # 批量替换
    for j in range(len(old)):
        if new_values[j] == None and (old[j] == "基站空调1" or old[j] == "基站空调2"):
            str1=old[j]+"隐藏"
            content = content.replace(str1, "1==1")
            continue
        if new_values[j] == None and (old[j] == "A网关备用电池AH数"):
            content = content.replace(str(old[j]), "666444")
            content = content.replace("A网关备用电池隐藏", "1==1")
            continue
        content = content.replace(str(old[j]), str(new_values[j]))

    # 处理文件名中的非法字符
    safe_name = "".join(c for c in site_name[i] if c not in r'\/:*?"<>|')
    # 输出文件到指定文件夹
    output_path = f"C:/Users/26485/Desktop/实时监控页面表/{safe_name}.txt"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)