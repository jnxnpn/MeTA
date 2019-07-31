'''

盈利能力指标（50%）：
文献原文指标：资产净利率20%、销售净利率20%、净值报酬率10%
用巨潮网指标表示的计算公式：2*profit/(last_asset+asset)、profit/revenue、2*profit/(last_asset+asset-last_liability-liability)

营运能力指标（30%）：
文献原文指标：自有资本比率15%、流动比率15%
用巨潮网指标表示的计算公式：(last_asset+asset-last_liability-liability)/(last_asset+asset)、(last_casset+casset)/(last_cliability+cliability

成长能力指标（20%）：
文献原文指标：销售增长率6.667%、净利增长率6.667%、资产增长率6.667%
用巨潮网指标表示的计算公式：profitgrowth、revenue/last_revenue-1、assetgrowth

'''

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import openpyxl

code = input("输入股票名称或代码")

url0 = "http://www.cninfo.com.cn/"

# 打开火狐浏览器
option = webdriver.FirefoxOptions()
option.add_argument('--user-data-dir=C:\\Users\\LMR\\AppData\\Local\\Google\\Chrome\\User Data')  # 设置成用户自己的数据目录
browser = webdriver.Firefox()
browser.get(url0)

browser.find_element_by_xpath("//input[@name='keyWord']").clear()
browser.find_element_by_xpath("//input[@name='keyWord']").send_keys(code)
time.sleep(1)
xoyelement = browser.find_element_by_xpath('//div[@class="search-inner"]')  # 基准元素
ActionChains(browser).move_to_element(xoyelement).perform()
ActionChains(browser).move_by_offset(0, 40).click().perform()
time.sleep(1)
url = browser.current_url+'&tabName=data&type=info'
browser.get(url)

browser.find_element_by_xpath("//select[@id='mainSelect']").click()
ActionChains(browser).move_by_offset(0, 85).perform()

# 定位网页中插入的主要指标表格
zhibiao = browser.find_element_by_css_selector('#companyzhibiao')
# 提取表格内容
zcontent = zhibiao.find_elements_by_tag_name("td")  # 进一步定位到表格内容所在的td节点
zlist = []  # 存储为list
for td in zcontent:
    zlist.append(td.text)

# 定位网页中插入的利润表
profittable = browser.find_element_by_css_selector('#companyliruan')
# 提取表格内容
pcontent = profittable.find_elements_by_tag_name("td")  # 进一步定位到表格内容所在的td节点
plist = []  # 存储为list
for td in pcontent:
    plist.append(td.text)
for p in plist:
    print(p)

# 定位网页中插入的资产负债表
balancesheet = browser.find_element_by_css_selector('#companyzichan')
# 提取表格内容
bcontent = balancesheet.find_elements_by_tag_name("td")  # 进一步定位到表格内容所在的td节点
blist = []  # 存储为list
for td in bcontent:
    blist.append(td.text)

revenue = float(plist[10])
last_revenue = float(plist[9])
profit = float(plist[65])
asset = float(blist[54])
last_asset = float(blist[53])
casset = float(blist[32])
last_casset = float(blist[31])
liability = float(blist[109])
last_liability = float(blist[108])
cliability = float(blist[76])
last_cliability = float(blist[75])
profitgrowth = float(zlist[65])/100
assetgrowth = float(zlist[54])/100

# 统计出的行业平均值
m1 = 2*profit/(last_asset+asset)
m2 = profit/revenue
m3 = 2*profit/(last_asset+asset-last_liability-liability)
m4 = (last_asset+asset-last_liability-liability)/(last_asset+asset)
m5 = (last_casset+casset)/(last_cliability+cliability)
m6 = profitgrowth
m7 = revenue/last_revenue-1
m8 = assetgrowth

a1 = 0.13
a2 = 0.27
a3 = 0.23
a4 = 0.56
a5 = 1.88
a6 = 0.13
a7 = 0.14
a8 = 0.68


v1 = 20*m1/a1
v2 = 20*m2/a2
v3 = 10*m3/a3
v4 = 15*m4/a4
v5 = 15*m5/a5
v6 = 20/3*m6/a6
v7 = 20/3*m7/a7
v8 = 20/3*m8/a8
