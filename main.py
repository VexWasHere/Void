import customtkinter as ctk

class TopNav(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.configure(corner_radius=0, fg_color="#333333", height=60)

        # Frame for icon and tabs
        self.top_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="#333333", height=60)
        self.top_frame.pack(fill="x", pady=0)

        # Left icon placeholder
        self.icon_label = ctk.CTkLabel(self.top_frame, text="Icon", width=150, fg_color="#333333", text_color="white")
        self.icon_label.pack(side="left", padx=(10, 0))

        # Tab buttons frame aligned to the right
        self.tab_buttons_frame = ctk.CTkFrame(self.top_frame, corner_radius=0, fg_color="#333333", height=60)
        self.tab_buttons_frame.pack(side="right")

        self.tabs = ["Home", "About", "Contact"]
        self.tab_buttons = []
        for i, tab in enumerate(self.tabs):
            button = ctk.CTkButton(self.tab_buttons_frame, text=tab, command=lambda tab=tab: self.show_tab(tab),
                                  width=150,
                                  height=60,
                                  corner_radius=0,
                                  fg_color="#4CAF50" if i == 0 else "#333333",
                                  text_color="#ffffff",
                                  hover_color="#3e8e41" if i == 0 else "#333333",
                                  border_width=0,
                                  border_color="#333333")
            button.pack(side="left", padx=(10, 0) if i != 0 else (0, 0))
            self.tab_buttons.append(button)

        # Create tab content frames
        self.tab_content_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="#f0f0f0")
        self.tab_content_frame.pack(fill="both", expand=True)

        self.tab_contents = {}
        for tab in self.tabs:
            frame = ctk.CTkFrame(self.tab_content_frame, corner_radius=0, fg_color="#f0f0f0")
            if tab == "Home":
                home_label = ctk.CTkLabel(frame, text="Welcome to the Home tab!", text_color="black")
                home_label.pack(pady=20)
            elif tab == "About":
                about_label = ctk.CTkLabel(frame, text="This is the About tab.", text_color="black")
                about_label.pack(pady=20)
            elif tab == "Contact":
                contact_label = ctk.CTkLabel(frame, text="Get in touch with us on the Contact tab.", text_color="black")
                contact_label.pack(pady=20)
            frame.pack(fill="both", expand=True)
            self.tab_contents[tab] = frame

        # Show the first tab by default
        self.show_tab(self.tabs[0])

    def show_tab(self, tab):
        for frame in self.tab_contents.values():
            frame.pack_forget()
        self.tab_contents[tab].pack(fill="both", expand=True)

        # Update active tab button style
        for i, button in enumerate(self.tab_buttons):
            if i == self.tabs.index(tab):
                button.configure(fg_color="#4CAF50", text_color="#ffffff", hover_color="#3e8e41")
            else:
                button.configure(fg_color="#333333", text_color="#ffffff", hover_color="#333333")

root = ctk.CTk()
root.title("Modern Top Nav")
root.geometry("800x600")

top_nav = TopNav(root)
top_nav.pack(fill="both", expand=True)

root.mainloop()
