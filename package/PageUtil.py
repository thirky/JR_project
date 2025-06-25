import os
import re
import shutil
from playwright.sync_api import sync_playwright
import time

#子操作
def AddData(page,site_id,device_name,data_name):
    time.sleep(1)
    #清空上一次勾选状态
    page.get_by_role("textbox", name="输入设备名称按Enter键搜索").fill("")          
    page.get_by_role("textbox", name="输入设备名称按Enter键搜索").press("Enter") 
    time.sleep(1)
    #选框输入设备名并且刷新列表
    page.get_by_role("textbox", name="输入设备名称按Enter键搜索").fill(device_name)
    page.get_by_role("textbox", name="输入设备名称按Enter键搜索").press("Enter")
    #等待设备出现并展开
    page.get_by_role("treeitem", name=site_id).get_by_role("group").nth(1).wait_for()
    page.get_by_role("treeitem", name=site_id).get_by_role("group").nth(1).click()  
    #等待数据项出现并勾选       
    page.get_by_role("treeitem", name=data_name).locator("span").nth(2).wait_for()
    page.get_by_role("treeitem", name=data_name).locator("span").nth(2).click() 
    page.get_by_role("button", name="确定").click()
    
#登录    
def Login(page,account,password):
    page.get_by_role("textbox", name="租户").fill("jinrong")
    page.get_by_role("textbox", name="用户名").fill(account)
    page.get_by_role("textbox", name="密码").fill(password)
    page.get_by_role("button", name="登 录").click()

#添加数据报表
def ArrangeLoadCurrent(page,site_id,site_name,group_name,data_name):
    page.get_by_text("数据报表").click()
    page.get_by_role("link", name="历史曲线").click()
    page.get_by_title("新建分组").click()
    page.get_by_role("textbox", name="请选择机构").click()
    page.get_by_role("listitem").filter(has_text=re.compile(r"^佛山立胜$")).click()    
    page.locator("div").filter(has_text=re.compile(r"^报表分组名称$")).get_by_role("textbox").fill(group_name)
    page.get_by_role("button", name="保存").click()   
    for i in range(len(site_id)):
        if i>0 and site_name[i]==site_name[i-1]:
            continue 
        page.get_by_text(group_name).click()
        page.get_by_title("新建曲线").click()
        page.get_by_role("button", name="添加数据项").click()
        AddData(page,site_id[i],"电源1计量",data_name)
        if i<len(site_id)-1 and site_name[i]==site_name[i+1]:
            page.get_by_role("button", name="添加数据项").click()
            time.sleep(1)
            AddData(page,site_id[i+1],"电源2计量",data_name)
        page.get_by_role("textbox", name="请选择项目").click()
        page.get_by_role("listitem").filter(has_text="立胜能源").click()
        page.locator("div").filter(has_text=re.compile(r"^报表名称$")).get_by_role("textbox").fill(site_name[i])
        page.get_by_role("button", name="保存").click()

#添加数据报表
def ArrangeEP(page,site_id,site_name,group_name,data_name):
    page.get_by_text("数据报表").click()
    page.get_by_role("link", name="历史曲线").click()
    page.get_by_title("新建分组").click()
    page.get_by_role("textbox", name="请选择机构").click()
    page.get_by_role("listitem").filter(has_text=re.compile(r"^佛山立胜$")).click()    
    page.locator("div").filter(has_text=re.compile(r"^报表分组名称$")).get_by_role("textbox").fill(group_name)
    page.get_by_role("button", name="保存").click()   
    for i in range(len(site_id)):
        if i>0 and site_name[i]==site_name[i-1]:
            continue 
        page.get_by_text(group_name).click()
        page.get_by_title("新建曲线").click()
        page.get_by_role("button", name="添加数据项").click()
        AddData(page,site_id[i],"电源1计量",data_name)
        page.get_by_role("row", name="COM1 电源1").get_by_placeholder("请选择算法").click()
        page.get_by_role("list").get_by_text("相减").click()
        if i<len(site_id)-1 and site_name[i]==site_name[i+1]:
            page.get_by_role("button", name="添加数据项").click()
            time.sleep(1)
            AddData(page,site_id[i],"电源2计量",data_name)
            page.get_by_role("row", name="COM1 电源2").get_by_placeholder("请选择算法").click()
            page.get_by_role("list").get_by_text("相减").click()
        page.get_by_role("textbox", name="请选择项目").click()
        page.get_by_role("listitem").filter(has_text="立胜能源").click()
        page.locator("div").filter(has_text=re.compile(r"^报表名称$")).get_by_role("textbox").fill(site_name[i])
        page.get_by_role("button", name="保存").click()

