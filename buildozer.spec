[app]

title = Jerry AI
package.name = jerryai
package.domain = org.sneh

source.include_exts = py,png,jpg,kv,atlas
source.dir = .
version = 1.0

# Clean aur zaroori requirements
requirements = python3,kivy,plyer

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,RECORD_AUDIO

# Stable API aur SDK configuration taaki build-tools ka error na aaye
android.api = 31
android.minapi = 21
android.sdk = 31

android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
