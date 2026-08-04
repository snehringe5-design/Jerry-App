[app]

# (str) Title of your application
title = Jerry App

# (str) Package name
package.name = jerryapp

# (str) Package domain (needed for android packaging)
package.domain = org.jerry

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusion/exclusion patterns
source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let it empty to exclude none)
source.exclude_exts = spec

# (list) List of directory to exclude (let it empty to exclude none)
source.exclude_dirs = tests, bin, venv

# (list) List of exclusions in source files
source.exclude_patterns = license,images/unsorted/*.png

# (str) Application versioning (method 1)
version = 1.0.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Custom source folders for requirements
#requirements.source.kivy = ../../kivy

# (list) Permissions
#android.permissions = INTERNET

# (list) Features
#android.features = 

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (list) Supported orientations
orientation = portrait

# (list) List of service to declare
#services = 

#
# OSX Specific
#

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Pruned XCode projects path (experimental)
#osx.project_path = ''

# (list) Golden ratio of the target Android SDK (to use with API 33+)
android.api = 33

# (list) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use Android X
android.androidx = True

# (str) Android APK meta-data to add
#android.meta_data =

# (str) Android extra libraries to load
#android.extra_libs =

# (list) The Android archs to build for,, and 'arm64-v8a'
android.archs = arm64-v8a

# (bool) Enable Android auto backup
android.allow_backup = True

# (str) The format used to package the app for release ('aab' or 'apk')
android.format = apk

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact, storage, logging etc.
bin_dir = ./bin

# (str) Path to build directory
#build_dir = @(dir)/.buildozer

# (str) Patches to apply
#patches = ''
