#!/bin/bash

# Install packages
sudo apt install mousepad git 7zip telegram-desktop cinnamon tmux vlc nicotine smplayer chromium neovim quodlibet qbittorrent snapd gimp libreoffice-writer libreoffice-calc curl locate

# Prompt for Anki installation
read -p "Do you want to install Anki? (y/n): " INSTALL_ANKI
if [[ "$INSTALL_ANKI" =~ ^[Yy]$ ]]; then
    # Anki
    ANKI_ARCHIVE="https://apps.ankiweb.net/downloads/archive/"
    ANKI_LATEST_FILE=$(curl -s $ANKI_ARCHIVE | grep -oP '(?<=href=")[^"]*' | grep "linux-qt6" | sort | tail -n 1)
    ANKI_FULL_URL="${ANKI_ARCHIVE}${ANKI_LATEST_FILE}"
    wget $ANKI_FULL_URL
    tar xaf "$ANKI_LATEST_FILE"
    echo "Downloaded and extracted the latest Anki version: $ANKI_LATEST_FILE"
    ANKI_FOLDER_NAME=$(basename "$ANKI_LATEST_FILE" .tar.zst)
    cd "$ANKI_FOLDER_NAME"
    sudo ./install.sh
    cd ~
    rm "$ANKI_LATEST_FILE"
    rm -rf "$ANKI_FOLDER_NAME"
 
else
    echo "Skipping Anki installation."
fi

echo "##### Opening Chrome Extensions... (Remember to Sync Both Firefox profiles) #####"
chromium documents/browser/Extension*


# Others downloads
wget --content-disposition "https://discord.com/api/download?platform=linux&format=deb"
sudo dpkg -i discord*.deb
rm discord*.deb

sudo snap install snapd
sudo snap install todoist
sudo snap set core experimental.refresh-app-awareness=true
sudo snap install --classic obsidian
