[app]
title = Jerry AI Assistant
package.name = jerryai
package.domain = org.jerry
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
source.exclude_exts = spec
source.exclude_dirs = bin, venv, .git, .github

# openssl aur certifi add kar diye hain taaki API error na aaye
requirements = python3,kivy,plyer,cython==0.29.36,openssl,certifi

version = 0.3
orientation = portrait

android.permissions = INTERNET,CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 33
android.min_api = 21
android.ndk = 25b
android.accept_sdk_license = True
android.androidx = True

p4a.branch = v2024.01.21
