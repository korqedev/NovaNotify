import customtkinter as ctk
from .themes import THEMES
from .animations import slide_in, fade_out


class Notify:
    active_notifications = []

    @staticmethod
    def show(
        message,
        notification_type="info",
        duration=3000,
        position="top-right",
        width=340,
        height=95
    ):
        theme = THEMES.get(notification_type, THEMES["info"])

        toast = ctk.CTkToplevel()
        toast.overrideredirect(True)
        toast.attributes("-topmost", True)
        toast.attributes("-alpha", 0.97)

        screen_width = toast.winfo_screenwidth()
        screen_height = toast.winfo_screenheight()

        margin = 20
        spacing = 12
        index = len(Notify.active_notifications)

        if position == "top-right":
            target_x = screen_width - width - margin
            target_y = margin + index * (height + spacing)
            start_x = screen_width

        elif position == "bottom-right":
            target_x = screen_width - width - margin
            target_y = screen_height - height - margin - index * (height + spacing)
            start_x = screen_width

        elif position == "top-left":
            target_x = margin
            target_y = margin + index * (height + spacing)
            start_x = -width

        elif position == "bottom-left":
            target_x = margin
            target_y = screen_height - height - margin - index * (height + spacing)
            start_x = -width

        else:
            target_x = screen_width - width - margin
            target_y = margin + index * (height + spacing)
            start_x = screen_width

        toast.geometry(f"{width}x{height}+{start_x}+{target_y}")

        frame = ctk.CTkFrame(
            toast,
            width=width,
            height=height,
            corner_radius=18,
            fg_color=theme["bg"]
        )
        frame.pack(fill="both", expand=True)

        title_label = ctk.CTkLabel(
            frame,
            text=theme["title"],
            text_color=theme["text"],
            font=("Arial", 16, "bold"),
            anchor="w"
        )
        title_label.pack(anchor="w", padx=18, pady=(14, 0))

        message_label = ctk.CTkLabel(
            frame,
            text=message,
            text_color=theme["text"],
            font=("Arial", 13),
            wraplength=280,
            anchor="w",
            justify="left"
        )
        message_label.pack(anchor="w", padx=18, pady=(4, 10))

        close_button = ctk.CTkButton(
            frame,
            text="×",
            width=28,
            height=28,
            fg_color="transparent",
            hover_color="#000000",
            text_color=theme["text"],
            command=lambda: Notify.close(toast)
        )
        close_button.place(x=width - 42, y=10)

        Notify.active_notifications.append(toast)

        slide_in(toast, target_x, target_y, start_x)

        toast.after(duration, lambda: Notify.close(toast))

    @staticmethod
    def close(toast):
        if toast in Notify.active_notifications:
            Notify.active_notifications.remove(toast)

        fade_out(toast)

    @staticmethod
    def success(message, duration=3000, position="top-right"):
        Notify.show(message, "success", duration, position)

    @staticmethod
    def error(message, duration=3000, position="top-right"):
        Notify.show(message, "error", duration, position)

    @staticmethod
    def warning(message, duration=3000, position="top-right"):
        Notify.show(message, "warning", duration, position)

    @staticmethod
    def info(message, duration=3000, position="top-right"):
        Notify.show(message, "info", duration, position)