#添加数据报表
def ArrangeZDY(page,site_id,site_name,group_name,data_name):
    page.get_by_text("数据报表").click()
    page.get_by_role("link", name="自定义报表").click()
    page.get_by_title("新建分组").click()
    page.get_by_role("textbox", name="请选择机构").click()
    page.get_by_role("listitem").filter(has_text=re.compile(r"^佛山立胜$")).click()    
    page.locator("div").filter(has_text=re.compile(r"^报表分组名称$")).get_by_role("textbox").fill(group_name)
    page.get_by_role("button", name="保存").click()   
    for i in range(len(site_id)):
        if i>0 and site_name[i]==site_name[i-1]:
            continue 
        page.get_by_text(group_name).click()
        page.get_by_title("新建曲线").click()
        page.get_by_role("button", name="添加数据项").click()
        AddData(page,site_id[i],"电源1计量",data_name)
        page.get_by_role("row", name="COM1 电源1").get_by_placeholder("请选择算法").click()
        page.get_by_role("list").get_by_text("相减").click()
        if i<len(site_id)-1 and site_name[i]==site_name[i+1]:
            page.get_by_role("button", name="添加数据项").click()
            time.sleep(1)
            AddData(page,site_id[i],"电源2计量",data_name)
            page.get_by_role("row", name="COM1 电源2").get_by_placeholder("请选择算法").click()
            page.get_by_role("list").get_by_text("相减").click()
        page.get_by_role("textbox", name="请选择项目").click()
        page.get_by_role("listitem").filter(has_text="立胜能源").click()
        page.locator("div").filter(has_text=re.compile(r"^报表名称$")).get_by_role("textbox").fill(site_name[i])
        page.get_by_role("button", name="保存").click()

#添加网关账户  
def AddGateway(page,site_id,site_name):
    page.get_by_text("工程管理").click()
    page.get_by_role("link", name="网关账户").click()
    for i in range(len(site_id)):
        page.get_by_role("button", name="新增").click()
        page.get_by_role("textbox", name="请输入网关id").fill(site_id[i])
        page.get_by_role("textbox", name="请输入sn").fill(site_name[i])
        page.get_by_role("textbox", name="请输入用户名").fill("admin")
        page.get_by_role("textbox", name="请输入密码").fill("admin123")
        page.get_by_role("button", name="确定").click()

#下载配置文件
def DownloadFiles(page,site_id,city,area=None):
    page.get_by_text("设备管理").click()
    page.get_by_role("link", name="数据源").click()
    if area != None:
        page.locator("section").get_by_text(city).wait_for()
        page.get_by_role("treeitem", name=city).locator("span").first.click()
        page.get_by_role("group").get_by_text(area).click()
    for i in range(len(site_id)):
        temp="【"+site_id[i]
        page.get_by_text(temp).click()
        if page.locator(".el-notification").is_visible():
            page.locator(".el-notification .el-notification__closeBtn").click()
        with page.expect_download() as download_info:
            page.get_by_role("button", name="导出").click()
        download = download_info.value
        # 获取下载文件的临时路径
        temp_path = download.path()
        # 获取下载文件的原始文件名
        original_filename = download.suggested_filename
        # 目标目录（可以自定义）
        target_directory = r"D:\LenovoSoftstore\配置文件"
        # 拼接目标路径
        if area == None:
            target_path = os.path.join(target_directory, city, original_filename)
        else:
            target_path = os.path.join(target_directory, city, area, original_filename)
        # 将文件移动到目标目录
        shutil.move(temp_path, target_path)
        print(f"文件已保存到: {target_path}")

