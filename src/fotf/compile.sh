for image in cover_front_ru cover_front_en pic_KurzWanted pic_ValdisJin pic_EagleArcana;
do {
	inkscape --export-text-to-path --export-filename=${image}.pdf ${image}.svg;
} done;

for image in by cc tw publisher_logo_ru publisher_logo_en qr_github_tofa qr_license_by40;
do {
	inkscape --export-text-to-path --export-filename=${image}.pdf ../../svg/${image}.svg;
} done;
