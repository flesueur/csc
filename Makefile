SRC= $(wildcard *.md)
PDF= $(SRC:.md=.pdf)
HTML= $(SRC:.md=.html)

all: $(PDF) $(HTML)

pdf: $(PDF)

html: $(HTML)

%.html: %.md
	pandoc $< -o $@ -s

%.pdf: %.html
	wkhtmltopdf $< $@

clean:
	\rm -rf *.html *.pdf


