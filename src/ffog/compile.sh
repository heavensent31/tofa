for image in by cc cover_front_ru cover_front_en cover_back publisher_logo_ru publisher_logo_en;
do {
	inkscape --export-text-to-path --export-filename=${image}.pdf ${image}.svg;
} done;

for image in by cc cover_front_ru cover_front_en cover_back publisher_logo_ru publisher_logo_en;
do {
	 rm ${image}.pdf;
} done;
