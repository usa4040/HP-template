from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Get absolute path to the file
        cwd = os.getcwd()
        file_path = os.path.join(cwd, 'catalog/template_099_bionics_neolab/index.html')
        url = f'file://{file_path}'

        print(f"Navigating to {url}")
        page.goto(url)

        # Wait for network idle to ensure fonts/images load
        page.wait_for_load_state('networkidle')

        # Check for title
        title = page.title()
        print(f"Page title: {title}")
        assert "{{COMPANY_NAME}}" in title

        # Check for Company Name placeholder
        count = page.get_by_text("{{COMPANY_NAME}}").count()
        print(f"Found {count} instances of {{COMPANY_NAME}}")
        assert count > 0

        # Take screenshot
        output_path = 'verification/template_099_verification.png'
        page.screenshot(path=output_path, full_page=True)
        print(f"Screenshot saved to {output_path}")

        browser.close()

if __name__ == "__main__":
    run()
