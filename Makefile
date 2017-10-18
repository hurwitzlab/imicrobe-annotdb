.PHONY: rmdb db load

DBNAME = annots.db

rmdb:
	find . -name $(DBNAME) -exec rm {} \;

db: rmdb
	sqlite3 $(DBNAME) < schema.sql

load:
	./loader.py imicrobe-blast-annots.txt
