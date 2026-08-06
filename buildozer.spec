[app]

# (str) Title of your application
title = Jerry AI

# (str) Package name
package.name = jerryai

# (str) Package domain (needed for android packaging)
package.domain = org.jerry

# (str) Source directory where the application resides
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusion patterns
source.include_patterns = assets/*,images/*

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy,requests,urllib3,certifi,idna,charset-normalizer,pyjnius,android

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

# (list) The Android supported architectures
android.architectures = arm64-v8a, armeabi-v7a

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version to use
android.ndk = r25b

# Explicit paths to prevent Buildozer from triggering downloads and 404 errors
android.sdk_path = /home/runner/.buildozer/android/platform/android-sdk
android.ndk_path = /home/runner/.buildozer/android/platform/android-ndk-r25b

[buildozer]

# (int) Log level (0 = error, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root (0 to bypass prompt in CI)
warn_on_root = 0
