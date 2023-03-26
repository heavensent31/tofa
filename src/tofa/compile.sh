for image in pic_OldSilvaSpirits pic_DelfinaQi pic_PlantQi pic_OldLarva;
do {
	inkscape --export-text-to-path --export-filename=${image}.pdf ${image}.svg;
} done;

for image in by cc tw publisher_logo_ru publisher_logo_en qr_github_tofa qr_license_by40;
do {
	inkscape --export-text-to-path --export-filename=${image}.pdf ../../svg/${image}.svg;
} done;
