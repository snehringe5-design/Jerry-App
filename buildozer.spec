[app]

# (str) Title of your application
title = My Application

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source directory where the main.py file lives
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,kivy

# (str) Version of your application
version = 0.1

# (str) Supported orientations
orientation = portrait

# (list) List of permissions
android.permissions = INTERNET

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.min_api = 21

# (str) Android NDK version to use
android.ndk = 25.2.9519653

# (bool) Use --private data storage
android.private_storage = True

# (str) python-for-android branch to use
p4a.branch = master
