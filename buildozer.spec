[app]

# (str) Title of your application
title = Jerry AI

# (str) Package name
package.name = jerryai

# (str) Package domain (needed for android packaging)
package.domain = org.jerry

# (str) Source where the app lives
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
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

# 👉 Yeh line sabse important hai: Sirf arm64-v8a rakhne se build fast hogi aur fail nahi hogi
android.archs = arm64-v8a

# (bool) Enable Android auto backup
android.skip_update = False

# (str) python-for-android branch to use
p4a.branch = master
