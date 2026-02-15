import os
from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Get absolute path to the file
        file_path = os.path.abspath("catalog/template_118_geospatial_topographic/index.html")
        page.goto(f"file://{file_path}")

        # Wait for content to load
        page.wait_for_selector("body")

        # Verify Title
        title = page.title()
        print(f"Page Title: {title}")
        assert "Geospatial Intelligence" in title

        # Verify Hero Text
        hero_text = page.locator("h1").inner_text()
        print(f"Hero Text: {hero_text}")
        assert "MAPPING THE" in hero_text

        # Verify Stats
        stats = page.locator("text=Coverage")
        assert stats.is_visible()

        # Verify Services
        services = page.locator("#services")
        assert services.is_visible()

        # Screenshot
        page.screenshot(path="template_118_verification.png", full_page=True)
        print("Verification successful. Screenshot saved to template_118_verification.png")

        browser.close()

if __name__ == "__main__":
    run()
