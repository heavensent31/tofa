# git remote add github git@github.com:regnveig/tofa.git
# git remote add 0xacab git@0xacab.org:regnveig/tofa.git
# git remote add codeberg git@codeberg.org:regnveig/tofa.git

[ -z "$1" ] && MESSAGE="$( date -Iseconds; )" || MESSAGE="$1"
git add *
git commit -a -m "${MESSAGE}" -Sregnveig@yandex.ru
git push github
git push 0xacab
git push codeberg
torify git push darktea
