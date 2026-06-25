# NovaNotify

A modern Python notification framework for desktop applications.

NovaNotify provides beautiful toast notifications, animations, custom themes, and an easy-to-use API for Python developers.

Made by @korqedev

---

## Features

* Success notifications
* Error notifications
* Warning notifications
* Information notifications
* Fade animations
* Multiple themes
* Auto-dismiss timers
* Custom positioning
* Easy integration
* Reusable library structure

---

## Installation

```bash
pip install -r requirements.txt
```

Or:

```bash
pip install customtkinter
```

---

## Example Usage

```python
from novanotify import Notify

Notify.success("Profile saved successfully!")

Notify.error("Connection failed!")

Notify.warning("Low battery!")

Notify.info("New update available!")
```

---

## Project Structure

```text
NovaNotify/
├── novanotify/
│   ├── __init__.py
│   ├── notify.py
│   ├── themes.py
│   └── animations.py
├── examples/
│   └── demo.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## Planned Features

* Custom notification sounds
* Gradient themes
* Progress bar notifications
* Plugin support
* PyPI package publishing
* Dark and light mode support
* Notification stacking

---

## Requirements

* Python 3.10+
* CustomTkinter

---

## License

MIT License

---

## Author

Made by @korqedev
