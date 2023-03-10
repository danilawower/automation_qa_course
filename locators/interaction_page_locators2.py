from selenium.webdriver.common.by import By


class SortablePageLocators:
    LIST_TAB = (By.XPATH, "//a[@id='demo-tab-list']")
    LIST_ELEMENTS = (By.XPATH, "//div[@class='vertical-list-container mt-4']//div[@class = 'list-group-item list-group-item-action']")
    GRID_TAB = (By.XPATH, "//a[@id='demo-tab-grid']")
    GRID_ELEMENTS = (By.XPATH, "//div[@class='create-grid']//div[@class = 'list-group-item list-group-item-action']")


class SelectablePageLocators:
    LIST_ELEMENTS = (By.XPATH, "//li[@class = 'mt-2 list-group-item list-group-item-action']")
    LIST_TAB = (By.XPATH, "//a[@id='demo-tab-list']")
    GRID_TAB = (By.XPATH, "//a[@id='demo-tab-grid']")
    GIRD_ELEMENTS = (By.XPATH, "//li[@class='list-group-item list-group-item-action']")
    LIST_ELEMENTS_ACTIVE = (By.XPATH, "//li[@class = 'mt-2 list-group-item active list-group-item-action']")
    GRID_ELEMENTS_ACTIVE = (By.XPATH, "//li[@class='list-group-item active list-group-item-action']")


class ResizablePageLocators:
    RESIZABLE_BOX = (By.XPATH, "//div[@id='resizableBoxWithRestriction']")
    RESIZABLE_BOX_HANDLE = (By.XPATH, "//div[@id='resizableBoxWithRestriction']//span[@class='react-resizable-handle react-resizable-handle-se']")


class DroppableLocators:
    DRAG_ME = (By.XPATH, "//div[@id='draggable']")
    DROP_HERE = (By.XPATH, "//div[@id='simpleDropContainer']//div[@id='droppable']")

    ACCEPT_BUTTON = (By.XPATH, "//a[@id='droppableExample-tab-accept']")
    ACCEPTABLE = (By.XPATH, "//div[@id='acceptable']")
    NOT_ACCEPTABLE = (By.XPATH, "//div[@id='notAcceptable']")
    DROP_HERE_ACCEPT = (By.XPATH, "//div[@id='acceptDropContainer']//div[@id='droppable']")


