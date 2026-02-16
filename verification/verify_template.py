import os
from playwright.sync_api import sync_playwright

def verify_template():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1920, 'height': 1080})

        # Absolute path to the file
        file_path = os.path.abspath("catalog/template_120_type_foundry_neo_grotesque/index.html")
        page.goto(f"file://{file_path}")

        # Wait for content to load (Tailwind CDN might take a moment)
        page.wait_for_timeout(2000)

        # Screenshot Hero
        page.screenshot(path="verification/hero.png")
        print("Hero screenshot taken.")

        # Scroll to Tester
        page.locator("#tester").scroll_into_view_if_needed()
        page.wait_for_timeout(500)
        page.screenshot(path="verification/tester.png")
        print("Tester screenshot taken.")

        # Scroll to Glyphs
        page.locator("#glyphs").scroll_into_view_if_needed()
        page.wait_for_timeout(500)
        page.screenshot(path="verification/glyphs.png")
        print("Glyphs screenshot taken.")

        # Scroll to Pricing
        page.locator("#pricing").scroll_into_view_if_needed()
        page.wait_for_timeout(500)
        page.screenshot(path="verification/pricing.png")
        print("Pricing screenshot taken.")

        browser.close()

if __name__ == "__main__":
    verify_template()
