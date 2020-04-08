CREATE TABLE DatiNazionali (
	"data" datetime not null,
	"ricoverati_con_sintomi" int not null,
	"terapia_intensiva" int not null,
	"totale_ospedalizzati" int not null,
	"isolamento_domiciliare" int not null,
	"totale_positivi" int not null,
	"variazione_totale_positivi" int not null,
	"nuovi_positivi" int not null,
	"dimessi_guariti" int not null,
	"deceduti" int not null,
	"totale_casi" int not null,
	"tamponi" int not null,
	PRIMARY KEY ("data"),
	CONSTRAINT chkData CHECK (data<=date("now"))
);