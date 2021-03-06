# KivyMD TimePicker with 24-hour time support

According to Wikipedia:
> The [12-hour time convention](https://en.wikipedia.org/wiki/12-hour_clock) is common in several English-speaking nations and former British colonies, as well as a few other countries. ... In most countries, however, the 24-hour clock is the standard system used, especially in writing. ... [This system](https://en.wikipedia.org/wiki/24-hour_clock), as opposed to the 12-hour clock, is the most commonly used time notation in the world today, and is used by the international standard ISO 8601.

Unfortunately, the KivyMD project removed the option of a 24-hour clock as *unnecessary,* at the same time also referring to some Material Design related reasons, which are rather unclear to me. (See [this thread](https://github.com/kivymd/KivyMD/issues/132#issuecomment-1039161258) for yourself.) To [my enquiry](https://github.com/kivymd/KivyMD/issues/132#issuecomment-1039554915) asking what happens if I implement this feature myself, I was told that they *consciously got rid of the functionality*. This is why I post this outcast feature myself instead of a pull request to the KivyMD repo. If you like this feature of a 24-hour clock or you simply want to show your support for an inclusive TimePicker that offers both options thus making everyone happy, please, consider giving this tiny repo a Star. Who knows, if it gains enough popularity, maybe it could be part of KivyMD one day?..

Independently of this design detail, I would like to express my great appreciation to all the [Contributors](https://github.com/kivymd/KivyMD#contributors) of the [KivyMD](https://github.com/kivymd/KivyMD) project, which I find a very useful and valuable extension to Kivy!

<br>

## How to use `timepicker.py` in a desktop environment?

Releases of this repo are tagged as `v<version numbers>+<hash of the KivyMD master branch that the current patch is based on>`. If you use the given KivyMD release or one that is sufficiently similar, just replace `/kivymd/uix/pickers/timepicker/timepicker.py` with the file from here, then...

```py
#MDTimePicker.AMPM_or_24h="24h"   # to use the 24h clock (the default setting)
#MDTimePicker.AMPM_or_24h="AMPM"  # to use the 12h clock

time_dialog = MDTimePicker()
```

<br>

## How to make use of it with [Buildozer](https://github.com/kivy/buildozer) or [python-for-android](https://github.com/kivy/python-for-android/)?

The patch in the recipe is also based on the same version of the KivyMD master branch as `timepicker.py`, see above. To apply this recipe, follow the steps below:

* If you don't have it yet, create a directory in your project folder for your own recipes (e.g. `myRecipes`) and download the `kivymd` folder into it.
* You also have to amend your `buildozer.spec` file in three ways:
    * `source.exclude_dirs = ..,myRecipes` (not critical, but better so)
    * `requirements = ..,kivymd` < whatever you had here before the application of the above recipe (could be e.g. `https://github.com/kivymd/KivyMD/archive/master.zip`), now you have to refer to it with the name of your recipe: `kivymd`
    * `p4a.local_recipes = myRecipes`
* Before the next build, either delete the corresponding folders, or just `buildozer android clean` to enforce the new recipe with the patch.

<br>

![TimePicker with 24h support](TimePicker-with-24h-support.png)
