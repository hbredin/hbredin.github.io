#!/usr/bin/env python
# encoding: utf-8

import bibparse
import sys

def tidy(string):
    replacements = [("{", ""), ("}", ""),
                    ("\\'a", "á"),
                    ("\\'e", "é"), ('\\"e', "ë"), ("\\`e", "è"),
                    ("\\'i", "í"), ('\\"i', "ï"), ('\\`i', "ì"),
                    ("\\'o", "ó"),
                    ("\\'u", "ú"), ]
    for old, new in replacements:
        string = string.replace(old, new)
    return string

def print_tab_title(f, title, papers):
    href = ''.join(title.split())
    f.write('<li><a href="#%s" data-toggle="tab">%s (%d)</a></li>\n' % (href, title, len(papers)))

def print_tab_content(f, title, papers, active=False):
    previous_year = ''
    href = ''.join(title.split())
    papers = reversed(sorted(papers, key=lambda paper: int(paper.data['Year'])))
    if active:
        f.write('<div class="tab-pane fade in active" id="%s">\n' % href)
    else:
        f.write('<div class="tab-pane fade in" id="%s">\n' % href)
    f.write('<div class="accordion" id="accordion%s">\n' % href)
    for paper in papers:
        if paper.data['Year'] != previous_year:
            f.write('<h3>%s</h3>\n' % paper.data['Year'])
            previous_year = paper.data['Year']
        f.write('<div class="accordion-group">\n')
        f.write('    <div class="accordion-heading">\n')
        f.write('        <a class="accordion-toggle" data-toggle="collapse" data-parent="#accordion%s" href="#collapse%s_%s" onClick="_gaq.push([\'_trackEvent\', \'Publications\', \'Abstract\', \'%s\']);">\n' % (href, paper.key, href, paper.key))
        f.write('        %s\n' % tidy(paper.data['Title']))
        f.write('        </a>\n')
        f.write('    </div>\n')
        f.write('    <div id="collapse%s_%s" class="accordion-body collapse">\n' % (paper.key, href))
        f.write('        <div class="accordion-inner">\n')
        f.write('        %s\n' % tidy(', '.join(paper.data['Author'].split(' and '))))
        if 'Booktitle' in paper.data:
            f.write('<p><em>%s</em></p>\n' % tidy(paper.data['Booktitle']))
        if 'Journal' in paper.data:
            f.write('<p><em>%s</em></p>\n' % tidy(paper.data['Journal']))
        if 'Abstract' in paper.data:
            f.write('<blockquote><p>%s</p></blockquote>\n' % tidy(paper.data['Abstract']))
        f.write('<i class="icon-tags"></i> <a href="https://raw.github.com/hbredin/cv/master/publi/bredin.bib" onClick="_gaq.push([\'_trackEvent\', \'Publications\', \'Bibtex\', \'%s\']);">.bib</a> [%s] | ' % (paper.key, paper.key))
        f.write('<i class="icon-book"></i> <a href="/download/pdfs/%s.pdf" onClick="_gaq.push([\'_trackEvent\', \'Publications\', \'Download\', \'%s\']);">.pdf</a>' % (paper.key, paper.key))
        f.write('        </div>\n')
        f.write('    </div>\n')
        f.write('</div>\n')
    f.write('</div>\n')
    f.write('</div>\n')

papers = bibparse.parse_bib('../cv/publi/bredin.bib')
inproceedings = [paper for paper in papers if paper.btype == 'inproceedings']
articles = [paper for paper in papers if paper.btype == 'article']
chapters = [paper for paper in papers if paper.btype == 'inbook']

f = open('research/publications.html', 'w')

f.write('---\n')
f.write('layout: page\n')
f.write('title: "Publications"\n')
f.write('description: ""\n')
from datetime import date
f.write('tagline: "last updated on %s"\n' % date.today().strftime("%B %d, %Y"))
f.write('group: research\n')
f.write('---\n')

f.write('{% include JB/setup %}\n')

f.write('<ul class="nav nav-tabs">\n')
print_tab_title(f, 'All', papers)
print_tab_title(f, 'Journal articles', articles)
print_tab_title(f, 'Book chapters', chapters)
print_tab_title(f, 'Conference and workshop proceedings', inproceedings)
f.write('</ul>\n')

f.write('<div id="myTabContent" class="tab-content">\n')
print_tab_content(f, 'All', papers, active=True)
print_tab_content(f, 'Journal articles', articles)
print_tab_content(f, 'Book chapters', chapters)
print_tab_content(f, 'Conference and workshop proceedings', inproceedings)
f.write('</div>\n')

f.close()
