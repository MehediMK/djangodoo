from django.apps import apps


class Utils:
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

    def apps_name_description_icon_version(self):
        """
        Return a list of dictionaries containing app name, description, icon, and version.
        """
        app_configs = self.get_installed_configs_excepet_contrib()
        apps_list = [
            {
                "name": self.get_name(app_config),
                "description": self.get_description(app_config),
                "icon": self.get_icon(app_config),  # Default icon path `base/icon.png`
                "version": self.get_version(app_config),
            } for app_config in app_configs
        ]
        return apps_list


utils = Utils()
