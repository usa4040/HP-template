from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Construct absolute file path
        cwd = os.getcwd()
        file_path = f"file://{cwd}/catalog/template_083_martial_arts_disciplined/index.html"

        print(f"Navigating to {file_path}")
        page.goto(file_path)

        # Wait for fonts and animations
        page.wait_for_timeout(2000)

        # Take screenshot of the Hero section
        page.screenshot(path="template_083_verification.png", full_page=True)
        print("Screenshot saved to template_083_verification.png")

        browser.close()

if __name__ == "__main__":
    run()
