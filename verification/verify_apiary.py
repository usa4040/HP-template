from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1280, "height": 800})

        # specific to this environment
        filepath = os.path.abspath("catalog/template_104_apiary_golden_hex/index.html")
        page.goto(f"file://{filepath}")

        # Wait for fonts and content
        page.wait_for_timeout(1000)

        # Take screenshot
        page.screenshot(path="verification/template_104_verification.png", full_page=True)

        browser.close()

if __name__ == "__main__":
    run()