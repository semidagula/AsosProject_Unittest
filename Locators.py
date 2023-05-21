from selenium.webdriver.common.by import By

LOGIN_BUTTON = (By.XPATH, '//*[@title="Logare"]')
ADRESA_EMAIL = (By.XPATH, '//*[@id="email"]')
PAROLA = (By.XPATH, '//*[@id="pass"]')
LOGGARE_BTN = (By.XPATH, "//*[@title='Logare']")
LOGARE_BTN = (By.XPATH,"//span[contains(text(),'Logare')]")
EMAIL_ERROR_MESSAGE = (By.CSS_SELECTOR, "#advice-validate-email-email")
ERROR_LOGIN = (By.XPATH, "//div[@id='advice-validate-password-pass']")
LOGO_HOME_PAGE = (By.CSS_SELECTOR, "img[alt='Shine Boutique']")
SEARCH_BAR = (By.CSS_SELECTOR, "#search")

MARIMEA = (By.XPATH, "//span[@class='swatch-label']")

ERROARE_CAUTARE = (By.XPATH, "//p[@class='note-msg']")
SEARCHING_BTN = (By.XPATH, "//button[@title='Căutare']//i[@class='icon-search']")

MOCASINI = (By.XPATH, "//img[@id='product-collection-image-49320']")
PRET = (By.XPATH,"//span[@id='product-price-49320']//span[@class='price'][normalize-space()='229,00 RON']")

PRODUCT_ITEMS = (By.CLASS_NAME, "category-products")
MARIMEA_UNI = (By.ID, "swatch59")
ADAUGARE_IN_COS = (By.CSS_SELECTOR, "button[title='Adăugare în Coș'] span span")
GEANTA = (By.XPATH, "//img[@id='product-collection-image-23795']")
SUCCES_MSG_GEANTA = (By.XPATH,"//span[contains(text(),'GEANTĂ PIELE ECO CU PRINT SNAKE MARO IT-GNT02Y a f')]")




EMPTY_CART_MSG =(By.XPATH, "//h1[contains(text(),'Coșul de Cumpărături este Gol')]")


ASOS_LOGO = (By.XPATH, '//*[@id="chrome-sticky-header"]/div[1]/div/div/a')
MY_CART = (By.XPATH, "/html/body/div[1]/div/div[2]/header/div[3]/div/div[1]/div/ul/li[3]/div/div/div/div/div/div/div/div[1]")
CART =(By.CLASS_NAME, '_1z5n7CN')
cart=(By.XPATH, "/html/body/div[1]/div/div[2]/header/div[3]/div/div[1]/div/ul/li[3]/a")
ADD_TO_BAG = (By.ID, "product-add-button")

VALENTINO_BAG = (By.ID, "pta-product-203141503-0")
SEARCH = (By.XPATH, '//*[@id="chrome-search"]')
LIST = (By.CLASS_NAME, 'productTitle_U0cIN')
BTN = (By.CLASS_NAME, 'kH5PAAC')
ACCEPT_COOCKIES = (By.ID, "onetrust-accept-btn-handler")
COOCKIES_BANNER   = (By.XPATH, '//*[@id="onetrust-banner-sdk"]')
VIEW_BAG = (By.XPATH, '//*[@id="minibag-dropdown"]/div/div/div/div[3]/div/div[3]/div[1]')
REMOVE_CART= (By.XPATH, '//*[@id="asos-web-bag-react"]/div[1]/div[2]/div[1]/div[1]/div[3]/ul/li/bag-item-list/ul/li/div/div/div/bag-remove/div/button')
MSG_ERROR = (By.XPATH, "//span[@id='Password-error']")

LISTA_DRESSES = (By.XPATH, "//div[@class='resultsView_HpeNk']")

SIGN_IN = (By.XPATH, "//span[@type='accountUnfilled']")
SIGN_IN_ACC= (By.XPATH, "//a[normalize-space()='Sign In']")
MY_ACCOUNT = (By.XPATH,"//a[normalize-space()='My Account']")
EMAIL = (By.XPATH, "//input[@id='EmailAddress']")
PASSWORD = (By.XPATH, "//input[@id='Password']")
I_AM_NOT_A_ROBOT = (By.XPATH, "//input[@id='Password']")
SAVED_LIST = (By.XPATH, "//span[@type='heartUnfilled']")
FACEBOOK_LINK = (By.XPATH, "//a[@href='https://www.facebook.com/ASOS/']")