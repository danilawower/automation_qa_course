import time

from pages.marshal_page import PersonalAccountPage, RegistrationPage, ChangePersonalInformationPage, \
    ProductCatalogPage, MenuHoverOverPage, CornerMenuPage, CarDropDownPage, ProductCatalogNewTabPage, VinSearchPage, \
    MainBannerPage


class TestLogin:

    def test_login(self, driver):
        registration_page = RegistrationPage(driver, 'https://marshal.ru/')
        registration_page.open()
        button = registration_page.check_registration()
        assert button == 'Выход'


class TestPersonalAccount:

    def test_personal_account(self, driver):
        account_page = PersonalAccountPage(driver, "https://marshal.ru/")
        account_page.open()
        result = account_page.check_login()
        assert result == 'Выход'


class TestChangePersonalInformation:

    def test_change_personal(self, driver):
        change_info = ChangePersonalInformationPage(driver, "https://marshal.ru/")
        change_info.open()
        old, changed = change_info.check_change_personal_info()
        assert old != changed


class TestProductCatalog:

    def test_product_catalog(self, driver):
        product_catalog = ProductCatalogPage(driver, 'https://marshal.ru/')
        product_catalog.open()
        product_catalog.check_product_catalog()
        time.sleep(5)


class TestMenuHoverOver:

    def test_hover_over(self, driver):
        menu_over_hover = MenuHoverOverPage(driver, 'https://marshal.ru/')
        menu_over_hover.open()
        result = menu_over_hover.check_dropdown()
        assert str(result)


class TestCornerMenu:

    def test_corner_menu(self, driver):
        corner_menu = CornerMenuPage(driver, 'https://marshal.ru/')
        corner_menu.open()
        corner_menu.check_corner_menu()


class TestCarDropdown:

    def test_car_dropdown(self, driver):
        car_dropdown = CarDropDownPage(driver, 'https://marshal.ru/')
        car_dropdown.open()
        header, car_mark = car_dropdown.check_dropdown_car_auto_choice()
        assert car_mark in header

    def test_car_dropdown_handtype(self, driver):
        car_dropdown = CarDropDownPage(driver, 'https://marshal.ru/')
        car_dropdown.open()
        car_mark, header = car_dropdown.check_dropdown_car_type_choice()
        assert car_mark in header


class TestProductCatalogNewTab:

    def test_product_catalog_new_tab(self, driver):
        product_catalog = ProductCatalogNewTabPage(driver, "https://marshal.ru/")
        product_catalog.open()
        text1, text2, text3, text4, text5 = product_catalog.check_product_catalog_new_tab()
        assert len(text1) > 0
        assert len(text2) > 0
        assert len(text3) > 0
        assert len(text4) > 0
        assert len(text5) > 0


class TestVinSearch:

    def test_vin_search(self, driver):
        vin_search = VinSearchPage(driver, 'https://marshal.ru/')
        vin_search.open()
        result = vin_search.check_vin_search()
        print(result)



class TestMainBanner:

    def test_main_banner(self, driver):
        main_banner = MainBannerPage(driver, "https://marshal.ru/")
        main_banner.open()
        text = main_banner.check_main_banner()
        assert str(text)





