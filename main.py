import json
from selenium import webdriver
from selenium.webdriver.common.by import By


def do_instructions(instructions):
    for page in instructions:
        for instruction in page:
            selector = instruction["selector"]
            action = instruction["action"]

            element = browser.find_element(By.CSS_SELECTOR, selector)

            if action == "click":
                element.click()
            elif action == "write":
                element.send_keys(instruction["value"])


# Open data
with open("data.json") as data:
    data = json.load(data)
    url = data["url"]
    repetitions = data["repetitions"]
    instructions = data["instructions"]


# Repeat instructions
for _ in range(repetitions):
    browser = webdriver.Firefox()  # Open new browser window
    browser.get(url)  # Open url
    do_instructions(instructions)  # Do instructions
    # browser.quit()  # Close browser window
