import os
from playwright.sync_api import sync_playwright

def verify_template():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 3000}) # Tall viewport to capture more

        # Construct absolute path
        cwd = os.getcwd()
        file_path = os.path.join(cwd, 'catalog/template_137_music_tech_voltage_control/index.html')
        url = f'file://{file_path}'

        print(f"Navigating to {url}")
        page.goto(url)

        # Wait for fonts and animations to settle
        page.wait_for_timeout(3000)

        # Take a screenshot
        screenshot_path = 'template_137_verification.png'
        page.screenshot(path=screenshot_path, full_page=True)
        print(f"Screenshot saved to {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    verify_template()
