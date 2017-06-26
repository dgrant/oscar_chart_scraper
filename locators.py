from selenium.webdriver.common.by import By


class SearchPageLocators(object):
    SELECT_SEARCH_MODE = (By.CSS_SELECTOR, 'select[name="search_mode"]')
    KEYWORD_INPUT = (By.CSS_SELECTOR, 'input[name="keyword"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'input[type="SUBMIT"]')
    ENCOUNTER_BUTTON = (By.CLASS_NAME, 'encounterBtn')


class SignInPageLocators(object):
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, 'input[value="Sign in"]')
    USER_NAME_FIELD = (By.CSS_SELECTOR, 'input[name="username"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[name="password"]')
    SECOND_PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[name="pin"]')


class ApointmentPageLocators(object):
    DESIRED_DATE_FOR_INIT = (By.XPATH, 'dateAppointment')
    FIRST_ENCOUNTER_LINK = (By.CLASS_NAME, 'encounterBtn')


class EncounterPageLocators(object):
    PRINT_BUTTON = (By.ID, "imgPrintEncounter")
    PRINT_ALL_RADIO_BUTTON = (By.ID, "printopAll")
    PRINT_CPP_BUTTON = (By.ID, "imgPrintCPP")
    PRINT_RX_BUTTON = (By.ID, "imgPrintRx")
    PRINT_LABS_BUTTON = (By.ID, "imgPrintLabs")
    PRINT_GO_BUTTON = (By.ID, "printOp")


class DocumentsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    BUTTON_GET_THIS_LOAN = (By.CLASS_NAME, "buttonEmphasis")
    RADIO_BUTTON_1_YEAR_LOAN = (By.CLASS_NAME, "gwt-RadioButton")


class PreventionsPageLocators(object):
    SECTION_VERIFY_IDENTITY = (By.CLASS_NAME, "verifyIdentitySection")


class AllergiesPageLocators(object):
    pass


class FormsPageLocators(object):
    pass