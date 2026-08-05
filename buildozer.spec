[app]

# (str) Title of your application
title = Jerry AI Assistant

# (str) Package name
package.name = jerryai

# (str) Package domain (needed for android packaging)
package.domain = org.jerry

# (str) Application versioning (method 1)
version = 0.1

# (list) Source files to include (let it empty to include all files)
source.dir = .

# (list) Source files to exclude (let it empty to avoid exclusion)
source.exclude_exts = spec

# (list) List of inclusions using pattern matching
source.include_patterns = assets/*,images/*.png

# (list) Application requirements
requirements = python3,kivy,plyer,requests,urllib3,idna,certifi,charset_normalizer

# (str) Supported orientations
orientation = portrait

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug with command output)
log_level = 2

# (str) Path to build artifact, storage, etc.
bin_dir = ./bin

# -----------------------------------------------------------------------------
# Android specific

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.min_api = 21

# (bool) Use --private data storage (True) or --public (False)
android.private_storage = True

# (list) The android archs to build for, supported: arm64-v8a, armeabi-v7a, x86
android.archs = arm64-v8a
