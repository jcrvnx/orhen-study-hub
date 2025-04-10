import tkinter
import tkinter.messagebox
import customtkinter
import subprocess
import os
import platform

# --- Appearance Settings ---
customtkinter.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

# --- Main Application Class ---
class OrhenStudyHub(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # --- Basic Window Configuration ---
        self.title("Orhen Study Hub")
        self.geometry("1100x700") # Initial size

        # --- Check OS ---
        if platform.system() != "Linux":
            tkinter.messagebox.showerror("Compatibility Error", "Orhen Study Hub is designed for Linux systems only.")
            self.destroy() # Close the app if not on Linux
            return

        # --- Main Layout (Grid: 1 row, 2 columns - Sidebar | Content) ---
        self.grid_rowconfigure(0, weight=1) # Content row expands vertically
        self.grid_columnconfigure(1, weight=1) # Content column expands horizontally

        # --- Navigation Frame (Sidebar) ---
        self.navbar_frame = customtkinter.CTkFrame(self, width=200, corner_radius=0)
        self.navbar_frame.grid(row=0, column=0, sticky="nsew")
        self.navbar_frame.grid_rowconfigure(4, weight=1) # Push elements towards top

        # --- Navbar Header ---
        self.navbar_header_frame = customtkinter.CTkFrame(self.navbar_frame, height=50, corner_radius=0, fg_color="transparent")
        self.navbar_header_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=(10, 10))
        self.navbar_header_frame.grid_columnconfigure(1, weight=1)

        self.hamburger_button = customtkinter.CTkButton(self.navbar_header_frame, text="☰", width=30,
                                                        command=self.toggle_navbar)
        self.hamburger_button.grid(row=0, column=0, padx=(0, 10), pady=5)
        self.navbar_label = customtkinter.CTkLabel(self.navbar_header_frame, text="Menu",
                                                    font=customtkinter.CTkFont(size=18, weight="bold"))
        self.navbar_label.grid(row=0, column=1, sticky="w")

        # --- Navbar Buttons ---
        self.dashboard_button = customtkinter.CTkButton(self.navbar_frame, corner_radius=0, height=40, border_spacing=10,
                                                     text="Dashboard", fg_color="transparent", text_color=("gray10", "gray90"),
                                                     hover_color=("gray70", "gray30"), anchor="w",
                                                     command=lambda: self.select_frame_by_name("dashboard"))
        self.dashboard_button.grid(row=1, column=0, sticky="ew", padx=5)

        self.tools_button = customtkinter.CTkButton(self.navbar_frame, corner_radius=0, height=40, border_spacing=10,
                                                    text="Tools", fg_color="transparent", text_color=("gray10", "gray90"),
                                                    hover_color=("gray70", "gray30"), anchor="w",
                                                    command=lambda: self.select_frame_by_name("tools"))
        self.tools_button.grid(row=2, column=0, sticky="ew", padx=5)

        self.settings_button = customtkinter.CTkButton(self.navbar_frame, corner_radius=0, height=40, border_spacing=10,
                                                       text="Settings", fg_color="transparent", text_color=("gray10", "gray90"),
                                                       hover_color=("gray70", "gray30"), anchor="w",
                                                       command=lambda: self.select_frame_by_name("settings"))
        self.settings_button.grid(row=3, column=0, sticky="ew", padx=5)

        # --- Navbar State ---
        self.navbar_visible = True
        self.navbar_full_width = 200
        self.navbar_collapsed_width = 60 # Adjust as needed

        # --- Content Area ---
        self.content_area = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.content_area.grid(row=0, column=1, sticky="nsew", padx=0, pady=0)
        self.content_area.grid_rowconfigure(1, weight=1) # Allow content frame to expand
        self.content_area.grid_columnconfigure(0, weight=1)

        # --- Header ---
        self.header_label = customtkinter.CTkLabel(self.content_area, text="ORHEN STUDY HUB",
                                                   font=customtkinter.CTkFont(size=24, weight="bold"))
        self.header_label.grid(row=0, column=0, padx=20, pady=(10, 10), sticky="n")

        # --- Content Frames (Dictionary to hold them) ---
        self.content_frames = {}

        for F_name in ("dashboard", "tools", "settings"):
            frame = customtkinter.CTkFrame(self.content_area, corner_radius=10, fg_color=("gray90", "gray10")) # Slightly different bg
            frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=(0, 20)) # Pad below header, around frame
            self.content_frames[F_name] = frame
            frame.grid_remove() # Hide all frames initially

        # --- Populate Frames ---
        self.create_dashboard_frame()
        self.create_tools_frame()
        self.create_settings_frame()

        # --- Select Initial Frame ---
        self.select_frame_by_name("dashboard")

    # --- Frame Switching Logic ---
    def select_frame_by_name(self, name):
        # Reset button colors
        self.dashboard_button.configure(fg_color=("gray75", "gray25") if name == "dashboard" else "transparent")
        self.tools_button.configure(fg_color=("gray75", "gray25") if name == "tools" else "transparent")
        self.settings_button.configure(fg_color=("gray75", "gray25") if name == "settings" else "transparent")

        # Hide all frames
        for frame in self.content_frames.values():
            frame.grid_remove()

        # Show the selected frame
        self.content_frames[name].grid()

    # --- Navbar Toggle Logic ---
    def toggle_navbar(self):
        if self.navbar_visible:
            # Collapse Navbar
            self.navbar_frame.configure(width=self.navbar_collapsed_width)
            self.navbar_label.grid_remove() # Hide label
            self.hamburger_button.grid(padx=0) # Center hamburger (approx)
            # Optionally hide text or replace with icons (more complex)
            self.dashboard_button.configure(text="D", anchor="center") # Example: Use initials
            self.tools_button.configure(text="T", anchor="center")
            self.settings_button.configure(text="S", anchor="center")
            self.navbar_visible = False
        else:
            # Expand Navbar
            self.navbar_frame.configure(width=self.navbar_full_width)
            self.navbar_label.grid() # Show label
            self.hamburger_button.grid(padx=(0,10)) # Reset padding
            # Restore button text and anchor
            self.dashboard_button.configure(text="Dashboard", anchor="w")
            self.tools_button.configure(text="Tools", anchor="w")
            self.settings_button.configure(text="Settings", anchor="w")
            self.navbar_visible = True

    # --- Application Launching ---
    def launch_app(self, command, app_name):
        """Launches an application using subprocess.Popen."""
        print(f"Attempting to launch: {app_name} ({command})")
        try:
            # Use Popen for non-blocking launch
            subprocess.Popen(command.split()) # Split command string into list
            print(f"{app_name} launched successfully.")
        except FileNotFoundError:
            print(f"Error: Command '{command}' not found. Is {app_name} installed and in PATH?")
            tkinter.messagebox.showerror("Launch Error", f"Could not find '{command}'.\nPlease ensure '{app_name}' is installed and accessible in your system's PATH.")
        except Exception as e:
            print(f"An unexpected error occurred launching {app_name}: {e}")
            tkinter.messagebox.showerror("Launch Error", f"An error occurred while trying to launch {app_name}:\n{e}")

    # --- Frame Creation Methods ---
    def create_dashboard_frame(self):
        frame = self.content_frames["dashboard"]
        frame.grid_columnconfigure((0, 1), weight=1) # Make columns expandable
        frame.grid_rowconfigure(1, weight=1) # Allow button lists to expand if needed

        # --- Browsers Column ---
        browser_frame = customtkinter.CTkFrame(frame, fg_color="transparent")
        browser_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        browser_frame.grid_columnconfigure(0, weight=1)

        browser_label = customtkinter.CTkLabel(browser_frame, text="BROWSERS", font=customtkinter.CTkFont(weight="bold"))
        browser_label.grid(row=0, column=0, pady=(0, 10), sticky="ew")

        # --- !!! ADJUST COMMANDS AS NEEDED FOR YOUR SYSTEM !!! ---
        browsers = {
            "Chrome": "google-chrome-stable", # Or 'google-chrome'
            "Firefox": "firefox",
            "Vivaldi": "vivaldi-stable",      # Or 'vivaldi'
            "Chromium": "chromium-browser"    # Or 'chromium'
        }
        row_num = 1
        for name, cmd in browsers.items():
            btn_text = f"{name}" + (" (Recommended)" if name == "Chromium" else "")
            btn = customtkinter.CTkButton(browser_frame, text=btn_text,
                                          command=lambda c=cmd, n=name: self.launch_app(c, n))
            btn.grid(row=row_num, column=0, pady=5, padx=10, sticky="ew")
            row_num += 1

        # --- Cheatsheet/Utils Column ---
        utils_frame = customtkinter.CTkFrame(frame, fg_color="transparent")
        utils_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        utils_frame.grid_columnconfigure(0, weight=1)

        utils_label = customtkinter.CTkLabel(utils_frame, text="CHEATSHEET & UTILS", font=customtkinter.CTkFont(weight="bold"))
        utils_label.grid(row=0, column=0, pady=(0, 10), sticky="ew")

        # --- !!! ADJUST COMMANDS AS NEEDED FOR YOUR SYSTEM !!! ---
        utils = {
            "Text Editor": "kate", # Or 'gedit', 'mousepad', 'pluma', 'nvim', 'vim', 'nano' (terminal)
            "Terminal": "gnome-terminal", # Or 'konsole', 'xfce4-terminal', 'terminator', 'kitty'
            "Wavemon (WiFi Scan)": "wavemon" # Might require running terminal first if not graphical itself
        }
        row_num = 1
        for name, cmd in utils.items():
             # Special handling for terminal apps if needed, though Popen often works
            is_terminal_app = name in ["Terminal", "Wavemon (WiFi Scan)"] # Adjust if needed
            if is_terminal_app and cmd != "gnome-terminal" and cmd != "konsole": # Example for non-standard terms
                 # Wrap command to launch inside a default terminal (adjust your default terminal)
                 # launch_cmd = f"gnome-terminal -- {cmd}" # Example for gnome-terminal
                 launch_cmd = f"xterm -e {cmd}" # More generic fallback
            else:
                 launch_cmd = cmd

            btn = customtkinter.CTkButton(utils_frame, text=name,
                                        command=lambda c=launch_cmd, n=name: self.launch_app(c, n)) # Use adjusted command
            btn.grid(row=row_num, column=0, pady=5, padx=10, sticky="ew")

            # Add separator visually (optional)
            if name == "Text Editor":
                 sep = customtkinter.CTkFrame(utils_frame, height=2, fg_color=("gray70", "gray30"))
                 sep.grid(row=row_num + 1, column=0, pady=(5, 5), padx=10, sticky="ew")
                 row_num += 1 # Increment extra for separator row

            row_num += 1


    def create_tools_frame(self):
        frame = self.content_frames["tools"]
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(0, weight=1) # Make scrollable frame expand

        # Use a scrollable frame for potentially many tools
        scrollable_frame = customtkinter.CTkScrollableFrame(frame, label_text="Common Linux Tools")
        scrollable_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        scrollable_frame.grid_columnconfigure(0, weight=1) # Make buttons expand inside

        # --- !!! DEFINE YOUR CURATED LIST OF TOOLS HERE !!! ---
        # It's impractical to list *all* tools. Provide common/useful ones.
        # Adjust commands as needed for your system.
        linux_tools = {
            "System Monitor": "gnome-system-monitor", # Or 'ksysguard', 'xfce4-taskmanager', 'htop' (terminal)
            "File Manager": "nautilus", # Or 'dolphin', 'thunar', 'pcmanfm'
            "Network Scanner (Nmap GUI)": "zenmap", # Needs install: sudo apt install zenmap / sudo dnf install nmap-frontend
            "Network Scanner (Nmap CLI)": "nmap", # Needs terminal wrapper
            "Packet Analyzer (Wireshark)": "wireshark", # Needs install & permissions usually
            "Password Cracker (John)": "john", # Needs terminal wrapper
            "Password Cracker (Hashcat)": "hashcat", # Needs terminal wrapper
            "Disk Usage Analyzer": "baobab", # Or 'filelight'
            "Image Editor (GIMP)": "gimp", # Needs install
            "Office Suite (LibreOffice)": "libreoffice", # Needs install
            "Code Editor (VS Code)": "code", # Needs install
            "Top Processes (htop)": "htop", # Needs terminal wrapper
            # Add more tools relevant to your workflow
        }

        row_num = 0
        for name, cmd in linux_tools.items():
            # Determine if it likely needs a terminal
            is_terminal_app = cmd in ["nmap", "john", "hashcat", "htop"] # Add others if needed
            if is_terminal_app:
                # Adjust terminal command as needed
                # launch_cmd = f"gnome-terminal -- {cmd}"
                launch_cmd = f"xterm -e {cmd}" # Generic fallback
                btn_text = f"{name} (Terminal)"
            else:
                launch_cmd = cmd
                btn_text = name

            btn = customtkinter.CTkButton(scrollable_frame, text=btn_text,
                                          command=lambda c=launch_cmd, n=name: self.launch_app(c, n))
            btn.grid(row=row_num, column=0, pady=5, padx=10, sticky="ew")
            row_num += 1

        # Add a note about the limitation
        note_label = customtkinter.CTkLabel(scrollable_frame, text="\nNote: This is a curated list.\nListing *all* system tools dynamically is complex.",
                                             text_color="gray", wraplength=300, justify="left")
        note_label.grid(row=row_num, column=0, pady=(20, 5), padx=10, sticky="w")

    def create_settings_frame(self):
        frame = self.content_frames["settings"]
        frame.grid_columnconfigure(0, weight=1)
        # Add padding within the frame
        frame.grid_rowconfigure(3, weight=1) # Push elements up

        settings_label = customtkinter.CTkLabel(frame, text="Appearance Settings", font=customtkinter.CTkFont(size=16, weight="bold"))
        settings_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

        # --- Appearance Mode ---
        appearance_mode_label = customtkinter.CTkLabel(frame, text="Theme Mode:")
        appearance_mode_label.grid(row=1, column=0, padx=20, pady=(10, 5), sticky="w")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(frame, values=["Light", "Dark", "System"],
                                                               command=self.change_appearance_mode)
        self.appearance_mode_menu.grid(row=1, column=0, padx=(120, 20), pady=(10, 5), sticky="w")
        self.appearance_mode_menu.set(customtkinter.get_appearance_mode()) # Set initial value

        # --- Color Theme ---
        # Note: Changing color theme often requires app restart with CustomTkinter
        color_theme_label = customtkinter.CTkLabel(frame, text="Color Theme (Restart may be needed):")
        color_theme_label.grid(row=2, column=0, padx=20, pady=(10, 5), sticky="w")

        # Add more themes if you know specific .json theme files exist
        self.color_theme_menu = customtkinter.CTkOptionMenu(frame, values=["blue", "dark-blue", "green"],
                                                            command=self.change_color_theme)
        self.color_theme_menu.grid(row=2, column=0, padx=(240, 20), pady=(10, 5), sticky="w")
        # Getting the *current* theme isn't straightforward, default to 'blue' display
        # Or read from a saved config if you implement that
        self.color_theme_menu.set("blue")


        # --- Cursor Setting Placeholder ---
        cursor_label = customtkinter.CTkLabel(frame, text="Cursor Theme:", text_color="gray")
        cursor_label.grid(row=4, column=0, padx=20, pady=(20, 5), sticky="w")
        cursor_note = customtkinter.CTkLabel(frame, text="(System-wide cursor change is complex and\n not implemented here. Change via Desktop Environment settings.)",
                                             text_color="gray", justify="left")
        cursor_note.grid(row=5, column=0, padx=20, pady=(0, 20), sticky="w")

    # --- Settings Actions ---
    def change_appearance_mode(self, new_mode: str):
        customtkinter.set_appearance_mode(new_mode)
        print(f"Appearance mode changed to: {new_mode}")

    def change_color_theme(self, new_theme: str):
        # This might not visually update everything instantly without a restart
        # For a real effect, you'd likely save this setting and apply it
        # on the *next* launch by calling set_default_color_theme() early.
        print(f"Color theme selected: {new_theme}. Restart app for full effect.")
        tkinter.messagebox.showinfo("Theme Change", f"Color theme set to '{new_theme}'.\nA restart of the Hub might be required for the change to fully apply.")
        # Example: Save to config (pseudo-code)
        # config.set('Appearance', 'ColorTheme', new_theme)
        # config.save()


# --- Run the Application ---
if __name__ == "__main__":
    app = OrhenStudyHub()
    app.mainloop()