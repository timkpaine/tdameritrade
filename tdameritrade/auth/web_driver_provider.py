class WebDriverProvider:

    @staticmethod
    def get_web_driver(use_headless_web_driver=True):
        from selenium import webdriver
        from webdriver_manager.chrome import ChromeDriverManager

        chrome_driver_binary_path = ChromeDriverManager().install()

        chrome_options = webdriver.ChromeOptions()

        if use_headless_web_driver:
            chrome_options.add_argument('--headless')
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument("--window-size=1920, 1200")

        return webdriver.Chrome(chrome_driver_binary_path, chrome_options=chrome_options)
