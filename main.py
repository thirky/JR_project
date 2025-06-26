#
 # @Date: 2025-02-27 11:57:49
 # @Author: thirky
 # @Description: 必须要在网络正常条件下运行本程序
 #
import sys
sys.path.append(r'.\adapters')
from playwright.sync_api import sync_playwright
from core.PlatformAutomator import PlatformAutomator
from adapters.ExcelUtil import ExcelUtil


with PlatformAutomator(headless=False) as platformautomator:
    platformautomator.login("admin", "jinrong1101")
    site_data= ExcelUtil.getSiteIdandRegion('深圳市')
    site_id = site_data['site_id']
    site_name = site_data['site_name']
    site_region = site_data['site_region']
    platformautomator.UploadFiles(site_id, "深圳市", area=None)


