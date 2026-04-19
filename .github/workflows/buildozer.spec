[app]

# (str) Title of your application
title = Intruder App

# (str) Package name
package.name = intruderapp

# (str) Package domain
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv

# (str) Application version
version = 1.0

# (list) Application requirements
requirements = python3,kivy

# (str) Orientation
orientation = portrait

# (bool) Fullscreen
fullscreen = 1

# (list) Permissions (IMPORTANT for camera)
android.permissions = CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Target Android API
android.api = 31

# (int) Minimum API
android.minapi = 21

# (str) Android NDK version
android.ndk = 25b

# (str) Presplash color
presplash_color = #FFFFFF


[buildozer]

# (int) Log level
log_level = 2

# (int) Warn on root
warn_on_root = 0