#上传配置文件
def UploadFiles(page,site_id,city,area=None):
    page.get_by_text("设备管理").click()
    page.get_by_role("link", name="数据源").click()
    if area != None:
        page.locator("section").get_by_text(city).wait_for()
        page.get_by_role("treeitem", name=city).locator("span").first.click()
        page.get_by_role("group").get_by_text(area).click()
    for i in range(len(site_id)):
        temp="【"+site_id[i]
        file_name=site_id[i]+".xls"
        target_directory = r"D:\LenovoSoftstore\配置文件"
        if area == None:
            target_path = os.path.join(target_directory, city, file_name)
        else:
            target_path = os.path.join(target_directory, city, area, file_name)
        page.get_by_text(temp).click()
        #双弹窗，等“导入成功”弹窗消失
        time.sleep(5)
        if page.locator(".el-notification").is_visible():
            page.locator(".el-notification .el-notification__closeBtn").click()
        page.get_by_role("button", name="导入").click()
        with page.expect_file_chooser() as upload_info:
            page.get_by_role("button", name="选择文件").click()
        file_chooser = upload_info.value
        file_chooser.set_files(target_path)
        page.get_by_role("button", name="确定").click()
        time.sleep(5)#等待上传成功

#添加电费报表
def ProfitAllocation(page,site_id,site_name,site_region):
    page.get_by_text("电能费用").click()
    page.get_by_role("link", name="电费报表").click()
    page.get_by_role("treeitem", name="深圳市(铁塔)").locator("span").first.click()
    for i in range(len(site_id)):
        page.get_by_text(site_region[i]).click(button="right")
        page.get_by_text("添加下级").click()
        page.get_by_role("textbox", name="请选择机构").click()
        page.get_by_text("广东津荣-深圳供电局-深圳铁塔", exact=True).click()
        page.locator("div").filter(has_text=re.compile(r"^报表分组名称$")).get_by_role("textbox").fill(site_name[i])
        page.get_by_role("button", name="保存").click()
        #找到站点
        page.get_by_role("treeitem", name="深圳市(铁塔)").locator("span").first.click()
        page.get_by_role("treeitem", name=site_region[i]).locator("span").first.click()
        page.get_by_text(site_name[i]).click()
        #建立总进线报表
        page.get_by_title("新建报表").click()
        page.get_by_role("dialog", name="报表基本信息").get_by_role("textbox").fill("总进线")
        page.get_by_role("button", name="保存").click()
        page.get_by_text("总进线").click(button="right")
        page.get_by_role("listitem").filter(has_text="编辑").click()
        page.get_by_role("button", name="添加数据项").click()
        AddData(page,site_id[i],"总进线计量","有功总电能")
        page.get_by_role("textbox", name="请选择电价配置").click()
        page.get_by_role("listitem").get_by_text("深圳市").click()
        page.get_by_role("button", name="保存").click()
        #建立电源进线报表
        page.get_by_title("新建报表").click()
        page.get_by_role("dialog", name="报表基本信息").get_by_role("textbox").fill("电源进线")
        page.get_by_role("button", name="保存").click()
        page.get_by_text("电源进线").click(button="right")
        page.get_by_role("listitem").filter(has_text="编辑").click()
        page.get_by_role("button", name="添加数据项").click()
        AddData(page,site_id[i],"电源计量","有功总电能")
        page.get_by_role("textbox", name="请选择电价配置").click()
        page.get_by_role("listitem").get_by_text("深圳市").click()
        page.get_by_role("button", name="保存").click()
        #建立空调进线报表
        page.get_by_title("新建报表").click()
        page.get_by_role("dialog", name="报表基本信息").get_by_role("textbox").fill("空调进线")
        page.get_by_role("button", name="保存").click()
        page.get_by_text("空调进线").click(button="right")
        page.get_by_role("listitem").filter(has_text="编辑").click()
        page.get_by_role("button", name="添加数据项").click()
        AddData(page,site_id[i],"空调1计量","有功总电能")
        page.get_by_role("textbox", name="请选择电价配置").click()
        page.get_by_role("listitem").get_by_text("深圳市").click()
        page.get_by_role("button", name="保存").click()

