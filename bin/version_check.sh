upstream_branch="https://raw.githubusercontent.com/SSouik/pyutil/main/pyutil/__init__.py"
upstream_version=$(curl $upstream_branch | cut -d ' ' -f 3 <<< $(grep -m1 __version__) | sed 's/[".]//g')

current_version=$(cut -d ' ' -f 3 <<< $(grep -m1 __version__ pyutil/__init__.py) | sed 's/[".]//g')

echo $upstream_version
echo $current_version

if [[ $upstream_version -ge $current_version ]]; then
    echo "Current version is not valid. Please bump the minor or patch version."
    exit 1
fi

echo "Current version checks out!"
