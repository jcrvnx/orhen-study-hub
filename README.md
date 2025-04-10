# ✨ ORHEN STUDY HUB ✨

<p align="center">
  <img src="PLACEHOLDER_ICON_OR_LOGO_URL" alt="Orhen Study Hub Logo" width="150"/>
</p>

<p align="center">
  <strong>Your Centralized GUI Hub for Linux Study & Tools 🐧</strong>
  <br>
  Built with Python & CustomTkinter for a modern experience.
</p>

<p align="center">
  <!-- Optional: Add Shields.io Badges here -->
  <!-- Example: <img src="https://img.shields.io/badge/python-3.8%2B-blue" alt="Python Version"> -->
  <!-- Example: <img src="https://img.shields.io/badge/platform-Linux-lightgrey" alt="Platform"> -->
  <!-- Example: <img src="https://img.shields.io/badge/license-MIT-green" alt="License"> -->
</p>

---

**Tired of juggling multiple windows and terminals for your study sessions, development tasks, or security engagements?** ORHEN STUDY HUB provides a sleek, customizable Graphical User Interface (GUI) to quickly access your essential browsers, utilities, and Linux tools – all in one place!

Designed specifically for **Linux distributions** (like Kali, Ubuntu, Fedora, etc.), this hub leverages the modern `customtkinter` library to offer a clean look that feels right at home on your desktop. It's built for organization, helping you streamline your workflow whether you're learning, coding, or conducting **organized security studies and tasks**.

