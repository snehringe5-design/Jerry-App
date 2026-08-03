[app]

# (str) Title of your application
title = Jerry App

# (str) Package name
package.name = jerryapp

# (str) Package domain (needed for android packaging)
package.domain = org.jerry

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusion/exclusion patterns
source.include_patterns = assets/*,images/*

# (list) Application requirements
# (अगर आपके ऐप में और लाइब्रेरी की ज़रूरत न हो तो सिर्फ python3 और kivy रखें)
requirements = python3,kivy

# (str) Custom source folders for requirements
#requirements.source.kivy = ../../../kivy

# (list) Permissions
#android.permissions = INTERNET

# (str) Orientations supporting
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Whitelist of sub-architectures to build for
android.archs = armeabi-v7a

# (str) Supported orientations
# Valid values are: landscape, portrait, sensorLandscape or sensorPortrait
orientation = portrait

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (str) Path to build artifact storage, absolute or relative to spec file
bin_dir = ./bin

# (int) Target Android API, should be as high as possible.
# android.api = 33

# (int) Minimum API your APK will support.
# android.minapi = 21
