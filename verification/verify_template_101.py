import os
from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1920, 'height': 1080})

        # Get absolute path to the file
        cwd = os.getcwd()
        file_path = os.path.join(cwd, 'catalog/template_101_horology_chronometric/index.html')
        url = f'file://{file_path}'

        print(f"Navigating to {url}")
        page.goto(url)

        # Wait for fonts and images (rough estimation)
        page.wait_for_timeout(2000)

        # Scroll down to trigger animations
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_timeout(1000)
        page.evaluate("window.scrollTo(0, 0)")
        page.wait_for_timeout(1000)

        # Screenshot Hero
        page.screenshot(path='verification/template_101_hero.png')

        # Scroll to Caliber section and screenshot
        caliber_section = page.locator('#caliber')
        caliber_section.scroll_into_view_if_needed()
        page.wait_for_timeout(1000) # Wait for reveal
        page.screenshot(path='verification/template_101_caliber.png')

        # Full page screenshot
        page.screenshot(path='verification/template_101_full.png', full_page=True)

        browser.close()

if __name__ == "__main__":
    run()
