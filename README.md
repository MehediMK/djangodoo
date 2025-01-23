# DjangoDoo: A Modular Multipurpose Application Framework

## About the Project

DjangoDoo is an open-source framework designed to serve as a multipurpose application platform, inspired by the modular architecture of Odoo. Built on the Django framework, DjangoDoo enables developers to create scalable, extensible, and maintainable applications by leveraging a modular design. Each module in DjangoDoo operates independently, with its own models, views, templates, and configurations, allowing dynamic enablement or disablement without affecting the core system.

This project aims to provide an efficient and flexible foundation for developing large-scale applications with minimal effort, following industry best practices.

### Key Features
- **Dynamic Module Loading**: Modules can be enabled or disabled dynamically.
- **Independent Modules**: Each module has its own models, views, templates, migrations, and configurations.
- **Module Dependencies**: Modules can define dependencies on other modules.
- **Centralized Module Registry**: All modules are registered and managed from a central location.
- **Extensible Admin Interface**: Manage modules directly from the Django admin panel.
- **Custom Reporting and Logging**: Modules can implement custom reporting and logging mechanisms.
- **Version Control for Modules**: Track and manage the version of each module.

---

## Project Structure

```
djangodoo/
├── djangodoo/               # Core app for managing modules
│   ├── admin.py             # Admin interface for modules
│   ├── models.py            # Module registry model
│   ├── management/          # Custom management commands
│   │   └── commands/
│   │       ├── load_modules.py
│   │       └── apply_module_migrations.py
├── modules/                 # Folder containing all modules
│   ├── sales/               # Example module: Sales
│   │   ├── migrations/      # Independent migrations for this module
│   │   ├── models.py        # Models for this module
│   │   ├── views.py         # Views for this module
│   │   ├── templates/       # Templates for this module
│   │   └── __init__.py      # Module configuration
│   ├── inventory/           # Example module: Inventory
├── templates/               # Global templates
├── manage.py                # Django's CLI entry point
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## Setup Instructions

Follow the steps below to set up the project locally:

### Prerequisites
- Python 3.10+
- Django 4.x
- A database (SQLite, PostgreSQL, etc.)

### Step 1: Clone the Repository

```bash
git clone https://github.com/MehediMK/djangodoo.git
cd djangodoo
```

### Step 2: Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```
### step 4: Setup Configuration in config.py
```bash
copy "config.py sample" config.py
```
### Step 5: Apply Initial Migrations

Run migrations for the core system:

```bash
python manage.py migrate
```

### Step 6: Register and Enable Modules

1. Place your modules inside the `modules/` directory.
2. Use the `load_modules` management command to register modules:

   ```bash
   python manage.py load_modules
   ```

3. Enable desired modules from the Django admin panel (Core > Modules).

### Step 7: Apply Module Migrations

Run migrations for all enabled modules:

```bash
python manage.py apply_module_migrations
```

### Step 8: Start the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

---

## Usage

### Adding a New Module

1. Create a new folder in the `modules/` directory, e.g., `modules/new_module/`.
2. Define your module's configuration in `__init__.py`:

   ```python
   class ModuleConfig:
       name = "New Module"
       version = "1.0"
       description = "Description of the new module"
       dependencies = []  # List of module names this module depends on
   ```

3. Add your models, views, templates, and migrations in the new module folder.
4. Register the module using the `load_modules` command.

### Managing Modules

- **Enable/Disable Modules**: Use the admin panel or update the `enabled` field in the `Module` model.
- **Check Module Dependencies**: Ensure all dependencies are enabled before activating a module.
- **Apply Module Migrations**: Use the `apply_module_migrations` command.

---

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

---
