import sys
sys.path.append(r'.\adapters')
from PlaywrightActions import PlaywrightActions
import os
import re
import shutil
import time


class PlatformAutomator:
    """平台自动化脚本：津荣云平台上的脚本功能操作"""
    def __init__(self, headless=False):
        self.actions = PlaywrightActions(headless=headless)
        self.page = self.actions.goto_jrie()  # 自动打开浏览器并导航
    
    def __enter__(self):
        """支持with语法"""
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        """退出时自动关闭资源"""
        self.actions.close()

    #登录
    def login(self, account, password,):
        self.page.get_by_role("textbox", name="租户").fill("jinrong")
        self.page.get_by_role("textbox", name="用户名").fill(account)
        self.page.get_by_role("textbox", name="密码").fill(password)
        self.page.get_by_role("button", name="登 录").click()
    
    #添加数据报表(当前负载曲线)
    def ArrangeLoadCurrent(self,site_id,site_name,group_name,data_name):
        self.page.get_by_text("数据报表").click()
        self.page.get_by_role("link", name="历史曲线").click()
        self.page.get_by_title("新建分组").click()
        self.page.get_by_role("textbox", name="请选择机构").click()
        self.page.get_by_role("listitem").filter(has_text=re.compile(r"^佛山立胜$")).click()    
        self.page.locator("div").filter(has_text=re.compile(r"^报表分组名称$")).get_by_role("textbox").fill(group_name)
        self.page.get_by_role("button", name="保存").click()   
        for i in range(len(site_id)):
            if i>0 and site_name[i]==site_name[i-1]:
                continue 
            self.page.get_by_text(group_name).click()
            self.page.get_by_title("新建曲线").click()
            self.page.get_by_role("button", name="添加数据项").click()
            self.actions.add_data(self.page,site_id[i],"电源1计量",data_name)
            if i<len(site_id)-1 and site_name[i]==site_name[i+1]:
                self.page.get_by_role("button", name="添加数据项").click()
                time.sleep(1)
                self.actions.add_data(self.page,site_id[i+1],"电源2计量",data_name)
            self.page.get_by_role("textbox", name="请选择项目").click()
            self.page.get_by_role("listitem").filter(has_text="立胜能源").click()
            self.page.locator("div").filter(has_text=re.compile(r"^报表名称$")).get_by_role("textbox").fill(site_name[i])
            self.page.get_by_role("button", name="保存").click()

    #添加数据报表(电源用电量曲线)
    def ArrangeEP(self,site_id,site_name,group_name,data_name):
        self.page.get_by_text("数据报表").click()
        self.page.get_by_role("link", name="历史曲线").click()
        self.page.get_by_title("新建分组").click()
        self.page.get_by_role("textbox", name="请选择机构").click()
        self.page.get_by_role("listitem").filter(has_text=re.compile(r"^佛山立胜$")).click()    
        self.page.locator("div").filter(has_text=re.compile(r"^报表分组名称$")).get_by_role("textbox").fill(group_name)
        self.page.get_by_role("button", name="保存").click()   
        for i in range(len(site_id)):
            if i>0 and site_name[i]==site_name[i-1]:
                continue 
            self.page.get_by_text(group_name).click()
            self.page.get_by_title("新建曲线").click()
            self.page.get_by_role("button", name="添加数据项").click()
            self.actions.add_data(self.page,site_id[i],"电源1计量",data_name)
            self.page.get_by_role("row", name="COM1 电源1").get_by_placeholder("请选择算法").click()
            self.page.get_by_role("list").get_by_text("相减").click()
            if i<len(site_id)-1 and site_name[i]==site_name[i+1]:
                self.page.get_by_role("button", name="添加数据项").click()
                time.sleep(1)
                self.actions.add_data(self.page,site_id[i],"电源2计量",data_name)
                self.page.get_by_role("row", name="COM1 电源2").get_by_placeholder("请选择算法").click()
                self.page.get_by_role("list").get_by_text("相减").click()
            self.page.get_by_role("textbox", name="请选择项目").click()
            self.page.get_by_role("listitem").filter(has_text="立胜能源").click()
            self.page.locator("div").filter(has_text=re.compile(r"^报表名称$")).get_by_role("textbox").fill(site_name[i])
            self.page.get_by_role("button", name="保存").click()

    #添加数据报表
    def ArrangeZDY(self,site_id,site_name,group_name,data_name):
        self.page.get_by_text("数据报表").click()
        self.page.get_by_role("link", name="自定义报表").click()
        self.page.get_by_title("新建分组").click()
        self.page.get_by_role("textbox", name="请选择机构").click()
        self.page.get_by_role("listitem").filter(has_text=re.compile(r"^佛山立胜$")).click()    
        self.page.locator("div").filter(has_text=re.compile(r"^报表分组名称$")).get_by_role("textbox").fill(group_name)
        self.page.get_by_role("button", name="保存").click()   
        for i in range(len(site_id)):
            if i>0 and site_name[i]==site_name[i-1]:
                continue 
            self.page.get_by_text(group_name).click()
            self.page.get_by_title("新建曲线").click()
            self.page.get_by_role("button", name="添加数据项").click()
            self.actions.add_data(self.page,site_id[i],"电源1计量",data_name)
            self.page.get_by_role("row", name="COM1 电源1").get_by_placeholder("请选择算法").click()
            self.page.get_by_role("list").get_by_text("相减").click()
            if i<len(site_id)-1 and site_name[i]==site_name[i+1]:
                self.page.get_by_role("button", name="添加数据项").click()
                time.sleep(1)
                self.actions.add_data(self.page,site_id[i],"电源2计量",data_name)
                self.page.get_by_role("row", name="COM1 电源2").get_by_placeholder("请选择算法").click()
                self.page.get_by_role("list").get_by_text("相减").click()
            self.page.get_by_role("textbox", name="请选择项目").click()
            self.page.get_by_role("listitem").filter(has_text="立胜能源").click()
            self.page.locator("div").filter(has_text=re.compile(r"^报表名称$")).get_by_role("textbox").fill(site_name[i])
            self.page.get_by_role("button", name="保存").click()

    #添加网关账户  
    def AddGateway(self,site_id,site_name):
        self.page.get_by_text("工程管理").click()
        self.page.get_by_role("link", name="网关账户").click()
        for i in range(len(site_id)):
            self.page.get_by_role("button", name="新增").click()
            self.page.get_by_role("textbox", name="请输入网关id").fill(site_id[i])
            self.page.get_by_role("textbox", name="请输入sn").fill(site_name[i])
            self.page.get_by_role("textbox", name="请输入用户名").fill("admin")
            self.page.get_by_role("textbox", name="请输入密码").fill("admin123")
            self.page.get_by_role("button", name="确定").click()

    #下载配置文件
    def DownloadFiles(self,site_id,city,area=None):
        self.page.get_by_text("设备管理").click()
        self.page.get_by_role("link", name="数据源").click()
        if area != None:
            self.page.locator("section").get_by_text(city).wait_for()
            self.page.get_by_role("treeitem", name=city).locator("span").first.click()
            self.page.get_by_role("group").get_by_text(area).click()
        for i in range(len(site_id)):
            temp="【"+site_id[i]
            self.page.get_by_text(temp).click()
            if self.page.locator(".el-notification").is_visible():
                self.page.locator(".el-notification .el-notification__closeBtn").click()
            with self.page.expect_download() as download_info:
                self.page.get_by_role("button", name="导出").click()
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
    def UploadFiles(self,site_id,city,area=None):
        self.page.get_by_text("设备管理").click()
        self.page.get_by_role("link", name="数据源").click()
        if area != None:
            self.page.locator("section").get_by_text(city).wait_for()
            self.page.get_by_role("treeitem", name=city).locator("span").first.click()
            self.page.get_by_role("group").get_by_text(area).click()
        for i in range(len(site_id)):
            temp="【"+site_id[i]
            file_name=site_id[i]+".xls"
            target_directory = r"D:\LenovoSoftstore\配置文件"
            if area == None:
                target_path = os.path.join(target_directory, city, file_name)
            else:
                target_path = os.path.join(target_directory, city, area, file_name)
            self.page.get_by_text(temp).click()
            #双弹窗，等“导入成功”弹窗消失
            time.sleep(5)
            if self.page.locator(".el-notification").is_visible():
                self.page.locator(".el-notification .el-notification__closeBtn").click()
            self.page.get_by_role("button", name="导入").click()
            with self.page.expect_file_chooser() as upload_info:
                self.page.get_by_role("button", name="选择文件").click()
            file_chooser = upload_info.value
            file_chooser.set_files(target_path)
            self.page.get_by_role("button", name="确定").click()
            time.sleep(5)#等待上传成功

    #添加电费报表
    def ProfitAllocation(self,site_id,site_name,site_region):
        self.page.get_by_text("电能费用").click()
        self.page.get_by_role("link", name="电费报表").click()
        self.page.get_by_role("treeitem", name="深圳市(铁塔)").locator("span").first.click()
        for i in range(len(site_id)):
            self.page.get_by_text(site_region[i]).click(button="right")
            self.page.get_by_text("添加下级").click()
            self.page.get_by_role("textbox", name="请选择机构").click()
            self.page.get_by_text("广东津荣-深圳供电局-深圳铁塔", exact=True).click()
            self.page.locator("div").filter(has_text=re.compile(r"^报表分组名称$")).get_by_role("textbox").fill(site_name[i])
            self.page.get_by_role("button", name="保存").click()
            #找到站点
            self.page.get_by_role("treeitem", name="深圳市(铁塔)").locator("span").first.click()
            self.page.get_by_role("treeitem", name=site_region[i]).locator("span").first.click()
            self.page.get_by_text(site_name[i]).click()
            #建立总进线报表
            self.page.get_by_title("新建报表").click()
            self.page.get_by_role("dialog", name="报表基本信息").get_by_role("textbox").fill("总进线")
            self.page.get_by_role("button", name="保存").click()
            self.page.get_by_text("总进线").click(button="right")
            self.page.get_by_role("listitem").filter(has_text="编辑").click()
            self.page.get_by_role("button", name="添加数据项").click()
            self.actions.add_data(self.page,site_id[i],"总进线计量","有功总电能")
            self.page.get_by_role("textbox", name="请选择电价配置").click()
            self.page.get_by_role("listitem").get_by_text("深圳市").click()
            self.page.get_by_role("button", name="保存").click()
            #建立电源进线报表
            self.page.get_by_title("新建报表").click()
            self.page.get_by_role("dialog", name="报表基本信息").get_by_role("textbox").fill("电源进线")
            self.page.get_by_role("button", name="保存").click()
            self.page.get_by_text("电源进线").click(button="right")
            self.page.get_by_role("listitem").filter(has_text="编辑").click()
            self.page.get_by_role("button", name="添加数据项").click()
            self.actions.add_data(self.page,site_id[i],"电源计量","有功总电能")
            self.page.get_by_role("textbox", name="请选择电价配置").click()
            self.page.get_by_role("listitem").get_by_text("深圳市").click()
            self.page.get_by_role("button", name="保存").click()
            #建立空调进线报表
            self.page.get_by_title("新建报表").click()
            self.page.get_by_role("dialog", name="报表基本信息").get_by_role("textbox").fill("空调进线")
            self.page.get_by_role("button", name="保存").click()
            self.page.get_by_text("空调进线").click(button="right")
            self.page.get_by_role("listitem").filter(has_text="编辑").click()
            self.page.get_by_role("button", name="添加数据项").click()
            self.actions.add_data(self.page,site_id[i],"空调1计量","有功总电能")
            self.page.get_by_role("textbox", name="请选择电价配置").click()
            self.page.get_by_role("listitem").get_by_text("深圳市").click()
            self.page.get_by_role("button", name="保存").click()

    #添加报表电池数量
    def yex(self,site_name,bat_num):
        self.page.get_by_text("电能费用").click()
        self.page.get_by_role("link", name="电费报表").click()
        self.page.get_by_role("treeitem", name="佛山市(移动)").locator("span").first.click()
        self.page.get_by_role("treeitem", name="禅城区").locator("span").first.click()
        for i in range(len(site_name)):
            if site_name[i]==site_name[i+1]:
                #找到站点
                self.page.get_by_text(site_name[i]).wait_for()
                self.page.get_by_text(site_name[i]).click()
                #建立总进线报表
                time.sleep(0.2)
                self.page.get_by_role("treeitem", name="总进线").locator("span").first.click(button="right")
                self.page.get_by_role("listitem").filter(has_text="编辑").click()
                self.page.get_by_role("spinbutton", name="请输入PACK数").fill(str(bat_num[i]+bat_num[i+1]))
                self.page.get_by_role("button", name="保存").click()
                continue
            if i>0 and site_name[i]==site_name[i-1]:
                continue
            #找到站点
            self.page.get_by_text(site_name[i]).wait_for()
            self.page.get_by_text(site_name[i]).click()
            #建立总进线报表
            time.sleep(0.2)
            self.page.get_by_role("treeitem", name="总进线").locator("span").first.click(button="right")
            self.page.get_by_role("listitem").filter(has_text="编辑").click()
            self.page.get_by_role("spinbutton", name="请输入PACK数").fill(str(bat_num[i]))
            self.page.get_by_role("button", name="保存").click()

    #平台站点添加(系统设置——站点管理——新增站点)
    def AddSite(self,site_name,site_addr,site_lon,site_lat,city,area):
        self.page.get_by_text("系统设置").click()
        self.page.get_by_role("link", name="站点管理").click()
        for i in range(len(site_name)):
            if site_name[i] == site_name[i + 1] and i < len(site_name) - 2:
                continue
            self.page.get_by_role("button", name="新增站点").click()
            self.page.locator("form div").filter(has_text="站点名称").get_by_role("textbox").first.fill(site_name[i])
            self.page.get_by_role("dialog", name="站点信息").get_by_placeholder("请选择").first.click()
            self.page.get_by_role("listitem").filter(has_text="广东省").click()
            self.page.get_by_role("dialog", name="站点信息").get_by_placeholder("请选择").nth(1).click()
            self.page.get_by_role("listitem").filter(has_text=city).click()
            self.page.get_by_role("dialog", name="站点信息").get_by_placeholder("请选择").nth(2).click()
            self.page.get_by_role("listitem").filter(has_text=area[i]).click()
            self.page.get_by_role("dialog", name="站点信息").get_by_placeholder("请选择").nth(3).click()
            self.page.get_by_role("listitem").filter(has_text="广东津荣-深圳供电局-深圳铁塔").click()
            self.page.locator("div").filter(has_text=re.compile(r"^详细地址经度纬度$")).get_by_role("textbox").first.fill(site_addr)
            self.page.locator("div").filter(has_text=re.compile(r"^详细地址经度纬度$")).get_by_role("textbox").nth(1).fill(site_lon)
            self.page.locator("div").filter(has_text=re.compile(r"^详细地址经度纬度$")).get_by_role("textbox").nth(2).fill(site_lat)
            self.page.get_by_role("button", name="选择").click()
            self.page.get_by_role("row", name="站点大屏 选择").get_by_role("button").click()
            self.page.get_by_role("dialog", name="站点信息").get_by_placeholder("请选择").nth(4).click()
            self.page.get_by_role("listitem").filter(has_text="admin").click()
            self.page.get_by_role("button", name="保存").click()    
    