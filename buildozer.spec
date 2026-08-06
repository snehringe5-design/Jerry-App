[app]

# (str) Title of your application
title = Jerry AI

# (str) Package name
package.name = jerryai

# (str) Package domain (needed for android packaging)
package.domain = org.jerry

# (list) Source files to include (let it match your project files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# Yahan dhyan rahe ki python3 likha ho, koi specific version (jaise python3.14) na ho.
requirements = python3,kivy,pillow,requests

# (str) Supported orientations
orientation = portrait

#
# Android specific
#

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Enable Android auto backup
android.skip_update = False

# (str) python-for-android branch to use
p4a.branch = master
