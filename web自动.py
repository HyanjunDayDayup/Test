from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

# 指定 ChromeDriver 的路径
chromedriver_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
# 找不到这个driver路径在哪里，也不想下载，就这样吧。
service = Service(chromedriver_path)

# 创建 WebDriver 实例
driver = webdriver.Chrome(service=service)

try:
    # 打开 Google 首页
    driver.get('https://www.baidu.com')
    print("成功打开百度首页")

    # # 找到搜索框元素
    # search_box = driver.find_element(By.ID, 'inputWrapper')

    # # 在搜索框中输入查询并按下回车键
    # search_query = 'Selenium Python'
    # search_box.send_keys(search_query + Keys.RETURN)

    # 等待几秒钟查看结果（可选）
    driver.implicitly_wait(10)

    # 打印页面标题
    # print(driver.title)

finally:
    # 关闭浏览器
    driver.quit()
