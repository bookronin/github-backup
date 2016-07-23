function github2zip() {
    username=$1
    for l in $(curl "https://api.github.com/users/$username/repos?per_page=1000" | grep '"full_name":\s' | sed -e 's/"full_name": "[^\/]*\/\([^"]*\)",/\1/g');
    do
        wget "https://github.com/$username/$l/archive/master.zip" -O "$l.zip"
    done
}
