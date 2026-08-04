[app]

title = Jerry App
package.name = jerryapp
package.domain = org.jerry
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
requirements = python3,kivy,plyer,android
version = 0.1
orientation = portrait
android.permissions = INTERNET

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android build tools version
android.build_tools_version = 33.0.0

# (int) Android NDK version to use
android.ndk = 25b

android.private_storage = True
