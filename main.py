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
    (site_id,site_name,site_region,bat_num)=Excelutil.getSiteIdandName(r".\docs\站点清单.xlsx",'禅城站点')
    #headless=False
    browser = playwright.chromium.launch(channel="msedge")
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://www.jrie.com.cn/")
    account="lsenergy"
    password="123456"
    group_name="电源用电量曲线(禅城)"
    data_name="有功总电能"
    PageUtil.Login(page,account,password)
    PageUtil.ArrangeEP(page,site_id,site_name,group_name,data_name)

    # ---------------------
    context.close()
    browser.close()