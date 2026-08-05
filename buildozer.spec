[app]

# (str) Title of your application
title = Jerry AI

# (str) Package name
package.name = jerryai

# (str) Package domain (needed for android packaging)
package.domain = org.sneh

# (list) Source files to include (let it include all py files and assets)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusion & exclusion patterns
source.include_patterns = assets/*,images/*.png

# (str) Application versioning
version = 1.0

# (list) Application requirements
# Yahan pyjnius, requests aur networking libraries add ki hain taaki Gemini aur Android features chalein
requirements = python3,kivy,requests,urllib3,idna,certifi,charset-normalizer,pyjnius

# (list) Permissions
# Internet aur Camera ki permissions yahan set hain
android.permissions = INTERNET,CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (list) Features
android.features = android.hardware.camera,android.hardware.camera.autofocus

# (str) Supported orientations (landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) The format used to pack the app for release ('aab' or 'apk')
android.format = apk

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_root = 1
