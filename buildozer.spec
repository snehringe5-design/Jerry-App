[app]

# (str) Title of your application
title = Jerry AI

# (str) Package name
package.name = jerryai

# (str) Package domain (needed for android packaging)
package.domain = org.sneh

# (str) Source code where the main.py is located
source.dir = .

# (list) Source files to include (let it include python files and assets)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (Needed by buildozer)
version = 0.1

# (list) Application requirements
requirements = python3,kivy,plyer,requests,urllib3,idna,certifi,charset_normalizer

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android SDK version to use
android.sdk = 33

# (str) Android NDK version to use
android.ndk = 25b

# (str) Supported architectures
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
