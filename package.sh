
IMG=python3.9.1-cp39-cp39-manylinux2014_x86_64.AppImage

#python -m python_appimage build manylinux 2014_x86_64 cp39-cp39



chmod +x $IMG
./$IMG --appimage-extract

./squashfs-root/AppRun -m pip install .


cp main.py  squashfs-root/usr/bin/main
cp typeD_questions.txt squashfs-root/usr/bin
chmod +x squashfs-root/usr/bin/main
sed -i -e 's|/opt/python3.9/bin/python3.9|/usr/bin/Dtest|g' ./squashfs-root/AppRun

cp dpersona.appdata.xml squashfs-root/usr/share/metainfo
#./squashfs-root/AppRun

ARCH=x86_64 VERSION=1 ./appimagetool-640-x86_64.AppImage squashfs-root



