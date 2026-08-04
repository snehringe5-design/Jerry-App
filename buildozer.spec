[app]

# (str) Title of your application
title = Jerry

# (str) Package name
package.name = jerry

# (str) Package domain (needed for android packaging)
package.domain = org.jerry

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusion patterns
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let it empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of exclusion patterns
#source.exclude_patterns = license,images/*.jpg

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,plyer,android

# (str) Custom source folders for requirements
#requirements.source.dir = ../../

# (list) Permissions
#android.permissions = INTERNET

# (list) Features
#android.features = android.hardware.usb.host

# (str) Supported orientations (landscape, portrait or all)
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PYTHON_SCRIPT,...

#
# OSX Specific
#

#
# Author
#

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (hex color code)
#presplash.color = #FFFFFF

# (string) Path to the Android manifest, defaults to automatic generation
#android.manifest = 

# (list) Graphic API to use (eggles = GLESv2, gles3)
#android.graphics_api = gles2

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
#android.sdk = 20

# (str) Android NDK version to use
#android.ndk = 25b

# (int) Android NDK API to use. This is the minimum API to target for NDK.
#android.ndk_api = 21

# (str) Android build tools version to use
android.sdk_build_tools_version = 33.0.3

# (str) Extra adb arguments
#android.adb_args = -d

# (list) Pyjnius gnu stl
#android.pyjnius_staticfiles = 

# (list) List of Java .jar files to add to the libs/ toplevel
#android.add_jars = foo.jar,bar.jar

# (list) List of Java files to add to the android project (can be python or java code)
#android.add_sources = 

# (list) Gradle dependencies
#android.gradle_dependencies = 

# (list) Other repositories to use
#android.gradle_repositories = 

# (list) packaging
#android.packaging = 

# (list) Java classes to add to the import
#android.add_javac_classes = 

# (list) Rules to override the build.gradle
#android.override_build.gradle = false

# (list) List of custom Gradle files to add
#android.add_gradle_files = 

# (str) python-for-android branch to use
#p4a.branch = master

# (str) Bootstrap to use for android build
#p4a.bootstrap = sdl2

# (int) Number of CPU to use for parallel compilation
#android.fork_count = 2

# (bool) Enable AndroidX support
android.enable_androidx = True


[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_root = 1

# (str) Path to build artifact, local or remote
bin_dir = ./bin

# (str) Directory to store all intermediate build files
#build_dir = ./.buildozer

# (str) Directory to store all downloaded android dependencies
#android_sdk_dir = ./.buildozer/android/platform/android-sdk

# (str) Directory to store all android ndk dependencies
#android_ndk_dir = ./.buildozer/android/platform/android-ndk-r25b
