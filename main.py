#
 # @Date: 2025-02-27 11:57:49
 # @Author: thirky
 # @Description: 必须要在网络正常条件下运行本程序
 #
import sys
sys.path.append(r'.\package')
from playwright.sync_api import sync_playwright
import PageUtil
import Excelutil
with sync_playwright() as playwright:
    (site_id,site_name,site_region)=Excelutil.getSiteIdandRegion(r".\docs\站点表.xlsx",'深圳市')
    #headless=False
    browser = playwright.chromium.launch(channel="msedge",headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://www.jrie.com.cn/")
    PageUtil.Login(page,account="admin",password="jinrong1101") 
    group_name="电源用电量曲线(禅城)"
    data_name="有功总电能"
    PageUtil.UploadFiles(page,site_id,"深圳市",area=None)

    # ---------------------
    context.close()
    browser.close()