*(This is **not** just another terminal theme - it's a functional GUI application!)*

---

## 🚀 Features

*   **✨ Modern GUI:** Clean and intuitive interface built with `customtkinter`.
*   **🏡 Centralized Dashboard:** Quick launchers for your favorite:
    *   Web Browsers (Chrome, Firefox, Vivaldi, Chromium)
    *   Utilities (Text Editor, Terminal, Wavemon)
*   **🔧 Tools Access:** A dedicated section with launchers for common Linux tools (easily customizable!). Perfect for development, system administration, or security tasks.
    *   *Note: Features a curated list - you can easily add your own!*
*   **🎨 Appearance Settings:** Customize the look and feel:
    *   Light / Dark / System Theme modes.
    *   Selectable Color Themes (Blue, Green, Dark-Blue).
*   **🍔 Collapsible Sidebar:** Maximize your workspace with an easy-to-toggle navigation menu.
*   **🐧 Linux Focused:** Designed and tested for Linux environments.
*   **🖱️ One-Click Launch:** Open applications instantly without hunting through menus or typing commands.

---

## 🎬 Demo / Screenshots

*(Seeing is believing! Add a GIF or screenshots here to showcase the Hub in action.)*

<!--
Recommended:
1. A GIF showing the main dashboard and clicking a launcher.
2. A GIF showing the sidebar collapsing/expanding and navigating between sections.
3. A screenshot of the Tools section.
4. A screenshot of the Settings section.
-->

<p align="center">
  <!-- Add your GIF or Screenshot here -->
  <!-- Example: <img src="URL_TO_YOUR_DEMO_GIF.gif" alt="Orhen Study Hub Demo"> -->
  *<center>(Placeholder: Add a captivating GIF demonstrating the HUB!)</center>*
</p>

<p align="center">
  <!-- Add more screenshots if desired -->
  <!-- Example: <img src="URL_TO_YOUR_SCREENSHOT_1.png" width="48%" alt="Dashboard Screenshot"> -->
  <!-- Example: <img src="URL_TO_YOUR_SCREENSHOT_2.png" width="48%" alt="Tools Screenshot"> -->
  *<center>(Placeholder: Add screenshots of Dashboard/Tools/Settings)</center>*
</p>

---

## 🛠️ Installation & Setup

Follow these steps to get ORHEN STUDY HUB running on your Linux system:

1.  **Prerequisites:**
    *   **Python 3:** Ensure you have Python 3.8 or newer installed. Check with `python3 --version`.
    *   **pip:** Python's package installer. Usually comes with Python. Check with `pip3 --version`.
    *   **git:** For cloning the repository. Install if needed (`sudo apt install git` or `sudo dnf install git`).
    *   **Target Applications:** Make sure the applications you want to launch (browsers, tools like `wavemon`, `nmap`, `wireshark`, your preferred text editor/terminal, etc.) are **already installed** on your system!

2.  **Clone the Repository:**
    Open your terminal and run:
    ```bash
    git clone https://github.com/jcrvnx/ORHEN-STUDY-HUB.git # <-- Replace 'ORHEN-STUDY-HUB' if your repo name is different!
    cd ORHEN-STUDY-HUB # <-- Navigate into the cloned directory
    ```

3.  **Install Dependencies:**
    Install the required Python libraries (`customtkinter` and `Pillow` for image handling):
    ```bash
    # It's highly recommended to use a virtual environment!
    # python3 -m venv venv
    # source venv/bin/activate

    pip3 install customtkinter Pillow

    # If you used a virtual environment, you can deactivate it when done:
    # deactivate
    ```
    *   **Important:** Install these packages as your **regular user**, not using `sudo`. Running the GUI as root is not recommended and might cause issues if the library wasn't installed for root.

4.  **(Potentially) Edit Tool Commands:**
    *   The script (`orhen_study_hub.py` or similar) contains hardcoded command names for launching applications (e.g., `google-chrome-stable`, `kate`, `gnome-terminal`).
    *   **You might need to edit these commands** within the Python script (look inside the `create_dashboard_frame` and `create_tools_frame` functions) to match the *exact* command names used on *your specific Linux distribution*. For example, your text editor might be `gedit` or `mousepad` instead of `kate`. Your terminal might be `konsole` or `xfce4-terminal`.

---

## ▶️ How to Run

1.  Navigate to the project directory in your terminal:
    ```bash
    cd /path/to/ORHEN-STUDY-HUB
    ```
2.  Run the main Python script:
    ```bash
    python3 orhen_study_hub.py # Or whatever you named the main script
    ```

The ORHEN STUDY HUB GUI should now launch!

---

## ⚙️ Customization

*   **Adding/Changing Launchers:** Modify the `browsers`, `utils`, and `linux_tools` dictionaries inside the `orhen_study_hub.py` script to add your own applications or change existing commands.
*   **Appearance:** Use the built-in **Settings** menu within the application to change themes and modes.

---

## ❤️ Support & Donations

If you find ORHEN STUDY HUB useful and want to support its development, consider donating! Your support helps keep the project alive and allows for future improvements.

*   ☕️ **Ko-fi:** [https://ko-fi.com/YOUR_KOFI_USERNAME](https://ko-fi.com/YOUR_KOFI_USERNAME) <!-- Replace with your link -->
*   🅿️ **PayPal:** [https://paypal.me/YOUR_PAYPAL_USERNAME](https://paypal.me/YOUR_PAYPAL_USERNAME) <!-- Replace with your link -->
*   <img src="https://img.shields.io/badge/GitHub%20Sponsors-Sponsor-ea4aaa?style=social&logo=githubsponsors" alt="GitHub Sponsors" height="20"> **GitHub Sponsors:** [https://github.com/sponsors/jcrvnx](https://github.com/sponsors/jcrvnx) <!-- Replace with your link -->
*   ₿ **Crypto (BTC):** `YOUR_BTC_ADDRESS` <!-- Replace with your address -->
*   <img src="https://img.shields.io/badge/Ethereum-Donate-blue?style=flat-square&logo=ethereum" alt="Ethereum" height="20"> **ETH:** `YOUR_ETH_ADDRESS` <!-- Replace with your address -->

*Even a small contribution is greatly appreciated!*

---

<p align="center">
  Made with ❤️ by Jcrist Orhen (jcrvnx)
</p>
