[app]

# (str) Title of your application
title = Jerry AI

# (str) Package name
package.name = jerryai

# (str) Package domain (needed for android packaging)
package.domain = org.sneh

# (list) Source files to include (let it default to all)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
source.include_patterns = assets/*,images/*.png

# (list) Application source directory
source.dir = .

# (str) Application versioning
version = 1.0

# (list) Application requirements
# Yahan pyjnius, requests aur plyer zaroori hain mic, internet aur speech ke liye
requirements = python3,kivy,plyer,requests,urllib3,certifi,idna,charset-normalizer,pyjnius

# (list) Custom source folders for python modules
#source.main_ext = py

# (list) Application orientation
orientation = portrait

# (list) List of services to declare
#services = 

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
# Yeh line mic aur internet ke liye sabse zaroori hai
android.permissions = INTERNET,RECORD_AUDIO

# (list) Features
#android.features = android.hardware.usb.host

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android SDK version to use
#android.sdk = 20

# (str) Android NDK version to use
#android.ndk = 25b

# (int) Android NDK version to use. If left empty, it will use the default.
#android.ndk_version = 

# (bool) Use --private data storage (True) or --public storage (False)
#android.private_storage = True

# (str) Android app theme, or use custom style
#android.theme = @android:style/Theme.NoTitleBar

# (list) Python for android (p4a) specific options
#p4a.branch = master

# (str) Bootstrap to use for android builds
#p4a.bootstrap = sdl2

# (str) extra prebuild commands
#p4a.prebuild = 

#
# Python for android (p4a) specific
#

# (str) The android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

# (int) Port number to use for p4a webview debugging
#android.webview_debug_port = 0

[buildozer]

# (int) Log level (0 = error, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
#bin_dir = ./bin

# (str) Path to build output (default is the root of the app)
#build_dir = ./build
