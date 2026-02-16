from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 3000}) # Large height to capture most sections

        # Absolute path to the file
        file_path = os.path.abspath("catalog/template_125_cryotherapy_sub_zero/index.html")
        page.goto(f"file://{file_path}")

        # Verify title
        title = page.title()
        print(f"Page Title: {title}")

        # Verify Hero Text
        hero_text = page.locator("h1").inner_text()
        print(f"Hero Text: {hero_text}")

        if "SUBZERO" in hero_text:
            print("Hero section verified.")
        else:
            print("Hero section missing or incorrect.")

        # Take screenshot
        screenshot_path = "verification/template_125_verification.png"
        page.screenshot(path=screenshot_path, full_page=True)
        print(f"Screenshot saved to {screenshot_path}")

        browser.close()

if __name__ == "__main__":
    run()