#!/bin/sh
# Create a folder (named dmg) to prepare our DMG in (if it doesn't already exist).
mkdir -p dist/dmg
# Empty the dmg folder.
rm -r dist/dmg/*
# Copy the app bundle to the dmg folder.
cp -r "dist/football-gui-mac.app" dist/dmg
# If the DMG already exists, delete it.
test -f "dist/football-gui-mac.dmg" && rm "dist/football-gui-mac.dmg"
create-dmg \
  --volname "football-gui-mac" \
  --window-pos 200 120 \
  --window-size 600 300 \
  --icon-size 100 \
  --icon "football-gui-mac.app" 175 120 \
  --hide-extension "football-gui-mac.app" \
  --app-drop-link 425 120 \
  "dist/football-gui-mac.dmg" \
  "dist/dmg/"


#  --volicon "football-gui-mac.icns" \
