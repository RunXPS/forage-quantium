from task4 import update_graph
from task4 import app
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import time

service = Service(executable_path="C:/Users/super/CodePractice/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service)  # Optional argument, if not specified will search path.

# driver = webdriver.Chrome()

# --- update_graph --- #

def test_sigular_update_graph_callback():
    """ Testing 'update_graph' for each of the singular regions """
    outputs = [update_graph("south")['data'][0]['name'], update_graph("north")['data'][0]['name'], update_graph("east")['data'][0]['name'], update_graph("west")['data'][0]['name']]
    assert outputs == ['south', 'north', 'east', 'west']

def test_all_update_graph_callback():
    """ Testing 'update_graph' using 'all' """
    output = update_graph('all')['data']
    arr = []
    for idx in range(0,len(output)):
        arr.append(output[idx]['name'])
    assert arr == ['north', 'south', 'east', 'west']

def test_none_update_graph_callback():
    """ Testing 'update_graph' without a positional arguement """
    with pytest.raises(TypeError):
        update_graph()

# --- elements are present --- #

def test_elements_present():
    """ Testing if the site has a header """
    driver.get("http://127.0.0.1:8050")
    header = driver.find_elements(by=By.TAG_NAME, value="header")
    graph = driver.find_elements(by=By.TAG_NAME, value="svg")
    radio = driver.find_elements(by=By.ID, value="region_set")
    #button = driver.find_elements(by=By.TAG_NAME, value="button")
    time.sleep(5)
    driver.quit()
    assert header != [] and graph != [] and radio != []


def test_header_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#header", timeout=10)


def test_visualization_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#visualization", timeout=10)


def test_region_picker_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region_picker", timeout=10)