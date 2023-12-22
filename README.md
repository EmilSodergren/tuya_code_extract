# Steps to aquire codes

1. Install [genymotion](https://www.genymotion.com/download/)
1. Create a virtual phone with Android 5.1
1. Install:
   - [ARM Translation](https://github.com/m9rco/Genymotion_ARM_Translation/raw/master/package/Genymotion-ARM-Translation_for_5.1.zip)
   - [Smartlife](https://www.apkmirror.com/apk/volcano-technology-limited/smart-life-smart-living/smart-life-smart-living-3-6-1-release/smart-life-smart-living-3-6-1-android-apk-download/)
   - [CX File Explorer](https://www.apkmirror.com/apk/cx-file-explorer/cx-file-explorer/cx-file-explorer-1-5-6-release/cx-file-explorer-1-5-6-android-apk-download/download/)
1. Login to Smartlife
1. Look in Cx File Explorer in, System -> data/data/com.tuya.smartlife/shared_prefs/preference_global_keyeuXXXXXXXX.xml
1. Copy the contents to a file, codes.xml, in this repo.
1. Run transform.py
