Timestamp=$( date -Iseconds; )
Hostname=$( hostname; )
git add *
git commit -a -m "Fast commit from ${Hostname} at ${Timestamp}" -Sregnveig@yandex.ru
git push
