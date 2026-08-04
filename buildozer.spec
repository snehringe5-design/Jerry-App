[app]

# (str) Title of your application
title = Jerry AI

# (str) Package name
package.name = jerryai

# (str) Package domain (needed for android packaging)
package.domain = org.jerry

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas,json,txt

# (list) List of directory to include (relative to source.dir)
source.include_dirs = 

# (list) List of exclusions
source.exclude_exts = spec

# (list) List of exclusion patterns
source.exclude_patterns = license,images/*.jpg

# (str) Source directory (where the main.py file lives)
source.dir = .

# (list) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (list) Permissions
android.permissions = INTERNET

# (list) Orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (str) Android target API, defaults to 31 as per Google Play requirements
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android SDK version to use (फिक्स कर दिया गया है ताकि 37 पर न जाए)
android.sdk = 33

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android SDK build-tools version to use
android.build_tools_version = 33.0.2

# (bool) Use Android X
android.androidx = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_root = 1
