# -*- coding: utf-8 -*-
"""
Prosjektoppgave PY1010
@author: Veronica Støylen
"""

# Importerer de pakkene vi skal bruke.
# pandas er til å lese Excel-filen, og matplotlib.pyplot lar oss lage diagrammer.
import pandas as pd
import matplotlib.pyplot as plt


# DEL A: Leser inn data fra Excel-filen og lagrer kolonnene i variabler.
#
# Vi leser filen 'support_uke_24.xlsx' og lagrer data for:
#   - Ukedag, Klokkeslett, Varighet og Tilfredshet.
support = pd.read_excel("support_uke_24.xlsx")

# Hent ut kolonne-data og lagre dem i variabler.
u_dag    = support['Ukedag'].values       # Data fra kolonnen "Ukedag"
kl_slett = support['Klokkeslett'].values    # Data fra kolonnen "Klokkeslett"
varighet = support['Varighet'].values       # Data fra kolonnen "Varighet"
score    = support['Tilfredshet'].values     # Data fra kolonnen "Tilfredshet"

# Skriver ut noen eksempler for å sjekke at vi har lastet inn data riktig.
print("DEL A: Eksempler fra datafilen:")
print("Ukedag (de første 5 radene):", u_dag[:5])
print("Klokkeslett (de første 5 radene):", kl_slett[:5])
print("Varighet (de første 5 radene):", varighet[:5])
print("Tilfredshet (de første 5 radene):", score[:5])
print("-----------------------------------------------------------\n")

# -----------------------------------------------------------
# DEL B: Teller antall henvendelser per ukedag og viser med stolpediagram.
#
# Vi bruker value_counts() for å telle hvor mange ganger hver ukedag forekommer.
ukedager = support["Ukedag"].value_counts()

# Vi lager en liste med ukedagene i den rekkefølgen vi ønsker å se dem.
ukedager_rekkefolge = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag"]

# Omorganiser tellingen slik at den vises i denne rekkefølgen.
ukedager_sortert = ukedager.loc[ukedager_rekkefolge]

print("DEL B: Henvendelser per ukedag:")
print(ukedager_sortert)
print("-----------------------------------------------------------\n")

# Lager et stolpediagram for å vise antallet.
ukedager_sortert.plot(kind="bar", title="Henvendelser per ukedag")
plt.xlabel("Ukedag")
plt.ylabel("Antall henvendelser")
plt.show()

# -----------------------------------------------------------
# DEL C: Finn minste og lengste samtaletid.
#
# Her antar vi at 'Varighet' er lagret som tall (f.eks. minutter).
# Hvis varighet er skrevet som tekst (f.eks. "00:05:30"), må man konvertere den først.
min_samtale = varighet.min
max_samtale = varighet.max

# -----------------------------------------------------------
# DEL D: Regn ut gjennomsnittlig samtaletid
#
# Siden samtaletiden er lagret som strenger med format "hh:mm:ss",
# må vi konvertere disse til et tidsobjekt. Det gjør vi med pd.to_timedelta().
samtaletid_numerisk = pd.to_timedelta(support['Varighet'])

# .mean() regner ut gjennomsnittet for alle samtaletidene
gjennomsnitt_samtale = samtaletid_numerisk.mean()

# Skriver ut gjennomsnittlig samtaletid til konsollen
print("Gjennomsnittlig samtaletid:", gjennomsnitt_samtale)

# -----------------------------------------------------------
# DEL E: Finn antall henvendelser i 2-timers perioder og vis med kakediagram
#
# Først må vi konvertere 'Klokkeslett'-kolonnen til datetime-objekter.
# Merk at dine klokkeslett er skrevet som "HH:MM:SS", så vi bruker formatet "%H:%M:%S".
support['Klokkeslett'] = pd.to_datetime(support['Klokkeslett'], format='%H:%M:%S')

# Nå lager vi betingelser (maske) for de ulike 2-timers periodene:
# For perioden 08-10, må vi ha timen mellom 8 og 9 (altså, fra 08:00 til før 10:00).
mask_08_10 = (support['Klokkeslett'].dt.hour >= 8)  & (support['Klokkeslett'].dt.hour < 10)
mask_10_12 = (support['Klokkeslett'].dt.hour >= 10) & (support['Klokkeslett'].dt.hour < 12)
mask_12_14 = (support['Klokkeslett'].dt.hour >= 12) & (support['Klokkeslett'].dt.hour < 14)
mask_14_16 = (support['Klokkeslett'].dt.hour >= 14) & (support['Klokkeslett'].dt.hour < 16)

# Teller antallet rader som oppfyller betingelsene for hver periode
antall_08_10 = mask_08_10.sum()
antall_10_12 = mask_10_12.sum()
antall_12_14 = mask_12_14.sum()
antall_14_16 = mask_14_16.sum()

# Skriver ut antall henvendelser for hver periode
print("Henvendelser fra 08-10:", antall_08_10)
print


