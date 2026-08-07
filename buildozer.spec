[app]

# (str) Title of your application
title = My Application

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android packaging)
package.domain = org.example

# (str) Source directory where the application resides
source.dir = .

# (str) Source files to include (let separate with commas)
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files to exclude (let separate with commas)
source.exclude_exts = spec

# (list) List of directory to exclude (let separate with commas)
source.exclude_dirs = bin, venv, .git, .github

# (list) Application requirements
requirements = python3,kivy

# (str) Version of the application
version = 0.1

# (list) Supported orientations
orientation = portrait

#
# Android specific
#

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.min_api = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use AndroidX support
android.androidx = True

# (str) python-for-android branch
p4a.branch = master
