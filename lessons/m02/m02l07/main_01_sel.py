import csv
import time

from selenium.webdriver.common.by import By

from selenium_lib import Initializer


def save_to_csv(data, filename: str):
    if not data:
        print("No data available to save.")
        return

    try:
        keys = data[0].keys()
        with open(filename, 'w', newline='', encoding='utf-8') as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)

        print(f"Data successfully saved to {filename}")

    except IOError as io_err:
        print(f"File I/O error occurred: {io_err}")

    except Exception as e:
        print(f"Error while saving data to CSV: {e}")
        raise e


driver = Initializer('firefox', False).init()

url = 'https://rfspager.app/pager'
driver.get(url)

header_css = 'table.table-auto thead th'
rows_css = 'table.table-auto tbody tr'

headers = [header.text.strip() for header in driver.find_elements(By.CSS_SELECTOR, header_css)]

table_data = []
for row in driver.find_elements(By.CSS_SELECTOR, rows_css):
    cells = row.find_elements(By.TAG_NAME, 'td')
    if cells:
        table_data.append({headers[i]: cell.text.strip() for i, cell in enumerate(cells)})

    last_cell = row.find_element(By.TAG_NAME, 'th')
    table_data[-1].update({headers[-1]: last_cell.text.strip()})

driver.quit()

output_file = 'output_sel.csv'
save_to_csv(table_data, output_file)
