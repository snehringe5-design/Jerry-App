[app]

# (str) Title of your application
title = My Application

# (str) Package name
package.name =myapp

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (list) Source files to include (let it blank to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Source directories to include
source.dir = .

# (str) Application versioning
version = 0.1

# (list) Application requirements
# (python और आपकी app के लिए जरूरी modules यहाँ लिखे जाते हैं)
requirements = python3,kivy

# (str) Custom source folders for requirements
#requirements.source_dir = ../

# (list) Permissions
android.permissions = INTERNET

# (list) Features
#android.features = android.hardware.usb.host

# (str) Supported orientations
orientation = portrait

# (list) List of service to declare
#services = NAME:gsAppService:-

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (hex color code)
#android.presplash_color = #FFFFFF

# (list) The Android archs to build for,, and aarch64
android.archs = arm64-v8a, armeabi-v7a

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android NDK version to use
android.ndk = 25b

# (str) Android SDK version to use
android.sdk = 33

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) XML main theme to use for Android
#android.theme = @android:style/Theme.NoTitleBar

# (list) The format used to package the app for each architecture
android.release_artifact = apk
android.debug_artifact = apk
