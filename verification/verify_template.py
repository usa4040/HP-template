from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Absolute path to the file
        file_path = os.path.abspath("catalog/template_045_senior_care_compassionate/index.html")
        page.goto(f"file://{file_path}")

        # Wait for the page to load (checking for a key element)
        page.wait_for_selector("h1")

        # Take a screenshot
        page.screenshot(path="verification/template_045_screenshot.png", full_page=True)

        browser.close()

if __name__ == "__main__":
    run()
