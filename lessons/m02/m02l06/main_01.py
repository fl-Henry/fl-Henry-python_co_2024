from webdriver_manager.chrome import ChromeDriverManager

driver_path = ChromeDriverManager().install()
print(f'ChromeDriver установлен в: {driver_path}')