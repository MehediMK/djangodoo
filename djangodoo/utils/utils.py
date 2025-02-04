import os
from pathlib import Path
import importlib
from django.apps import apps
from django.conf import settings


class Utils:
    def __init__(self):
        pass

    def get_name(self, app_config):
        """
        Get the name of the app.
        """
        return app_config.name or app_config.verbose_name

    def get_description(self, app_config):
        """
        Get the description of the app.
        """
        return getattr(app_config, "description", "No description available.")

    def get_icon(self, app_config, base_dir="djangodoo"):
        """
        Get the icon of the app.
        """
        if hasattr(app_config, "icon"):
            return getattr(app_config, "icon", f"{app_config.name}/icon.png")
        return getattr(app_config, "icon", f"{base_dir}/icon.png")

    def get_version(self, app_config):
        """
        Get the version of the app.
        """
        return getattr(app_config, "version", "1.0.0")

    def get_installed_configs_excepet_contrib(self):
        """
        Get all app configs except those contrib/default apps
        """
        return [
            app for app in apps.get_app_configs() if not app.name.startswith('django.contrib')
        ]

    def get_install_apps_info(self) -> list[dict]:
        """Get all installed apps information
        Returns:
            [{name, description, icon, version}]
        """
        app_configs = self.get_installed_configs_excepet_contrib()
        apps_list = [
            {
                "name": self.get_name(app_config).replace("_", " ").title(),
                "description": self.get_description(app_config),
                "icon": self.get_icon(app_config),  # Default icon path `base/icon.png`
                "version": self.get_version(app_config),
                "installed": True,
            } for app_config in app_configs
        ]
        return apps_list

    def get_uninstall_apps_info(self) -> list[dict]:
        """Get all uninstalled apps information
        Returns:
            [{name, description, icon, version}]
        """
        installed_apps = [i_app.name for i_app in self.get_installed_configs_excepet_contrib()]
        unstalled_apps = []
        for dir_name in os.listdir(settings.BASE_DIR):
            dir_path = settings.BASE_DIR / dir_name
            if os.path.isdir(dir_path) and os.path.exists(os.path.join(dir_path, "apps.py")):
                app_meta = {
                    "module": dir_name,
                    "name": dir_name.replace("_", " ").title(),
                    "description": "No description available.",
                    "icon": "base/icon.png",  # Default icon
                    "version": "1.0.0",
                    "installed": dir_name in installed_apps,
                }
                None if dir_name in installed_apps else unstalled_apps.append(app_meta)
        return unstalled_apps


utils = Utils()
