for image in cover_front_ru cover_front_en cover_back;
do {
	inkscape --export-text-to-path --export-filename=${image}.pdf ${image}.svg;
} done;

for image in by cc publisher_logo_ru publisher_logo_en;
do {
	inkscape --export-text-to-path --export-filename=${image}.pdf ../../svg/${image}.svg;
} done;

#for tex in header_ru header_en;
#do {
#	xelatex -interaction=nonstopmode ${tex}.tex;
#} done;
