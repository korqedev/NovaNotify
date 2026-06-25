import customtkinter as ctk
from novanotify import Notify


class DemoApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("NovaNotify Demo")
        self.geometry("500x420")
        self.resizable(False, False)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        frame = ctk.CTkFrame(self, corner_radius=20)
        frame.pack(padx=30, pady=30, fill="both", expand=True)

        ctk.CTkLabel(
            frame,
            text="NovaNotify",
            font=("Arial", 34, "bold")
        ).pack(pady=(35, 5))

        ctk.CTkLabel(
            frame,
            text="Modern Python Toast Notifications",
            text_color="gray",
            font=("Arial", 15)
        ).pack(pady=(0, 25))

        ctk.CTkButton(
            frame,
            text="Success Notification",
            width=300,
            height=42,
            command=lambda: Notify.success("Your changes were saved successfully.")
        ).pack(pady=8)

        ctk.CTkButton(
            frame,
            text="Error Notification",
            width=300,
            height=42,
            command=lambda: Notify.error("Something went wrong. Please try again.")
        ).pack(pady=8)

        ctk.CTkButton(
            frame,
            text="Warning Notification",
            width=300,
            height=42,
            command=lambda: Notify.warning("Your storage space is almost full.")
        ).pack(pady=8)

        ctk.CTkButton(
            frame,
            text="Info Notification",
            width=300,
            height=42,
            command=lambda: Notify.info("A new update is available.")
        ).pack(pady=8)

        ctk.CTkLabel(
            frame,
            text="Made by @korqedev",
            text_color="gray",
            font=("Arial", 13)
        ).pack(side="bottom", pady=15)


if __name__ == "__main__":
    app = DemoApp()
    app.mainloop()
