CREATE TABLE Regioni (
	codice_regione int not null,
	denominazione_regione varchar(20) not null,
	lat  decimal(2,10) not null,
	long decimal(2,10) not null, 
	PRIMARY KEY(codice_regione)	
);
