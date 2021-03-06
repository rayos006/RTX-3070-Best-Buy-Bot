from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import info

# make sure this path is correct
PATH = "../chromedriver"

driver = webdriver.Chrome(PATH)

TEST = True

RTX3070LINK1 = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442"
XBOXHEADSET = "https://www.bestbuy.com/site/microsoft-xbox-wireless-headset-for-xbox-series-xs-xbox-one-and-windows-10-black/6453204.p?skuId=6453204"
XBOXREMOTE = "https://www.bestbuy.com/site/microsoft-xbox-elite-wireless-controller-series-2-for-xbox-one-xbox-series-x-and-xbox-series-s-black/6352703.p?skuId=6352703"

driver.get(XBOXREMOTE)

isComplete = False

while not isComplete:
    # find add to cart button
    try:
        atcBtn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".add-to-cart-button"))
        )
    except:
        driver.refresh()
        continue

    print("Add to cart button found")

    try:
        # add to cart
        atcBtn.click()

        # go to cart and begin checkout as guest
        driver.get("https://www.bestbuy.com/cart")

        checkoutBtn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="cartApp"]/div[2]/div[1]/div/div[1]/div[1]/section[2]/div/div/div[3]/div/div[1]/button'))
        )
        checkoutBtn.click()
        print("Successfully added to cart - beginning check out")

        # fill in email and password
        emailField = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "fld-e"))
        )
        emailField.send_keys(info.email)

        pwField = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "fld-p1"))
        )
        pwField.send_keys(info.password)

        # click sign in button
        signInBtn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/section/main/div[1]/div/div/div/div/form/div[3]/button"))
        )
        signInBtn.click()
        print("Signing in")

        # fill in card cvv
        cvvField = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "credit-card-cvv"))
        )
        cvvField.send_keys(info.cvv)
        print("Attempting to place order")

        if not TEST:
            # place order
            placeOrderBtn = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".button__fast-track"))
            )
            placeOrderBtn.click()

        isComplete = True
    except:
        # make sure this link is the same as the link passed to driver.get() before looping
        driver.get(XBOXREMOTE)
        print("Error - restarting bot")
        continue

print("Order successfully placed")



