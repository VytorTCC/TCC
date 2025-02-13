# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestBuscaDetalhada():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_buscaDetalhada(self):
    # Test name: Busca_Detalhada
    # Step # | name | target | value
    # 1 | open | https://dashboard.plataformabyou.com.br/visao-geral | 
    self.driver.get("https://dashboard.plataformabyou.com.br/visao-geral")
    # 2 | setWindowSize | 1382x784 | 
    self.driver.set_window_size(1382, 784)
    # 3 | runScript | window.scrollTo(0,253) | 
    self.driver.execute_script("window.scrollTo(0,253)")
    # 4 | mouseOver | css=.fa-magnifying-glass > path | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".fa-magnifying-glass > path")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 5 | click | css=.fa-magnifying-glass > path | 
    self.driver.find_element(By.CSS_SELECTOR, ".fa-magnifying-glass > path").click()
    # 6 | mouseOut | css=.fa-magnifying-glass > path | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 7 | click | css=.MuiGrid-root:nth-child(1) > .MuiAutocomplete-root .MuiInputBase-root | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiGrid-root:nth-child(1) > .MuiAutocomplete-root .MuiInputBase-root").click()
    # 8 | mouseOver | css=.MuiAutocomplete-popupIndicatorOpen > .MuiSvgIcon-root | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".MuiAutocomplete-popupIndicatorOpen > .MuiSvgIcon-root")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 9 | mouseOut | css=.MuiGrid-root:nth-child(1) > .MuiAutocomplete-root .MuiSvgIcon-root | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 10 | click | css=.MuiGrid-root:nth-child(1) > .MuiAutocomplete-root .MuiSvgIcon-root | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiGrid-root:nth-child(1) > .MuiAutocomplete-root .MuiSvgIcon-root").click()
    # 11 | click | id=status-auto-complete-option-0 | 
    self.driver.find_element(By.ID, "status-auto-complete-option-0").click()
    # 12 | click | id=users-auto-complete | 
    self.driver.find_element(By.ID, "users-auto-complete").click()
    # 13 | click | id=users-auto-complete-option-0 | 
    self.driver.find_element(By.ID, "users-auto-complete-option-0").click()
    # 14 | mouseOver | css=.MuiBox-root:nth-child(1) > .MuiStack-root .MuiSvgIcon-root | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".MuiBox-root:nth-child(1) > .MuiStack-root .MuiSvgIcon-root")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 15 | click | id=procedures-auto-complete | 
    self.driver.find_element(By.ID, "procedures-auto-complete").click()
    # 16 | click | id=procedures-auto-complete-option-0 | 
    self.driver.find_element(By.ID, "procedures-auto-complete-option-0").click()
    # 17 | mouseOver | css=.MuiAutocomplete-popupIndicatorOpen > .MuiSvgIcon-root | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".MuiAutocomplete-popupIndicatorOpen > .MuiSvgIcon-root")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 18 | click | css=.MuiGrid-root:nth-child(4) .MuiInputBase-root | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiGrid-root:nth-child(4) .MuiInputBase-root").click()
    # 19 | mouseOver | css=.MuiAutocomplete-popupIndicatorOpen > .MuiSvgIcon-root | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".MuiAutocomplete-popupIndicatorOpen > .MuiSvgIcon-root")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 20 | click | css=.MuiAutocomplete-popupIndicatorOpen > .MuiSvgIcon-root | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiAutocomplete-popupIndicatorOpen > .MuiSvgIcon-root").click()
    # 21 | click | css=.MuiGrid-root:nth-child(4) .MuiSvgIcon-root | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiGrid-root:nth-child(4) .MuiSvgIcon-root").click()
    # 22 | mouseOut | css=.MuiAutocomplete-popupIndicatorOpen > .MuiSvgIcon-root | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 23 | click | css=.MuiAutocomplete-noOptions | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiAutocomplete-noOptions").click()
    # 24 | click | id=search-input | 
    self.driver.find_element(By.ID, "search-input").click()
    # 25 | mouseOver | css=.MuiGrid-root:nth-child(1) > .MuiAutocomplete-root .MuiSvgIcon-root | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".MuiGrid-root:nth-child(1) > .MuiAutocomplete-root .MuiSvgIcon-root")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 26 | click | css=.MuiGrid-root:nth-child(1) > .MuiAutocomplete-root .MuiSvgIcon-root | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiGrid-root:nth-child(1) > .MuiAutocomplete-root .MuiSvgIcon-root").click()
    # 27 | mouseOut | css=.MuiAutocomplete-popupIndicatorOpen > .MuiSvgIcon-root | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 28 | click | id=status-auto-complete-option-1 | 
    self.driver.find_element(By.ID, "status-auto-complete-option-1").click()
    # 29 | click | css=.Mui-focused:nth-child(2) | 
    self.driver.find_element(By.CSS_SELECTOR, ".Mui-focused:nth-child(2)").click()
    # 30 | mouseOver | css=.MuiGrid-root:nth-child(1) > .MuiAutocomplete-root .MuiSvgIcon-root | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".MuiGrid-root:nth-child(1) > .MuiAutocomplete-root .MuiSvgIcon-root")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 31 | mouseOver | css=.MuiAutocomplete-popupIndicatorOpen > .MuiSvgIcon-root | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".MuiAutocomplete-popupIndicatorOpen > .MuiSvgIcon-root")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 32 | click | css=.MuiAutocomplete-popupIndicatorOpen > .MuiSvgIcon-root | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiAutocomplete-popupIndicatorOpen > .MuiSvgIcon-root").click()
    # 33 | click | css=.MuiGrid-root:nth-child(1) > .MuiAutocomplete-root .MuiSvgIcon-root | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiGrid-root:nth-child(1) > .MuiAutocomplete-root .MuiSvgIcon-root").click()
    # 34 | mouseOut | css=.MuiAutocomplete-popupIndicatorOpen > .MuiSvgIcon-root | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 35 | click | id=status-auto-complete-option-2 | 
    self.driver.find_element(By.ID, "status-auto-complete-option-2").click()
    # 36 | mouseOver | css=.MuiGrid-root:nth-child(2) > .MuiAutocomplete-root .MuiButtonBase-root | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".MuiGrid-root:nth-child(2) > .MuiAutocomplete-root .MuiButtonBase-root")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 37 | click | css=.MuiGrid-root:nth-child(2) > .MuiAutocomplete-root .MuiButtonBase-root | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiGrid-root:nth-child(2) > .MuiAutocomplete-root .MuiButtonBase-root").click()
    # 38 | mouseOut | css=.MuiAutocomplete-popupIndicatorOpen | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 39 | click | id=users-auto-complete-option-4 | 
    self.driver.find_element(By.ID, "users-auto-complete-option-4").click()
    # 40 | mouseOver | css=.MuiGrid-root:nth-child(2) path | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".MuiGrid-root:nth-child(2) path")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 41 | click | css=.MuiGrid-root:nth-child(2) path | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiGrid-root:nth-child(2) path").click()
    # 42 | mouseOut | css=.MuiAutocomplete-popupIndicatorOpen path | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 43 | click | id=users-auto-complete-option-0 | 
    self.driver.find_element(By.ID, "users-auto-complete-option-0").click()
    # 44 | click | css=.MuiGrid-root:nth-child(1) > .MuiAutocomplete-root .MuiInputBase-root | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiGrid-root:nth-child(1) > .MuiAutocomplete-root .MuiInputBase-root").click()
    # 45 | mouseOver | css=.MuiGrid-root:nth-child(1) > .MuiAutocomplete-root .MuiSvgIcon-root | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".MuiGrid-root:nth-child(1) > .MuiAutocomplete-root .MuiSvgIcon-root")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 46 | mouseOut | css=.MuiAutocomplete-popupIndicatorOpen > .MuiSvgIcon-root | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 47 | mouseOver | css=.MuiAutocomplete-popupIndicatorOpen | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".MuiAutocomplete-popupIndicatorOpen")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 48 | click | css=.MuiAutocomplete-popupIndicatorOpen | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiAutocomplete-popupIndicatorOpen").click()
    # 49 | mouseOut | css=.Mui-focused .MuiButtonBase-root | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 50 | mouseOver | css=.MuiGrid-root:nth-child(1) > .MuiAutocomplete-root .MuiSvgIcon-root | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".MuiGrid-root:nth-child(1) > .MuiAutocomplete-root .MuiSvgIcon-root")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 51 | click | css=.MuiGrid-root:nth-child(1) > .MuiAutocomplete-root .MuiSvgIcon-root | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiGrid-root:nth-child(1) > .MuiAutocomplete-root .MuiSvgIcon-root").click()
    # 52 | mouseOut | css=.MuiAutocomplete-popupIndicatorOpen > .MuiSvgIcon-root | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 53 | click | id=status-auto-complete-option-5 | 
    self.driver.find_element(By.ID, "status-auto-complete-option-5").click()
    # 54 | click | id=professionals-auto-complete | 
    self.driver.find_element(By.ID, "professionals-auto-complete").click()
    # 55 | click | id=professionals-auto-complete-option-1 | 
    self.driver.find_element(By.ID, "professionals-auto-complete-option-1").click()
    # 56 | click | css=.MuiGrid-root:nth-child(4) .MuiInputBase-root | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiGrid-root:nth-child(4) .MuiInputBase-root").click()
    # 57 | click | css=.MuiAutocomplete-noOptions | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiAutocomplete-noOptions").click()
    # 58 | click | id=search-input | 
    self.driver.find_element(By.ID, "search-input").click()
    # 59 | mouseOver | css=#filter-button > .MuiTypography-root | 
    element = self.driver.find_element(By.CSS_SELECTOR, "#filter-button > .MuiTypography-root")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 60 | click | css=#filter-button > .MuiTypography-root | 
    self.driver.find_element(By.CSS_SELECTOR, "#filter-button > .MuiTypography-root").click()
    # 61 | mouseOut | css=#filter-button > .MuiTypography-root | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 62 | mouseOver | css=.MuiBox-root:nth-child(1) > .MuiStack-root .MuiSvgIcon-root | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".MuiBox-root:nth-child(1) > .MuiStack-root .MuiSvgIcon-root")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 63 | click | css=.MuiBox-root:nth-child(1) > .MuiStack-root .MuiSvgIcon-root | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiBox-root:nth-child(1) > .MuiStack-root .MuiSvgIcon-root").click()
    # 64 | mouseOut | css=.MuiBox-root:nth-child(1) > .MuiStack-root .MuiSvgIcon-root | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 65 | mouseOver | css=.MuiDayCalendar-weekContainer:nth-child(2) > .MuiButtonBase-root:nth-child(4) | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".MuiDayCalendar-weekContainer:nth-child(2) > .MuiButtonBase-root:nth-child(4)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 66 | click | css=.MuiDayCalendar-weekContainer:nth-child(2) > .MuiButtonBase-root:nth-child(4) | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiDayCalendar-weekContainer:nth-child(2) > .MuiButtonBase-root:nth-child(4)").click()
    # 67 | mouseOut | css=.MuiDayCalendar-weekContainer:nth-child(2) > .MuiButtonBase-root:nth-child(4) | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 68 | mouseOver | css=#filter-button > .MuiTypography-root | 
    element = self.driver.find_element(By.CSS_SELECTOR, "#filter-button > .MuiTypography-root")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 69 | click | css=#filter-button > .MuiTypography-root | 
    self.driver.find_element(By.CSS_SELECTOR, "#filter-button > .MuiTypography-root").click()
    # 70 | mouseOut | css=#filter-button > .MuiTypography-root | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 71 | mouseOver | css=.css-hboir5 > #filter-button | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".css-hboir5 > #filter-button")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 72 | click | css=.css-hboir5 > #filter-button | 
    self.driver.find_element(By.CSS_SELECTOR, ".css-hboir5 > #filter-button").click()
    # 73 | mouseOut | css=.css-hboir5 > #filter-button | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 74 | click | css=.MuiButtonBase-root:nth-child(3) .MuiTypography-root | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiButtonBase-root:nth-child(3) .MuiTypography-root").click()
    # 75 | click | css=.MuiButtonBase-root:nth-child(3) .MuiTypography-root | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiButtonBase-root:nth-child(3) .MuiTypography-root").click()
    # 76 | doubleClick | css=.MuiButtonBase-root:nth-child(3) .MuiTypography-root | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".MuiButtonBase-root:nth-child(3) .MuiTypography-root")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    # 77 | click | css=.MuiBackdrop-root | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiBackdrop-root").click()
    # 78 | click | css=.MuiBackdrop-root | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiBackdrop-root").click()
    # 79 | click | id=search-input | 
    self.driver.find_element(By.ID, "search-input").click()
    # 80 | type | id=search-input | teste
    self.driver.find_element(By.ID, "search-input").send_keys("teste")
    # 81 | sendKeys | id=search-input | ${KEY_ENTER}
    self.driver.find_element(By.ID, "search-input").send_keys(Keys.ENTER)
    # 82 | click | id=search-input | 
    self.driver.find_element(By.ID, "search-input").click()
    # 83 | click | id=search-input | 
    self.driver.find_element(By.ID, "search-input").click()
    # 84 | doubleClick | id=search-input | 
    element = self.driver.find_element(By.ID, "search-input")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    # 85 | click | id=search-input | 
    self.driver.find_element(By.ID, "search-input").click()
    # 86 | click | css=.css-f3cthu .MuiInputBase-root | 
    self.driver.find_element(By.CSS_SELECTOR, ".css-f3cthu .MuiInputBase-root").click()
    # 87 | mouseOver | css=.MuiBox-root:nth-child(1) > .MuiStack-root .MuiSvgIcon-root | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".MuiBox-root:nth-child(1) > .MuiStack-root .MuiSvgIcon-root")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 88 | click | css=.MuiBox-root:nth-child(1) > .MuiStack-root .MuiSvgIcon-root | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiBox-root:nth-child(1) > .MuiStack-root .MuiSvgIcon-root").click()
    # 89 | mouseOut | css=.MuiBox-root:nth-child(1) > .MuiStack-root .MuiSvgIcon-root | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 90 | mouseOver | css=.MuiDayCalendar-weekContainer:nth-child(4) > .MuiButtonBase-root:nth-child(6) | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".MuiDayCalendar-weekContainer:nth-child(4) > .MuiButtonBase-root:nth-child(6)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 91 | click | css=.MuiDayCalendar-weekContainer:nth-child(4) > .MuiButtonBase-root:nth-child(6) | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiDayCalendar-weekContainer:nth-child(4) > .MuiButtonBase-root:nth-child(6)").click()
    # 92 | click | id=date-picker-inline-start | 
    self.driver.find_element(By.ID, "date-picker-inline-start").click()
    # 93 | click | id=date-picker-inline-start | 
    self.driver.find_element(By.ID, "date-picker-inline-start").click()
    # 94 | doubleClick | id=date-picker-inline-start | 
    element = self.driver.find_element(By.ID, "date-picker-inline-start")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    # 95 | click | id=date-picker-inline-start | 
    self.driver.find_element(By.ID, "date-picker-inline-start").click()
    # 96 | mouseOver | css=.MuiBox-root:nth-child(4) > .MuiStack-root .MuiSvgIcon-root | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".MuiBox-root:nth-child(4) > .MuiStack-root .MuiSvgIcon-root")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 97 | click | css=.MuiBox-root:nth-child(4) > .MuiStack-root .MuiSvgIcon-root | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiBox-root:nth-child(4) > .MuiStack-root .MuiSvgIcon-root").click()
    # 98 | mouseOut | css=.MuiBox-root:nth-child(4) > .MuiStack-root .MuiSvgIcon-root | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 99 | mouseOver | css=.MuiDayCalendar-weekContainer:nth-child(3) > .MuiButtonBase-root:nth-child(4) | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".MuiDayCalendar-weekContainer:nth-child(3) > .MuiButtonBase-root:nth-child(4)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 100 | click | css=.MuiDayCalendar-weekContainer:nth-child(3) > .MuiButtonBase-root:nth-child(4) | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiDayCalendar-weekContainer:nth-child(3) > .MuiButtonBase-root:nth-child(4)").click()
    # 101 | mouseOut | css=.MuiDayCalendar-weekContainer:nth-child(3) > .MuiButtonBase-root:nth-child(4) | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 102 | click | css=.MuiGrid-root:nth-child(5) | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiGrid-root:nth-child(5)").click()
    # 103 | mouseOver | css=.fa-door-open > path | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".fa-door-open > path")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 104 | mouseOut | css=.fa-door-open > path | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 105 | mouseOver | id=equipments-button | 
    element = self.driver.find_element(By.ID, "equipments-button")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 106 | mouseOut | id=equipments-button | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 107 | mouseOver | id=detailedSearch-button | 
    element = self.driver.find_element(By.ID, "detailedSearch-button")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 108 | mouseOut | id=detailedSearch-button | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 109 | click | id=sidebar-logout | 
    self.driver.find_element(By.ID, "sidebar-logout").click()
    # 110 | runScript | window.scrollTo(0,0) | 
    self.driver.execute_script("window.scrollTo(0,0)")
  
