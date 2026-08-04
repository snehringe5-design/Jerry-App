[app]

# (str) Title of your application
title = Jerry AI Assistant

# (str) Package name
package.name = jerryai

# (str) Package domain (needed for android packaging)
package.domain = org.jerry

# (list) Source files to include (let it blank to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusion patterns
source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let it blank to exclude nothing)
source.exclude_exts = spec

# (list) List of directory to exclude (let it blank to exclude nothing)
source.exclude_dirs = tests, bin, venv

# (list) List of exclusions using pattern matching
source.exclude_patterns = license,images/*~

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
# (list) python3, kivy aur plyer ko yahan joda gaya hai
requirements = python3,kivy,plyer

# (str) Custom source folders for requirements
#requirements.source.kivy = ../../../kivy

# (list) Garden requirements
garden_requirements = 

# (list) Permissions
# (list) 24 ghante background service aur audio ke liye permissions
android.permissions = INTERNET, FOREGROUND_SERVICE, WAKE_LOCK, RECORD_AUDIO

# (list) Features
#android.features = android.hardware.usb.host

# (str) Supported orientations
orientation = portrait

# (list) List of service to declare
#services = MyService:service.py:autostart

#
# OSX Specific
#

#
# Author
#
author = Sneh Ringe

#
# Icon
#
icon.filename = %(source.dir)s/icon.png

#
# Presplash
#
presplash.filename = %(source.dir)s/presplash.png

#
# Supported orientations
#
osx.identity = Example Developer ID: Firstname Lastname (ABCDE12345)
osx.organization = Unknown
osx.kivy_ios_url = https://github.com/kivy/kivy-ios
osx.kivy_ios_branch = master
osx.skipped_update_requirements = 

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
bin_dir = ./bin

# (str) Path to build dependencies (CWD by default)
#android.sdk_path = /home/user/.buildozer/android/platform/android-sdk
#android.ndk_path = /home/user/.buildozer/android/platform/android-ndk
#android.api = 31
#android.minapi = 21
#android.sdk = 33
#android.ndk = 25b
#android.skip_update = False
#android.accept_sdk_license = True

# (list) Supported architectures
# (str) Yahan sirf arm64-v8a set kiya gaya hai jaisa aapne kaha tha
android.archs = arm64-v8a

# (bool) Enable AndroidX support
android.enable_androidx = True
