from selenium import webdriver


ch_options = webdriver.ChromeOptions()
ch_options.add_argument("--headless")
ch_options.add_argument("--no-sandbox")
ch_options.add_argument("--disable-gpu")
ch_options.add_argument("--disable-dev-shm-usage")
# prefs = {"profile.managed_default_content_settings.images": 2}
# ch_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=ch_options)
#把上述地址改成你电脑中geckodriver.exe程序的地址
#在虚拟浏览器中打开 Airbnb 页面
driver.get("https://zh.airbnb.com/s/taipei")
driver.page_source
#找到页面中所有的出租房
rent_list = driver.find_elements_by_css_selector('a._okj6x')

#对于每一个出租房
for eachhouse in rent_list:
    #找到评论数量
    try:
        comment = eachhouse.find_element_by_css_selector('span._1clmxfj')
        comment = comment.text
    except:
        comment = 0
    
    #找到价格
    price = eachhouse.find_element_by_css_selector('div._18gk84h')
    price = price.find_elements_by_tag_name('span')
    price = price[1]
    # price = price.text.replace("每晚", "").replace("价格", "").replace("\n", "")
    price = price.text
    
    #找到名称
    name = eachhouse.find_element_by_css_selector('div._qrfr9x5')
    name = name.text
    
    #找到房屋类型，大小
    details = eachhouse.find_element_by_css_selector('span[style="color: rgb(118, 118, 118);"]')
    details = details.text
    # house_type = details.split(" · ")[0]
    # bed_number = details.split(" · ")[1]
    print (comment, price, name, details)
    print("____________________________")