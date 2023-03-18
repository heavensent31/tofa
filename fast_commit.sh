# git remote add github git@github.com:regnveig/tofa.git
# git remote add 0xacab git@0xacab.org:regnveig/tofa.git
# git remote add darktea git@it7otdanqu7ktntxzm427cba6i53w6wlanlh23v5i3siqmos47pzhvyd.onion:regnveig/tofa.git
# git remote add codeberg git@codeberg.org:regnveig/tofa.git

git add *
git commit -a -m "${1}" -Sregnveig@yandex.ru
git push github
git push 0xacab
git push codeberg
torify git push darktea
