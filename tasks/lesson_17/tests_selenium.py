from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.support.expected_conditions import element_to_be_clickable, visibility_of_element_located
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

first_website = "http://uitestingplayground.com/home"
second_website = "http://the-internet.herokuapp.com/"
third_website = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"


class TestSuiteOne:
    def test_ajax_request(self, driver, wait):
        driver.get(first_website)

        button = driver.find_element(by='xpath', value='//a[contains(@href,"/ajax")]')
        button.click()

        result_element = driver.find_element(by='id', value='ajaxButton')
        result_element.click()

        wait.until(EC.text_to_be_present_in_element((By.ID, "content"), "Data loaded with AJAX get request."))
        element = driver.find_element(by='id', value='content')
        expected_text = "Data loaded with AJAX get request."
        assert element.text == expected_text, f"Expected text {expected_text}, but was received {element.text}"

    def test_button_color_change(self, driver, wait):
        driver.get(first_website)

        button = driver.find_element(by='xpath', value='//a[contains(@href,"/click")]')
        button.click()

        element = driver.find_element(by='id', value='badButton')
        initial_color = element.value_of_css_property('background-color')
        element.click()

        wait.until(EC.visibility_of_element_located((By.ID, 'badButton')))

        updated_color = element.value_of_css_property('background-color')

        assert initial_color != updated_color, f"Color is not changed from {initial_color} to {updated_color}"

    def test_button_name_changed(self, driver, wait):
        driver.get(first_website)

        button = driver.find_element(by='xpath', value='//a[contains(@href,"/textinput")]')
        button.click()

        element = driver.find_element(by='id', value='newButtonName')
        element.send_keys("Crazy button")

        new_button = driver.find_element(by='id', value='updatingButton')

        button_text = new_button.text
        new_button.click()

        wait.until(EC.text_to_be_present_in_element((By.ID, "updatingButton"), "Crazy button"))

        new_button_text = new_button.text

        assert button_text != new_button_text, f"The name of the button {button_text} was not changed to {new_button_text}"

    def test_authorization(self, driver, wait):
        driver.get(first_website)

        button = driver.find_element(by='xpath', value='//a[contains(@href,"/sampleapp")]')
        button.click()

        user_status = driver.find_element(by='id', value="loginstatus")
        status = user_status.text

        username_field = driver.find_element(by='name', value="UserName")
        password_field = driver.find_element(by='name', value="Password")
        submit_button = driver.find_element(by='id', value="login")

        username_field.send_keys("Marilyn Manson")
        password_field.send_keys("pwd")

        entered_username = username_field.get_attribute("value")
        submit_button.click()

        wait.until(EC.text_to_be_present_in_element((By.ID, "loginstatus"), "Welcome, Marilyn Manson!"))

        new_status = user_status.text
        assert new_status != status
        assert entered_username == "Marilyn Manson", f"The current name is not equal {entered_username}"

    def test_check_counter(self, driver, wait):
        driver.get(first_website)

        button = driver.find_element(by='xpath', value='//a[contains(@href,"/mouseover")]')
        button.click()

        click_button = driver.find_element(by='xpath', value="//a[@class='text-primary' and @title='Click me']")
        counter = driver.find_element(by='id', value="clickCount")

        count = counter.text
        actions = ActionChains(driver)
        actions.double_click(click_button).perform()

        wait.until(lambda driver: counter.text != count)

        new_count = counter.text
        expected_count = "2"
        assert new_count == expected_count, f"Counter did not change to {expected_count}. Actual count: {new_count}"


class TestSuiteTwo:
    def test_check_title(self, driver, wait):
        driver.get(second_website)

        title_element = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                     "//h1[contains(text(),"
                                                                     "'Welcome to "
                                                                     "the-internet')]")))
        assert title_element.text == "Welcome to the-internet", "Header is not found"

    def test_authorization(self, driver, wait):
        driver.get(second_website)

        link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Form "
                                                                      "Authentication')]")))
        link.click()

        auth_title_element = driver.find_element(by='xpath', value="//h2[contains(text(),'Login Page')]")
        assert auth_title_element.text == "Login Page", "Authentication page header not found"

        username_field = driver.find_element(by='xpath', value="//input[@id='username']")
        password_field = driver.find_element(by='xpath', value="//input[@id='password']")
        submit_button = driver.find_element(by='xpath', value="//button[@type='submit']")

        username_field.send_keys("tomsmith")
        password_field.send_keys("SuperSecretPassword!")

        submit_button.click()

        success_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//div["
                                                                                 "@id='flash']")))
        assert "You logged into a secure area!" in success_message.text, "No successful login message found"


