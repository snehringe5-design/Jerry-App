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
source.include_patterns = assets/*,images/*

# (list) Application requirements
requirements = python3,kivy

# (list) Permissions
#android.permissions = INTERNET

# (str) Orientations supporting
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Whitelist of sub-architectures to build for
android.archs = armeabi-v7a

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (str) Path to build artifact storage, absolute or relative to spec file
bin_dir = ./bin
