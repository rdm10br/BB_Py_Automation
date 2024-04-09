from playwright.sync_api import sync_playwright

def get_excel_cell_text(url, sheet_selector, cell_selector):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)

        # Wait for the Excel sheet to load, adjust the selector as needed
        page.wait_for_selector(sheet_selector)

        # Get the text content of the Excel cell
        cell_text = page.text_content(cell_selector)

        browser.close()

    return cell_text

# Example usage
excel_url = "your_excel_web_app_url"
sheet_selector = ".your-sheet-selector"  # Replace with the actual selector for your Excel sheet
cell_selector = ".your-cell-selector"    # Replace with the actual selector for your Excel cell

result = get_excel_cell_text(excel_url, sheet_selector, cell_selector)
print("Excel Cell Text:", result)