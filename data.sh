#!/bin/sh
set -e

cd /lockers/tlevine_vol/jail/big.dada.pink/wikipedia-dumps

# Download
wget https://dumps.wikimedia.org/enwiki/20150304/enwiki-20150304-pages-meta-history1.xml-p000000010p000002944.7z
wget https://dumps.wikimedia.org/enwiki/20150304/enwiki-20150304-pages-meta-history1.xml-p000002945p000005211.7z
wget https://dumps.wikimedia.org/enwiki/20150304/enwiki-20150304-pages-meta-history1.xml-p000005213p000007604.7z
wget https://dumps.wikimedia.org/enwiki/20150304/enwiki-20150304-pages-meta-history1.xml-p000007605p000009966.7z
wget https://dumps.wikimedia.org/enwiki/20150304/enwiki-20150304-pages-meta-history1.xml-p000009967p000010000.7z

# Concat
cat enwiki-20150304-pages-meta-history1.xml-p*p*.7z > enwiki-20150304-pages-meta-history1.xml.7z

# Extract
7z e enwiki-20150304-pages-meta-history1.xml.7z
