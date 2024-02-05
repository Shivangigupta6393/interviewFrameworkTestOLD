import os,pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# current_directory = os.getcwd()
# current_dir = (current_directory.rsplit("/", 1))[0]
# path = current_dir + "/driverObjects" #path to the drivers for various browsers
#print(path)

import csv


def get_test_data_from_csv():
        with open("./testData/test1.csv", "r") as file:
                csvreader = csv.reader(file)
                rows = [row for row in csvreader]
                #titles = rows[1]
                rows.pop(0)
                rows.pop(0)
                #print(f"rows is {rows} length is {len(rows)}&& titles are {titles}")
        return (rows)

@pytest.fixture(params = get_test_data_from_csv())
def test_data(request):
        return request.param

@pytest.fixture(scope= "class")
def setup(request):
        serv_obj = Service("driverObjects/chromedriver")
        # email = request.param[0]
        # name = request.param[1]
        # company = request.param[2]
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("head")
        #options.add_argument("--start-maximized")
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36')
        options.add_argument("--ignore-certificate-errors")
        options.page_load_strategy = "eager" #handling

        driver = webdriver.Chrome(service=serv_obj,
                                  options=options
                                  )
        driver.implicitly_wait(10)
        url = "https://dlptest.com/"
        #https://rahulshettyacademy.com/angularpractice/
        driver.get(url)
        driver.maximize_window()
        print("setup ended"+ f"driver url is {driver.current_url}")
        request.cls.driver = driver
        yield
        driver.close()

