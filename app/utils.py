from werkzeug.utils import find_modules, import_string


class SetupHelper:
    def __init__(self):
        self.app = None

    def init_app(self, app):
        self.app = app

    def mount_blueprints(self, recursive=False):
        from flask.blueprints import Blueprint
        if not self.app:
            import warnings
            warnings.warn("SetupHelper didn't get Flask app instance! Use init_app(app) method!", )
            return True

        conf = self.app.config
        blue_print_dirs = conf['BLUEPRINT_DIRS']

        bp_mods = []
        for dir_name in blue_print_dirs:
            sub_mods = find_modules(dir_name, include_packages=True, recursive=recursive)
            bp_mods.extend(sub_mods)
        print('--- blueprint mounting ---')
        for bp_mod in bp_mods:
            mod = import_string(bp_mod)
            if hasattr(mod, conf['BLUEPRINT_MOD_NAME']):
                bp = getattr(mod, conf['BLUEPRINT_MOD_NAME'])
                if isinstance(bp, Blueprint):
                    print('{} register'.format(mod.__name__))
                    self.app.register_blueprint(bp)
        print('--- blueprint mounted ---')


def import_all_submods(mod_name):
    sub_mods = find_modules(mod_name, include_packages=True, recursive=True)
    for sub_mod in sub_mods:
        import_string(sub_mod)
