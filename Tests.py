import time
from json_data import *

#################### locators ####################
co2_counter = '//*[@class="desktop-impact-item-eeQO3"][2]'
water_counter = '//*[@class="desktop-impact-item-eeQO3"][4]'
energy_counter = '//*[@class="desktop-impact-item-eeQO3"][6]'

###################### data ######################
main_url = 'https://www.avito.ru/avito-care/eco-impact'
mock_url = 'https://www.avito.ru/web/1/charity/ecoImpact/init'



def test_1_negative_values(page):
    page.route(mock_url, lambda route: route.fulfill(json=negative_values_json))
    page.goto(main_url)
    time.sleep(3)
    page.locator(co2_counter).screenshot(path='./output/test1-CO2.png')
    page.locator(water_counter).screenshot(path='./output/test1-water.png')
    page.locator(energy_counter).screenshot(path='./output/test1-energy.png')
    page.close()


def test_2_zero_boundary(page):
    page.route(mock_url, lambda route: route.fulfill(json=zero_values_json))
    page.goto(main_url)
    time.sleep(3)
    page.locator(co2_counter).screenshot(path='./output/test2-CO2.png')
    page.locator(water_counter).screenshot(path='./output/test2-water.png')
    page.locator(energy_counter).screenshot(path='./output/test2-energy.png')
    page.close()


def test_3_positive_units(page):
    page.route(mock_url, lambda route: route.fulfill(json=positive_units_json))
    page.goto(main_url)
    time.sleep(3)
    page.locator(co2_counter).screenshot(path='./output/test3-CO2.png')
    page.locator(water_counter).screenshot(path='./output/test3-water.png')
    page.locator(energy_counter).screenshot(path='./output/test3-energy.png')
    page.close()


def test_4_below_thousand_boundary(page):
    page.route(mock_url, lambda route: route.fulfill(json=thousand_boundary_below_json))
    page.goto(main_url)
    time.sleep(3)
    page.locator(co2_counter).screenshot(path='./output/test4-CO2.png')
    page.locator(water_counter).screenshot(path='./output/test4-water.png')
    page.locator(energy_counter).screenshot(path='./output/test4-energy.png')
    page.close()


def test_5_thousand_boundary(page):
    page.route(mock_url, lambda route: route.fulfill(json=thousand_boundary_json))
    page.goto(main_url)
    time.sleep(3)
    page.locator(co2_counter).screenshot(path='./output/test5-CO2.png')
    page.locator(water_counter).screenshot(path='./output/test5-water.png')
    page.locator(energy_counter).screenshot(path='./output/test5-energy.png')
    page.close()


def test_6_above_thousand_boundary(page):
    page.route(mock_url, lambda route: route.fulfill(json=thousand_boundary_above_json))
    page.goto(main_url)
    time.sleep(3)
    page.locator(co2_counter).screenshot(path='./output/test6-CO2.png')
    page.locator(water_counter).screenshot(path='./output/test6-water.png')
    page.locator(energy_counter).screenshot(path='./output/test6-energy.png')
    page.close()


def test_7_below_millions_boundary(page):
    page.route(mock_url, lambda route: route.fulfill(json=millions_boundary_below_json))
    page.goto(main_url)
    time.sleep(3)
    page.locator(co2_counter).screenshot(path='./output/test7-CO2.png')
    page.locator(water_counter).screenshot(path='./output/test7-water.png')
    page.locator(energy_counter).screenshot(path='./output/test7-energy.png')
    page.close()


def test_8_millions_boundary(page):
    page.route(mock_url, lambda route: route.fulfill(json=millions_boundary_json))
    page.goto(main_url)
    time.sleep(3)
    page.locator(co2_counter).screenshot(path='./output/test8-CO2.png')
    page.locator(water_counter).screenshot(path='./output/test8-water.png')
    page.locator(energy_counter).screenshot(path='./output/test8-energy.png')
    page.close()


