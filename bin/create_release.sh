# Get the upstream branch's version
upstream_branch="https://raw.githubusercontent.com/SSouik/pyutil/main/pyutil/__init__.py"
upstream_version=$(curl $upstream_branch | cut -d ' ' -f 3 <<< $(grep -m1 __version__) | sed 's/[".]//g')

# Get the current version of the Package
version=$(cut -d ' ' -f 3 <<< $(grep -m1 __version__ pyutil/__init__.py) | sed 's/["]//g')
current_version=$(echo $version | sed 's/[.]//g')

if [[ $upstream_version -eq $current_version ]]; then
    echo "Skipping release creation"
else
    echo "Creating release for v${version}"
    token=$1

    # Create the release
    curl \
    -X POST \
    -u "SSouik:${token}" \
    -H "Accept: application/vnd.github.v3+json" \
    https://api.github.com/repos/SSouik/pyutil/releases \
    -d "{\"tag_name\":\"v${version}\",\"name\":\"v${version}\",\"generate_release_notes\":true}\""
fi
