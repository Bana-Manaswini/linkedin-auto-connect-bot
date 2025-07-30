LinkedIn Auto Connect Bot is a web-based automation tool built with Streamlit and Selenium WebDriver. It automates the process of logging into LinkedIn, searching for a profile by name, and sending a connection request with a personalized message—all from a simple browser interface.

This tool simplifies repetitive networking tasks and demonstrates browser automation using Python, making it ideal for developers, learners, and recruiters (for educational purposes only).

---

## 🧠 Why This Matters

Manually sending connection requests on LinkedIn is time-consuming, especially for recruiters, marketers, or job seekers trying to build professional networks. This bot:

- 🔐 Logs into LinkedIn with provided credentials  
- 🔍 Searches and navigates to a target profile  
- 💬 Sends a connection request with a custom note  
- ⏱️ Uses Selenium waits to ensure stable interaction  
- 🧩 Falls back to manual login if CAPTCHA or 2FA appears  

It’s a practical example of combining Python scripting, automation, and a lightweight UI for real-world use.

---

## 🔧 How It Works (Under the Hood)

1. User Input via Streamlit  
   Users enter their LinkedIn email, password, target profile name, and connection message.

2. Browser Automation with Selenium
   - Launches Firefox via GeckoDriver  
   - Logs into LinkedIn  
   - Searches the specified name  
   - Opens the first matching profile  
   - Waits for and clicks “Connect” → “Add a note” → Sends the message

3. Smart Handling
   - Automatically waits for elements using WebDriverWait  
   - Detects if CAPTCHA/2FA occurs and prompts for manual login

---

## 🎯 Who Can Use This?

- 👨‍💼 Recruiters – to streamline outreach  
- 👩‍💻 Developers – to learn Selenium and automation  
- 👩‍🎓 Students – for Python and browser automation practice  
- 📢 Growth Hackers – for controlled LinkedIn engagement (educational)


