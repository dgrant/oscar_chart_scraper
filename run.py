#!/usr/bin/env python3
import argparse
import os
import shutil
from selenium import webdriver

from page import SearchPage, EncounterPage, SignInPage
import time

scrape_charts_dir = '/tmp/oscar_scrape_charts'

options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
  "download.default_directory": scrape_charts_dir,
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})


def wait_for_file():
    num_seconds = 0
    delay = 1
    while num_seconds < 120:
        files = os.listdir(scrape_charts_dir)
        if len(files) > 0 and files[0].find('Encounter') == 0:
            return
        else:
            time.sleep(delay)
            num_seconds += delay
            delay = delay * 2


def get_driver():
    return webdriver.Chrome(executable_path='chromedriver', chrome_options=options)


def sign_in(driver, url, user, password, pin):
    print('Sign-in page')
    sign_in_page = SignInPage(url, driver)
    sign_in_page.is_loaded()
    sign_in_page.fill(user, password, pin)


def copy_encounter_file(phn, output_dir):
    files = os.listdir(scrape_charts_dir)
    assert len(files) == 1
    encounter_file = files[0]
    src = os.path.join(scrape_charts_dir, encounter_file)
    dest = os.path.join(output_dir, '{0}_{1}.pdf'.format(phn, 'encounter'))
    shutil.copy(src, dest)


def export_phn_numbers(url, phn_numbers, output_dir, username, password, pin):
    driver = get_driver()

    sign_in(driver, url, username, password, pin)

    for phn_number in phn_numbers:
        if os.path.isdir(scrape_charts_dir):
            shutil.rmtree(scrape_charts_dir)
        os.makedirs(scrape_charts_dir)

        print("Doing PHN: ", phn_number)
        search_window = driver.current_window_handle
        search_page = SearchPage(url, driver)
        search_page.search_by_phn_number(phn_number)

        handles = driver.window_handles
        handles.remove(search_window)
        encounter_window = handles[0]
        driver.switch_to.window(encounter_window)
        encounter_page = EncounterPage(driver)
        encounter_page.is_loaded()

        encounter_page.print_all()
        wait_for_file()

        copy_encounter_file(phn_number, output_dir)

        driver.close()
        driver.switch_to.window(search_window)


def export(url, phn_input_file, output_directory, username, password, pin):
    phn_numbers = [x.strip() for x in open(phn_input_file).readlines()]
    print('phn_numbers=', phn_numbers)
    export_phn_numbers(url, phn_numbers, output_directory, username, password, pin)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='OSCAR EMR url')
    parser.add_argument('phn_input_file', help='input file containing list of PHN numbers to export')
    parser.add_argument('output_directory', help='output directory')
    parser.add_argument('credentials', help='comma-delimited credentials, eg. dave:password:pin')
    args = parser.parse_args()
    credentials = args.credentials.split(':')
    export(args.url, args.phn_input_file, args.output_directory, credentials[0], credentials[1], credentials[2])


if __name__ == '__main__':
    main()
