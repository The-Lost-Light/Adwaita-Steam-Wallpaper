#!/usr/bin/env sh

test "$#" -eq 0 && echo "Need the image path" && exit 1

IMAGE_PATH="$1"
CSS_URL="https://raw.githubusercontent.com/The-Lost-Light/Adwaita-Steam-Wallpaper/refs/heads/main/custom.css"
TARGET_DIR="$HOME/.steam/steam/steamui/adwaita/custom"

mkdir -p "$TARGET_DIR"
curl -s -o "$TARGET_DIR/custom.css" "$CSS_URL"
sed -i '3s|--image-path:.*|--image-path: url("'"$(basename "$IMAGE_PATH")"'");|' "$TARGET_DIR/custom.css"
cp "$IMAGE_PATH" "$TARGET_DIR/"

echo "Copied custom.css and the image to $TARGET_DIR"
