[app]

# (str) Title of your application
title = Jerry AI Assistant

# (str) Package name
package.name = jerryai

# (str) Package domain (needed for android packaging)
package.domain = org.jerry

# (list) Source files to include (let it blank to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files to exclude (let it blank to exclude nothing)
source.exclude_exts = spec

# (list) List of directory to exclude (let it blank to exclude nothing)
source.exclude_dirs = tests, bin, venv

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
requirements = python3,kivy,plyer

# (list) Permissions
android.permissions = INTERNET, FOREGROUND_SERVICE, WAKE_LOCK, RECORD_AUDIO

# (str) Supported orientations
orientation = portrait

# (str) Author
author = Sneh Ringe

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (str) Path to build artifact storage, absolute or relative to spec file
bin_dir = ./bin

# (list) Supported architectures (arm64-v8a)
android.archs = arm64-v8a

# (bool) Enable AndroidX support
android.enable_androidx = True
