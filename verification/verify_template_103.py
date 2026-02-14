from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Construct absolute file path
        cwd = os.getcwd()
        file_path = os.path.join(cwd, 'catalog/template_103_geothermal_magmatic/index.html')
        page.goto(f'file://{file_path}')

        # Wait for fonts and content
        page.wait_for_timeout(2000)

        # Take full page screenshot
        page.screenshot(path='verification/template_103.png', full_page=True)

        browser.close()

if __name__ == '__main__':
    run()