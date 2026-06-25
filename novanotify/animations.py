def slide_in(window, target_x, target_y, start_x, step=18):
    current_x = start_x

    def animate():
        nonlocal current_x

        if current_x > target_x:
            current_x -= step
            window.geometry(f"+{current_x}+{target_y}")
            window.after(10, animate)
        else:
            window.geometry(f"+{target_x}+{target_y}")

    animate()


def fade_out(window, alpha=1.0, step=0.05):
    def animate():
        nonlocal alpha

        alpha -= step

        if alpha > 0:
            window.attributes("-alpha", alpha)
            window.after(30, animate)
        else:
            window.destroy()

    animate()
