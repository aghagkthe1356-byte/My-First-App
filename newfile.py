name: Build Android APK
on:
  push:
    branches:
      - main
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Build APK
        uses: digreatbrian/buildozer-action@v4
        with:
          buildozer-cmd: buildozer -v android debug
      - name: Upload artifacts
        uses: actions/upload-artifact@v4
        with:
          name: package
          path: ./bin/*.apk
