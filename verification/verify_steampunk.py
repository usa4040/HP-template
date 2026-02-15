from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Construct absolute path to the file
        file_path = os.path.abspath("catalog/template_111_escape_room_steampunk/index.html")
        url = f"file://{file_path}"

        print(f"Navigating to {url}")
        page.goto(url)

        # Wait for fonts and content to load
        page.wait_for_load_state("networkidle")

        # Take a full page screenshot
        page.screenshot(path="verification/steampunk_full.png", full_page=True)

        # Take a screenshot of the Hero section specifically
        hero = page.locator("section").first
        hero.screenshot(path="verification/steampunk_hero.png")

        print("Screenshots taken.")
        browser.close()

if __name__ == "__main__":
    run()
