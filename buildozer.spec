[app]

# (str) Title of your application
title = Jerry AI

# (str) Package name
package.name = jerryai

# (str) Package domain (needed for android packaging)
package.domain = org.sneh

# (str) Source directory where your application resides
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusion & exclusion patterns
source.include_patterns = assets/*,images/*.png

# (str) Application versioning
version = 1.0

# (list) Application requirements
requirements = python3,kivy,requests,urllib3,idna,certifi,charset-normalizer,pyjnius

# (list) Permissions
android.permissions = INTERNET,CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (list) Features
android.features = android.hardware.camera,android.hardware.camera.autofocus

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Supported architectures (Sirf arm64-v8a rakhne se build fast ho jata hai)
android.archs = arm64-v8a

# (str) The format used to pack the app for release
android.format = apk

[buildozer]
log_level = 2
warn_root = 1
