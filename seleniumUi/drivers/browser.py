from selenium import webdriver
import pathlib

current_dir = pathlib.Path(__file__).parent.absolute()


class Browser:
    @staticmethod
    def get_chrome_driver():
        return webdriver.Chrome(executable_path=f"{current_dir}/chromedriver.exe")