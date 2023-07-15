for image in cover_front_ru cover_front_en cover_back pic_choice_sticker pic_graveyard pic_debt_graffiti;
do {
	inkscape --export-text-to-path --export-filename=${image}.pdf ${image}.svg;
} done;

for image in by cc tw publisher_logo_ru publisher_logo_en qr_github_tofa qr_license_by40;
do {
	inkscape --export-text-to-path --export-filename=${image}.pdf ../../svg/${image}.svg;
} done;

#for tex in header_ru header_en;
#do {
#	xelatex -interaction=nonstopmode ${tex}.tex;
#} done;