class TestSuiteThree:
    def test_user_log_in(self, driver, wait):
        driver.get(third_website)

        button = wait.until(
            element_to_be_clickable((By.CSS_SELECTOR, 'button.btn.btn-primary.btn-lg[ng-click="customer()"]')))
        button.click()

        button = wait.until(element_to_be_clickable((By.ID, 'userSelect')))
        button.click()

        dropdown = driver.find_element(by="id", value="userSelect")
        select = Select(dropdown)
        select.select_by_visible_text("Neville Longbottom")

        new_button = wait.until(element_to_be_clickable(
            (By.CSS_SELECTOR, 'button.btn.btn-default[type="submit"][ng-show="custId != \'\'"]')))

        new_button.click()

        welcome_message = wait.until(visibility_of_element_located((By.CSS_SELECTOR, 'span.fontBig.ng-binding')))
        assert welcome_message.text == 'Neville Longbottom', "User login failed"

    def test_add_customer(self, driver, wait):
        driver.get(third_website)

        button = wait.until(
            element_to_be_clickable((By.CSS_SELECTOR, 'button.btn.btn-primary.btn-lg[ng-click="manager()"]')))
        button.click()

        add_button = wait.until(
            element_to_be_clickable((By.CSS_SELECTOR, 'button.btn.btn-lg.tab[ng-click="addCust()"]')))
        add_button.click()

        input_fields = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,
                                                                       'input.form-control.ng'
                                                                       '-pristine.ng-untouched.ng'
                                                                       '-invalid.ng-invalid'
                                                                       '-required')))
        first_name_field = input_fields[0]
        last_name_field = input_fields[1]
        post_code_field = input_fields[2]

        first_name_field.send_keys("Valeriia")
        last_name_field.send_keys("Tyshchenko")
        post_code_field.send_keys("03134")

        add_button = wait.until(
            element_to_be_clickable((By.CSS_SELECTOR, 'button.btn.btn-default[type="submit"][value=""] ')))
        add_button.click()
        alert = wait.until(EC.alert_is_present())
        message = alert.text
        assert "Customer added successfully with customer id" in message, "Failed to create account successfully."
        alert.accept()

    def test_open_account(self, driver, wait):
        driver.get(third_website)

        bank_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                             'button.btn.btn-primary.btn-lg[ng-click="manager()"]')))
        bank_button.click()

        open_account_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn.btn-lg.tab['
                                                         'ng-click="openAccount()"]')))
        open_account_button.click()

        customer_field = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'select[name="userSelect"]')))
        customer_field.click()

        option_element = wait.until(
            EC.presence_of_element_located((By.XPATH, '//option[@value="4" and contains(text(), '
                                                      '"Albus Dumbledore")]')))
        option_element.click()

        select_currency = wait.until(EC.presence_of_element_located((By.ID, "currency")))
        select_currency.click()

        currency = wait.until(
            EC.presence_of_element_located((By.XPATH, '//option[@value="Dollar"]')))
        currency.click()

        process_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//button[@type="submit" and @value=""]')))
        process_button.click()
        alert = wait.until(EC.alert_is_present())
        message = alert.text
        assert 'Account created successfully with account Number' in message, \
            "Failed to create account successfully."
        alert.accept()

    def test_search_customer(self, driver, wait):
        driver.get(third_website)

        bank_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn.btn-primary.btn-lg[ng-click="manager()"]')))
        bank_button.click()

        customers_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn.btn-lg.tab[ng-click="showCust()"]')))
        customers_button.click()

        search_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                              'input.form-control.ng-pristine.ng-untouched.ng-valid['
                                                              'placeholder="Search Customer"]['
                                                              'ng-model="searchCustomer"]')))
        customer_name = "Ron"
        search_field.send_keys(customer_name)

        customer_name_element = wait.until(
            EC.presence_of_element_located((By.XPATH, f'//tr//td[text()="{customer_name}"]')))
        assert customer_name_element.text == customer_name, f"Name {customer_name} not found in the table"
