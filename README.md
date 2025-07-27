# DjangoDoo: A Modular, Versatile Application Framework

[![GitHub Stars](https://img.shields.io/github/stars/MehediMK/djangodoo?style=social)](https://github.com/MehediMK/djangodoo/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/MehediMK/djangodoo)](https://github.com/MehediMK/djangodoo/commits/main)
[![License](https://img.shields.io/github/license/MehediMK/djangodoo)](./LICENSE)

## About the Project

DjangoDoo is an open-source framework designed to be a flexible platform for building diverse applications, inspired by the modular architecture of Odoo. Built on the Django framework, DjangoDoo enables developers to create scalable, extensible, and maintainable applications through a modular design. Each module in DjangoDoo operates independently, with its own models, views, templates, and configurations. Modules can be dynamically enabled or disabled without affecting the core system.

This project aims to provide an efficient and flexible solution for developers looking to build complex applications with ease.

---

### Key Features

- 📦 Dynamic Module Loading: Enable or disable modules without restarting the server.
- 🧩 Independent Modules: Models, views, templates, and configurations are isolated per module.
- 🔁 Module Dependencies: Define dependencies to ensure module integrity.
- 🧮 Centralized Module Registry: Manage modules from a single point.
- 🧑‍💼 Extensible Admin Interface: Manage and activate modules via Django admin.
- 📊 Custom Reporting and Logging: Extend functionality per module.
- 🕒 Version Control for Modules: Track each module version easily.

---

## Project Structure

```
djangodoo/
├── djangodoo/               # Core app for managing modules
│   ├── admin.py
│   ├── models.py
│   ├── management/
│   │   └── commands/
│   │       ├── load_modules.py
│   │       └── apply_module_migrations.py
├── modules/
│   ├── sales/
│   ├── inventory/
├── templates/
├── manage.py
├── requirements.txt
└── README.md
```

---

## Setup Instructions

### Prerequisites

- Python 3.10+
- Django 4.x
- A supported database (e.g., SQLite, PostgreSQL)

### Step-by-Step Setup

```bash
git clone https://github.com/MehediMK/djangodoo.git
cd djangodoo

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt

# Copy config
cp "config.py sample" config.py

# Run base migrations
python manage.py migrate

# Load modules from /modules
python manage.py load_modules

# Enable modules in Django admin (Core > Modules)

# Run module migrations
python manage.py apply_module_migrations

# Start server
python manage.py runserver
```

Then open: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Usage

### Adding a New Module

1. Create a folder in `modules/`, e.g., `modules/new_module/`
2. Add `apps.py` with:

```python
class ModuleConfig:
    name = "New Module"
    description = "Describe your module"
    dependencies = []
    version = '1.0.0'
    icon = "module_name/icon.png"
```

3. Add models, views, templates, migrations.
4. Register with:

```bash
python manage.py load_modules
```

### Managing Modules

- Enable/Disable via admin panel.
- Run:

```bash
python manage.py apply_module_migrations
```

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repo
2. Create a branch: `git checkout -b feature-name`
3. Make changes & commit: `git commit -m "Description"`
4. Push: `git push origin feature-name`
5. Open a Pull Request

More details in [CONTRIBUTING.md](CONTRIBUTING.md)

---

## License

This project is licensed under the [MIT License](./LICENSE).

---

## Contact

- GitHub Issues: [Create one](https://github.com/MehediMK/djangodoo/issues)
- Author: [MehediMK on LinkedIn](https://www.linkedin.com/in/mehedikhan-mk/)
