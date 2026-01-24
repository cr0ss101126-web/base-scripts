#!/bin/bash
echo "Identificati"
read UTENTE

if [ "$UTENTE" == "utente" ]; then
	echo "Accesso consentito! creo la tua cartella personale."
	mkdir -p Area_Privata
	echo "hai registrato un accesso il $(date)" >> Area_Privata/Benvenuto.txt
else
	echo "Accetto negato! Non sei il proprietario." 
	echo "l'intruso $UTENTE ha provato ad accedere il $(date)" >> tentativo_intrusione.log
fi