#添加报表电池数量
def yex(page,site_name,bat_num):
    page.get_by_text("电能费用").click()
    page.get_by_role("link", name="电费报表").click()
    page.get_by_role("treeitem", name="佛山市(移动)").locator("span").first.click()
    page.get_by_role("treeitem", name="禅城区").locator("span").first.click()
    for i in range(len(site_name)):
        if site_name[i]==site_name[i+1]:
            #找到站点
            page.get_by_text(site_name[i]).wait_for()
            page.get_by_text(site_name[i]).click()
            #建立总进线报表
            time.sleep(0.2)
            page.get_by_role("treeitem", name="总进线").locator("span").first.click(button="right")
            page.get_by_role("listitem").filter(has_text="编辑").click()
            page.get_by_role("spinbutton", name="请输入PACK数").fill(str(bat_num[i]+bat_num[i+1]))
            page.get_by_role("button", name="保存").click()
            continue
        if i>0 and site_name[i]==site_name[i-1]:
            continue
        #找到站点
        page.get_by_text(site_name[i]).wait_for()
        page.get_by_text(site_name[i]).click()
        #建立总进线报表
        time.sleep(0.2)
        page.get_by_role("treeitem", name="总进线").locator("span").first.click(button="right")
        page.get_by_role("listitem").filter(has_text="编辑").click()
        page.get_by_role("spinbutton", name="请输入PACK数").fill(str(bat_num[i]))
        page.get_by_role("button", name="保存").click()

#平台站点添加(系统设置——站点管理——新增站点)
def AddSite(page,site_name,site_addr,site_lon,site_lat,city,area):
    page.get_by_text("系统设置").click()
    page.get_by_role("link", name="站点管理").click()
    for i in range(len(site_name)):
        if site_name[i] == site_name[i + 1] and i < len(site_name) - 2:
            continue
        page.get_by_role("button", name="新增站点").click()
        page.locator("form div").filter(has_text="站点名称").get_by_role("textbox").first.fill(site_name[i])
        page.get_by_role("dialog", name="站点信息").get_by_placeholder("请选择").first.click()
        page.get_by_role("listitem").filter(has_text="广东省").click()
        page.get_by_role("dialog", name="站点信息").get_by_placeholder("请选择").nth(1).click()
        page.get_by_role("listitem").filter(has_text=city).click()
        page.get_by_role("dialog", name="站点信息").get_by_placeholder("请选择").nth(2).click()
        page.get_by_role("listitem").filter(has_text=area[i]).click()
        page.get_by_role("dialog", name="站点信息").get_by_placeholder("请选择").nth(3).click()
        page.get_by_role("listitem").filter(has_text="广东津荣-深圳供电局-深圳铁塔").click()
        page.locator("div").filter(has_text=re.compile(r"^详细地址经度纬度$")).get_by_role("textbox").first.fill(site_addr)
        page.locator("div").filter(has_text=re.compile(r"^详细地址经度纬度$")).get_by_role("textbox").nth(1).fill(site_lon)
        page.locator("div").filter(has_text=re.compile(r"^详细地址经度纬度$")).get_by_role("textbox").nth(2).fill(site_lat)
        page.get_by_role("button", name="选择").click()
        page.get_by_role("row", name="站点大屏 选择").get_by_role("button").click()
        page.get_by_role("dialog", name="站点信息").get_by_placeholder("请选择").nth(4).click()
        page.get_by_role("listitem").filter(has_text="admin").click()
        page.get_by_role("button", name="保存").click()