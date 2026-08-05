[app]

title = Jerry AI
package.name = jerryai
package.domain = org.sneh
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
source.include_patterns = assets/*,images/*.png
version = 1.0

requirements = python3,kivy,requests,urllib3,idna,certifi,charset-normalizer,pyjnius

android.permissions = INTERNET,CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.features = android.hardware.camera,android.hardware.camera.autofocus

orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 21

# NDK 25b ko strict force karne ke liye
android.ndk = 25b
android.archs = arm64-v8a

android.format = apk

[buildozer]
log_level = 2
warn_root = 1