def test_9_above_millions_boundary(page):
    page.route(mock_url, lambda route: route.fulfill(json=millions_boundary_above_json))
    page.goto(main_url)
    time.sleep(3)
    page.locator(co2_counter).screenshot(path='./output/test9-CO2.png')
    page.locator(water_counter).screenshot(path='./output/test9-water.png')
    page.locator(energy_counter).screenshot(path='./output/test9-energy.png')
    page.close()


def test_10_below_billions_boundary(page):
    page.route(mock_url, lambda route: route.fulfill(json=billions_boundary_below_json))
    page.goto(main_url)
    time.sleep(3)
    page.locator(co2_counter).screenshot(path='./output/test10-CO2.png')
    page.locator(water_counter).screenshot(path='./output/test10-water.png')
    page.locator(energy_counter).screenshot(path='./output/test10-energy.png')
    page.close()


def test_11_billions_boundary(page):
    page.route(mock_url, lambda route: route.fulfill(json=billions_boundary_json))
    page.goto(main_url)
    time.sleep(3)
    page.locator(co2_counter).screenshot(path='./output/test11-CO2.png')
    page.locator(water_counter).screenshot(path='./output/test11-water.png')
    page.locator(energy_counter).screenshot(path='./output/test11-energy.png')
    page.close()


def test_12_above_billions_boundary(page):
    page.route(mock_url, lambda route: route.fulfill(json=billions_boundary_above_json))
    page.goto(main_url)
    time.sleep(3)
    page.locator(co2_counter).screenshot(path='./output/test12-CO2.png')
    page.locator(water_counter).screenshot(path='./output/test12-water.png')
    page.locator(energy_counter).screenshot(path='./output/test12-energy.png')
    page.close()


def test_13_below_trillions_boundary(page):
    page.route(mock_url, lambda route: route.fulfill(json=trillions_boundary_below_json))
    page.goto(main_url)
    time.sleep(3)
    page.locator(co2_counter).screenshot(path='./output/test13-CO2.png')
    page.locator(water_counter).screenshot(path='./output/test13-water.png')
    page.locator(energy_counter).screenshot(path='./output/test13-energy.png')
    page.close()


def test_14_trillions_boundary(page):
    page.route(mock_url, lambda route: route.fulfill(json=trillions_boundary_json))
    page.goto(main_url)
    time.sleep(3)
    page.locator(co2_counter).screenshot(path='./output/test14-CO2.png')
    page.locator(water_counter).screenshot(path='./output/test14-water.png')
    page.locator(energy_counter).screenshot(path='./output/test14-energy.png')
    page.close()


def test_15_above_trillions_boundary(page):
    page.route(mock_url, lambda route: route.fulfill(json=trillions_boundary_above_json))
    page.goto(main_url)
    time.sleep(3)
    page.locator(co2_counter).screenshot(path='./output/test15-CO2.png')
    page.locator(water_counter).screenshot(path='./output/test15-water.png')
    page.locator(energy_counter).screenshot(path='./output/test15-energy.png')
    page.close()


def test_16_below_max_boundary(page):
    page.route(mock_url, lambda route: route.fulfill(json=below_max_value_json))
    page.goto(main_url)
    time.sleep(3)
    page.locator(co2_counter).screenshot(path='./output/test16-CO2.png')
    page.locator(water_counter).screenshot(path='./output/test16-water.png')
    page.locator(energy_counter).screenshot(path='./output/test16-energy.png')
    page.close()


def test_17_max_boundary(page):
    page.route(mock_url, lambda route: route.fulfill(json=max_value_json))
    page.goto(main_url)
    time.sleep(3)
    page.locator(co2_counter).screenshot(path='./output/test17-CO2.png')
    page.locator(water_counter).screenshot(path='./output/test17-water.png')
    page.locator(energy_counter).screenshot(path='./output/test17-energy.png')
    page.close()


def test_18_negative_testing(page):
    page.route(mock_url, lambda route: route.fulfill(json=insane_json))
    page.goto(main_url)
    time.sleep(5)
    page.locator(co2_counter).screenshot(path='./output/test18-CO2.png')
    page.locator(water_counter).screenshot(path='./output/test18-water.png')
    page.locator(energy_counter).screenshot(path='./output/test18-energy.png')
    page.close()