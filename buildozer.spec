[app]

# (str) Title of your application
title = Jerry AI Assistant

# (str) Package name
package.name = jerryai

# (str) Package domain (needed for android packaging)
package.domain = org.jerry

# (str) Source directory where the application resides
source.dir = .

# (str) Source files to include (let separate with commas)
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files to exclude (let separate with commas)
source.exclude_exts = spec

# (list) List of directory to exclude (let separate with commas)
source.exclude_dirs = bin, venv, .git, .github

# (list) Application requirements - Gemini AI aur Plyer ke liye zaroori libraries
requirements = python3,kivy,plyer,google-generativeai,grpcio,protobuf,certifi

# (str) Version of the application
version = 0.1

# (list) Supported orientations
orientation = portrait

#
# Android specific
#

# (list) Permissions - Internet (Gemini ke liye), Camera, aur Storage
android.permissions = INTERNET,CAMERA,RECORD_AUDIO,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.min_api = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Automatically accept Android SDK license agreements
android.accept_sdk_license = True

# (bool) Use AndroidX support
android.androidx = True

# (str) python-for-android branch
p4a.branch = master
