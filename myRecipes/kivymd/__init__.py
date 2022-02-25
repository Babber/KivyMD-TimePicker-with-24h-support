from pythonforandroid.recipe import PythonRecipe

# See the documentation at https://python-for-android.readthedocs.io/en/latest/recipes/

class MDTimePickerFix(PythonRecipe):

    site_packages_name = 'kivymd'
    version = '041c7af' # master as of 220223
    url = 'https://github.com/kivymd/KivyMD/archive/{version}.zip'
    depends = ['kivy']
    
    call_hostpython_via_targetpython = False   # Due to setuptools.

    def prebuild_arch(self, arch):
        super().prebuild_arch(arch)
        self.apply_patch('timepicker.patch', arch)

    def build_arch(self, arch):
        super().build_arch(arch)

    def get_recipe_env(self, arch):
        env = super().get_recipe_env(arch)
        return env

    def postbuild_arch(self, arch):
        super().postbuild_arch(arch)

recipe = MDTimePickerFix()
