import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
import time

# Streamlit UI
st.title("LinkedIn Auto Login & Messaging")

email = st.text_input("Enter your LinkedIn Email")
password = st.text_input("Enter your LinkedIn Password", type="password")
search_name = st.text_input("Enter LinkedIn profile name to search")
default_message = st.text_area("Enter the message to send", "Hi, I'd like to connect with you!")

if st.button("Login and Send Message"):
    if email and password and search_name and default_message:
        try:
            # Browser setup
            options = Options()
            options.headless = False  # Set to True for headless mode
            service = Service(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service, options=options)
            wait = WebDriverWait(driver, 15)

            # Step 1: Login to LinkedIn
            driver.get("https://www.linkedin.com/login")
            wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys(email)
            driver.find_element(By.ID, "password").send_keys(password, Keys.RETURN)
            wait.until(lambda d: "feed" in d.current_url or "checkpoint" in d.current_url)
            current_url = driver.current_url

            if "checkpoint" in current_url:
                st.warning("Manual verification required. Please complete CAPTCHA or 2FA.")
                driver.quit()
                driver = webdriver.Firefox(service=service, options=options)
                driver.get("https://www.linkedin.com/login")
                st.info("A browser has been opened. Please log in manually.")

            elif "feed" in current_url:
                st.success("Successfully logged in!")

                # Step 2: Search for the profile
                search_url = f"https://www.linkedin.com/search/results/people/?keywords={search_name}"
                driver.get(search_url)
                time.sleep(3)

                # Wait and click first profile result using reliable XPath
                wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/in/')]")))
                profile_link = driver.find_element(By.XPATH, "//a[contains(@href, '/in/')]")
                profile_url = profile_link.get_attribute("href")
                driver.get(profile_url)

                # Step 3: Wait for "Add a note" popup
                try:
                    st.info("Please click the 'Connect' button manually in the browser. The app will take over when 'Add a note' appears.")

                    with st.spinner('Waiting for "Add a note" popup...'):
                        add_note_button = WebDriverWait(driver, 60).until(
                            EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Add a note')]"))
                        )
                        add_note_button.click()

                    with st.spinner('Adding note and sending connection request...'):
                        note_textarea = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, "//textarea[@name='message']"))
                        )
                        note_textarea.clear()
                        note_textarea.send_keys(default_message)

                        send_now_button = WebDriverWait(driver, 10).until(
                            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Send now']"))
                        )
                        send_now_button.click()

                    st.success("Connection request with note sent successfully!")

                except Exception as conn_err:
                    st.error("Could not detect 'Add a note' popup or send message. Maybe already connected?")
                    st.info(f"Profile URL: {profile_url}")

            else:
                st.error("Login failed. Please check your credentials.")

        except Exception as e:
            st.error(f"An error occurred: {e}")

    else:
        st.warning("Please fill in all required fields.")