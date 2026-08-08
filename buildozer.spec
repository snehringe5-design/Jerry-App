[app]

title = Jerry AI Assistant
package.name = jerryai
package.domain = org.jerry
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
source.exclude_exts = spec
source.exclude_dirs = bin, venv, .git, .github

requirements = python3,kivy,plyer,cython==0.29.36

version = 0.2
orientation = portrait

android.permissions = INTERNET,CAMERA,RECORD_AUDIO,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 33
android.min_api = 21
android.ndk = 25b
android.accept_sdk_license = True
android.androidx = True

# Python 3.14 compilation error fix karne ke liye stable branch
p4a.branch = v2024.01.21
