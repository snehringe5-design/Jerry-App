[app]

# (str) Title of your application
title = Jerry AI Assistant

# (str) Package name
package.name = jerryai

# (str) Package domain (needed for android packaging)
package.domain = org.jerry

# (list) Source files to include (let it match your python files)
source.dir = .
source.exts = py,png,jpg,kv,atlas

# (list) Application requirements
# Add your dependencies here (e.g., kivy)
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (list) List of permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 24

# (list) The android archs to build for, supported: arm64-v8a, armeabi-v7a, x86
android.archs = arm64-v8a

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 1

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 1

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
