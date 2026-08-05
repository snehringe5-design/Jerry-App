[app]

title = Jerry AI
package.name = jerryai
package.domain = org.sneh

source.include_exts = py,png,jpg,kv,atlas
source.dir = .
version = 1.0

requirements = python3,kivy,plyer

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,RECORD_AUDIO

android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.accept_sdk_license = True

# Build speed fast karne ke liye filhal sirf arm64 rakhein
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_no_root = 1
