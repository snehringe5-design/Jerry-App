[app]
title = Jerry AI Assistant
package.name = jerryai
package.domain = org.jerry
source.include_exts = py,png,jpg,kv,atlas
source.exclude_exts = spec
source.exclude_dirs = tests, bin, venv
version = 1.0
requirements = python3,kivy,plyer
android.permissions = INTERNET, FOREGROUND_SERVICE, WAKE_LOCK, RECORD_AUDIO
orientation = portrait
author = Sneh Ringe

[buildozer]
log_level = 2
bin_dir = ./bin
android.archs = arm64-v8a
android.enable_androidx = True
