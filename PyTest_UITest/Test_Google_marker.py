@pytest.mark.smoke
def test_open_JavaScript_url():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://the-internet.herokuapp.com/javascript_alerts')
    driver.maximize_window()
    title = "The Internet"
    assert title == driver.title