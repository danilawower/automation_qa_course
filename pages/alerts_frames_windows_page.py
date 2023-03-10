import random
import time

from locators.alerts_frames_windows_locators import BrowserWindowsPageLocators, AlertPageLocators, FramesPageLocators, \
    NestedFramesPageLocators, ModalWindowsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators

    def check_opened_new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])  # переключаемся на окно второе(по индексу 1)
        text_title = self.element_is_present(self.locators.TITLE_TEXT).text
        return text_title

    def check_opened_new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.TITLE_TEXT).text
        return text_title


class AlertPage(BasePage):
    locators = AlertPageLocators

    def check_see_alert(self):
        self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert  # переключение на алерт
        return alert_window.text

    def check_alert_appear_5_sec(self):
        self.element_is_visible(self.locators.APPEAR_ALERT_5_SEC_BUTTON).click()
        time.sleep(6)
        alert_window = self.driver.switch_to.alert  # переключение на алерт
        return alert_window.text

    def check_confirm_alert(self):
        self.element_is_visible(self.locators.CONFIRM_BOX_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.accept()  # нажать на ОК в алерте
        text_result = self.element_is_present(self.locators.CONFIRM_RESULT).text
        return text_result

    def check_alert_prompt(self):
        text = f'Test{random.randint(0, 100)}'
        self.element_is_visible(self.locators.PROMT_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(text)  # отправить текст внутрь алерта
        alert_window.accept()
        text_result = self.element_is_present(self.locators.PROMT_RESULT).text
        return text, text_result


class FramesPage(BasePage):
    locators = FramesPageLocators

    def check_frame(self, frame_num):  # нумерация фрейма. там их два
        if frame_num == 'frame1':
            frame = self.element_is_present(self.locators.FIRST_FRAME)  # обозначил элемент, с которым буду работать
            width = frame.get_attribute('width')  # получаю с него нужные параметры
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)  # переключаемся на фрейм и указываем на какой
            text = self.element_is_present(self.locators.TITLE_NAME).text
            self.driver.switch_to.default_content()  # переключаемся с фрейма на начальную страницу
            return [text, width, height]
        if frame_num == 'frame2':
            frame = self.element_is_present(self.locators.SECOND_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.TITLE_NAME).text
            return [text, width, height]


class NestedFramesPage(BasePage):
    locators = NestedFramesPageLocators

    def check_nested_frame(self):
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.driver.switch_to.frame(parent_frame)
        parent_text = self.element_is_present(self.locators.PARENT_FRAME_TEXT).text
        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.driver.switch_to.frame(child_frame)  # внутри родительского фрейма на дефолт окно переключатся не нужно
        child_text = self.element_is_present(self.locators.CHILD_FRAME_TEXT).text
        return parent_text, child_text


class ModalWindowsPage(BasePage):
    locators = ModalWindowsPageLocators

    def check_modal_dialogs(self):
        self.element_is_visible(self.locators.SMALL_MODAL_BUTTON).click()
        title_small = self.element_is_visible(self.locators.SMALL_BUTTON_TITLE).text
        body_small_text = self.element_is_visible(self.locators.SMALL_BUTTON_BODY).text
        self.element_is_visible(self.locators.SMALL_MODAL_CLOSE_BUTTON).click()
        self.element_is_visible(self.locators.LARGE_MODAL_BUTTON).click()
        title_large = self.element_is_visible(self.locators.LARGE_BUTTON_TITLE).text
        body_large_text = self.element_is_visible(self.locators.LARGE_BUTTON_BODY).text
        self.element_is_visible(self.locators.LARGE_MODAL_CLOSE_BUTTON).click()
        return [title_small, len(body_small_text)], [title_large, len(body_large_text)] #текст большой, по этому выведем его кол-во символов
