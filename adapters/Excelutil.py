#
 # @Date: 2025-02-27 12:16:30
 # @Author: thirky
 # @Description: EXCEL工具类
 #

import openpyxl
import os


#获取站点表的消息，(用于系统设置-站点管理-新增站点)
def getSiteForm(path,sheetName):
    workbook = openpyxl.load_workbook(path)
    sheet = workbook[sheetName]
    site_name = []
    site_addr=[]
    site_lon=[]
    site_lat=[]
    for row in range(1,sheet.max_row+1):
        cell_value=sheet[f'A{row}'].value
        if cell_value:
            str(cell_value).strip()
    for row in range(2, sheet.max_row + 1):
        site_name.append(sheet[f'A{row}'].value)
        site_addr.append(sheet[f'B{row}'].value)
        site_lon.append(sheet[f'C{row}'].value)
        site_lat.append(sheet[f'D{row}'].value)
    return site_name,site_addr,site_lon,site_lat

#获取excel表格里的站点id和名字
def getSiteIdandRegion(path,sheetName):
    workbook = openpyxl.load_workbook(path)
    sheet = workbook[sheetName]
    site_id = []
    site_name=[]
    site_region=[]
    for row in range(1,sheet.max_row+1):
        cell_value=sheet[f'A{row}'].value
        if cell_value:
            str(cell_value).strip()
    for row in range(2, sheet.max_row + 1):
        site_id.append(sheet[f'A{row}'].value)
        site_name.append(sheet[f'B{row}'].value)
        site_region.append(sheet[f'C{row}'].value)
    return site_id,site_name,site_region

#实时监控站点信息表数据
def getPoint(path,sheetName):
    workbook = openpyxl.load_workbook(path)
    sheet = workbook[sheetName]
    site_region=[]
    site_name=[]
    site_addr=[]
    gw_aid=[]
    all_id=[]
    power_id=[]
    powerA_mfg=[]
    powerA_model=[]
    air1_name=[]
    air2_name=[]
    acn_AH=[]
    aby_AH=[]
    old=[]
    for cell in sheet[1]:
        if cell.value:
            old.append(cell.value.strip())
    for row in range(2, sheet.max_row + 1):
        site_region.append(sheet[f'A{row}'].value)
        site_name.append(sheet[f'B{row}'].value)
        site_addr.append(sheet[f'C{row}'].value)
        all_id.append(sheet[f'D{row}'].value)
        power_id.append(sheet[f'E{row}'].value)
        air1_name.append(sheet[f'F{row}'].value)
        air2_name.append(sheet[f'G{row}'].value)
        gw_aid.append(sheet[f'H{row}'].value)
        powerA_mfg.append(sheet[f'I{row}'].value)
        powerA_model.append(sheet[f'J{row}'].value)
        acn_AH.append(sheet[f'K{row}'].value)
        aby_AH.append(sheet[f'L{row}'].value)
    return old,site_region,site_name,site_addr,all_id,power_id,air1_name,air2_name,gw_aid,powerA_mfg,powerA_model,acn_AH,aby_AH
