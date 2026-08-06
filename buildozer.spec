[app]

# (str) Title of your application
title = Jerry AI

# (str) Package name
package.name = jerryai

# (str) Package domain (needed for android packaging)
package.domain = org.jerry

# (str) Source directory where your app lives
source.dir = .

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusion patterns relative to the source dir
source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let it empty to exclude nothing)
source.exclude_exts = spec

# (list) List of directory to exclude (let it empty to exclude nothing)
source.exclude_dirs = tests, bin, venv, .git, .github

# (list) List of exclusions using pattern matching
source.exclude_patterns = license,images/unsorted/*

# (str) Application versioning
version = 1.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,requests,urllib3,certifi,idna,charset-normalizer,pyjnius,android

# (list) Custom source folders for requirements
#requirements.source.kivy = ../../../kivy

# (list) Garden requirements
garden_requirements = 

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (list) Supported orientations
orientation = portrait

# (list) List of services to include
#services = 

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (for Android)
#android.presplash_color = #FFFFFF

# (string) The Android package brand (eg. google)
#android.publisher_uri = 

# (list) Permissions
android.permissions = INTERNET,CAMERA,RECORD_AUDIO,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (list) Features (optional)
#android.features = android.hardware.camera, android.hardware.camera.autofocus

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
#android.sdk = 20

# (str) Android NDK version to use
#android.ndk = 25b

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path = 

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path = 

# (str) ANT directory (if empty, it will be automatically downloaded.)
#android.ant_path = 

# (bool) If True, then an aar will be built instead of an apk
android.archs = arm64-v8a, armeabi-v7a

# (bool) Enables Android auto backup feature (default True)
android.allow_backup = True

# (str) The format used to package the app for release/debug (apk or aab).
android.build_mode = debug
