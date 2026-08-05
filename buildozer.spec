[app]

# (str) Title of your application
title = Jerry AI Assistant

# (str) Package name
package.name = jerryai

# (str) Package domain (needed for android packaging)
package.domain = org.jerry

# (str) Application versioning (यह लाइन जोड़नी है)
version = 0.1

# (list) Source files to include (let it match your python files)
source.dir = .
source.exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (list) List of permissions
android.permissions = INTERNET

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 24

# (list) The android archs to build for
android.archs = arm64-v8a

# (int) Log level
log_level = 1

[buildozer]
log_level = 1
warn_on_root = 1
