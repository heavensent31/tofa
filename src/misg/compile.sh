for image in by cc publisher_logo_ru qr_github_tofa qr_license_by40;
do {
	inkscape --export-text-to-path --export-filename=${image}.pdf ../../svg/${image}.svg;
} done;
