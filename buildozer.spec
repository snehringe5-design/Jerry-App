[app]

# (str) Title of your application
title = Jerry App

# (str) Package name
package.name = jerryapp

# (str) Package domain (needed for android packaging)
package.domain = org.jerry

# (list) Source files to include (let it as is or include your main.py)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# Specify your python dependencies here, e.g. kivy
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

#
# Android specific
#

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25.2.9519653

# (bool) Use --private data storage (True) or --public storage (False)
android.private_storage = True

# (list) Permissions
android.permissions = INTERNET
