import pytest
from selene import browser, be, have

def test_one(open_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('html').should(have.text('yashaka.github.io'))

def test_second(open_browser):
    browser.element('[name="q"]').should(be.blank).type('15qw4e7rqwqererry').press_enter()
    browser.element('[class="deB7ubqmD22Y2q4Hxlgr FTHtdWkuKDa5mfka2ns5"]').should(have.text('По запросу «15qw4e7rqwqererry» ничего не найдено.'))

