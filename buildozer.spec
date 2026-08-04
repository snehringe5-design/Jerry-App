[app]

# (str) Title of your application
title = Jerry App

# (str) Package name
package.name = jerryapp

# (str) Package domain (needed for android packaging)
package.domain = org.jerry

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kg,atlas,ttf

# (list) Application requirements
requirements = python3,kivy,plyer,android

# (str) Version of your application
version = 0.1

# (list) Orientations supporting
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Whitelist of sub-architectures to build for
android.archs = arm64-v8a

# (int) Android API to target
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Enable AndroidX support
android.enable_androidx = True

# (bool) Automatically accept Android SDK licenses
android.accept_sdk_license = True

# (list) Permissions
android.permissions = INTERNET,RECORD_AUDIO,MODIFY_AUDIO_SETTINGS

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (str) Path to build artifact storage, absolute or relative to spec file
bin_dir = ./bin

# (bool) Allow buildozer to run as root without pausing for input
warn_on_root = 1
