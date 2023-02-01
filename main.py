import json
from selenium import webdriver
from selenium.webdriver.common.by import By

# Open data
with open("data.json") as data:
    data = json.load(data)
    url = data["url"]
    instructions = data["instructions"]


# Connect to url
browser = webdriver.Firefox()
browser.get(url)


# Loop through instructions
for page in instructions:
    for instruction in page:
        selector = instruction["selector"]
        action = instruction["action"]

        element = browser.find_element(By.CSS_SELECTOR, selector)

        if action == "click":
            element.click()


# Close the browser window
# browser.quit()
