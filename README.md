# The Earth Test

**Is Earth's 15 °C set by the pressure and the lapse rate, or by the greenhouse effect? Same planet, same sunlight, same air, same lapse rate: two runs, and an energy ledger that has to balance.**

**Interactive page:** https://davey811.github.io/earth-greenhouse/

![The Earth Test](results/earth_test.png)

## In 60 seconds

| | |
|---|---|
| Infrared emitted by the surface, measured | 396 W/m² |
| Infrared that leaves Earth, the same as the sunlight it absorbs | 240 W/m² |
| Never reaches space: trapped by the air. That is the greenhouse effect | **156 W/m²** |
| The surface with the same air but no infrared absorbers | 255 K (278 K even reflecting nothing) |

## The argument, step by step

1. **Earth is in energy balance.** It absorbs about 240 W/m² of sunlight, averaged over the planet, and sends about the same back to space as infrared. The small difference, under 1 W/m², is the warming now under way.
2. **Without infrared absorbers, the surface can't be warmer than 255 K.** Air that doesn't absorb infrared doesn't emit it either: the surface is the only thing that radiates, and all of its radiation escapes. So σT⁴, averaged over the surface, equals the 240 W/m² absorbed: 255 K, −18 °C, whatever the pressure, the winds, the convection or the lapse rate. A surface with hot and cold patches averages lower, not higher. Even reflecting nothing, the limit would be 278 K.
3. **The real surface emits 396 W/m², and only 240 leave.** The other 156 W/m² of the surface's infrared is absorbed by the air. That is the greenhouse effect: *"the infrared radiation energy trapped by atmospheric gases and clouds"* (Raval & Ramanathan 1989).
4. **The surface lives on what the air sends back.** The surface absorbs about 161 W/m² of sunlight and emits 396. The air sends back down 333 W/m² of infrared, measured; the rest leaves the surface as rising warm air and evaporation (Trenberth et al. 2009; Wild et al. 2013).
5. **The lapse rate fills in the shape.** Earth radiates to space from about 5.1 km, where the air is at 255 K; below it the troposphere warms by 6.5 K per km: 255.02 + 6.5 × 5.097 = 288.15 K. The absorbers set the height, the lapse rate sets the slope. This step explains the profile; the height and slope are read from the measured profile, so 288 K comes out by construction. The proof is in steps 1 to 4.

## Who does what

In the GISS ModelE attribution (Schmidt et al. 2010; Lacis et al. 2010), water vapour does about 50% of the present-day greenhouse effect, clouds about 25%, CO₂ about 20% and the other non-condensing gases about 5%. Water vapour and clouds condense and rain out, so their amount follows the temperature. In the model, removing the non-condensing gases makes the water follow them out: within 50 years the global mean falls to −21 °C, 34.8 K colder, and sea ice grows from 4.6% to 46.7% of the globe.

## Isn't CO₂ saturated?

At the centre of its 15 µm band the air is already opaque. But Earth radiates the band to space from aloft, and more CO₂ lifts that level to colder air: less leaves, until the column below warms up. The forcing grows with the logarithm of the concentration, 5.35 × ln(C / 280) W/m² (Myhre et al. 1998): every doubling adds the same.

| CO₂ | Forcing since 1750 | Emission level higher by | Surface warmer, before feedbacks | With feedbacks, 3 K per doubling |
|---|---|---|---|---|
| 420 ppm, today | 2.17 W/m² | 89 m | 0.58 K | 1.8 K |
| 560 ppm | 3.71 W/m² | 151 m | 0.98 K | 3.0 K |
| 1,120 ppm | 7.42 W/m² | 303 m | 1.97 K | 6.0 K |
| 2,240 ppm | 11.13 W/m² | 454 m | 2.95 K | 9.0 K |

Today's 2.17 W/m² matches the IPCC AR6 assessed CO₂ forcing for 1750–2019, 2.16 W/m². The IPCC assesses 3.93 ± 0.47 W/m² per doubling including fast adjustments, and an equilibrium climate sensitivity of 3 K, likely 2.5–4 K. Before feedbacks, the column warms by forcing / (4σT_e³) = forcing / 3.77, and the emission level rises by that warming divided by 6.5 K/km. A saturated band would give a flat line.

The spectrum on the page shades the CO₂ band, about 13–17 µm, which holds 19% of what a 288 K surface emits, next to its peak, and the window, 8–13 µm, which holds 31%.

## What a satellite sees

The spectrum on the page has a button that draws Earth's outgoing infrared as a satellite sees it, as a schematic: the window, 8–13 µm, leaves from the surface at 288 K; the CO₂ band, 13–17 µm, from the cold air near the tropopause, 216.65 K in the U.S. Standard Atmosphere; the rest from water vapour, at the temperature that makes the total 240 W/m² (232 K). The bite in the CO₂ band is the greenhouse effect seen from space. Satellites have measured this shape since 1970; between 1970 and 1997 less infrared escaped in the CO₂ and methane bands (Harries et al. 2001).

## CO₂ or the Sun? The stratosphere decides

A brighter Sun and more CO₂ both warm the surface. A brighter Sun also warms the stratosphere, where ozone absorbs its ultraviolet; more CO₂ cools it, because up there CO₂ radiates more to space than it absorbs.

| | Troposphere | Middle and upper stratosphere |
|---|---|---|
| Brighter Sun | warmer | warmer |
| More CO₂ | warmer | cooler |
| Measured, 1979–2018 | +0.6 to 0.8 K | −1 to −3 K |

Measured: satellites, radiosondes and GPS radio occultation (Steiner et al. 2020). The lower stratosphere cooled mainly because of ozone loss until the mid-1990s (IPCC AR6); the clean CO₂ signal is at 25–50 km, and natural causes can't explain it (Santer et al. 2023). Natural drivers, the Sun included, account for −0.1 to +0.1 °C of the warming since 1850–1900 (IPCC AR6, SPM A.1.3).

## Out of balance: the warming in progress

The real Earth absorbs more than it emits: 0.76 ± 0.2 W/m² on average for 2006–2020 (von Schuckmann et al. 2023), about 12 ZJ a year over the whole planet. The imbalance roughly doubled from 2005 to 2019, seen by CERES satellites and Argo ocean floats alike (Loeb et al. 2021). Of the 381 ZJ gained from 1971 to 2020, 89% is in the oceans, 6% in land, 4% went into melting ice and 1% into the air.

Why it lasts: double CO₂ at once and Earth sends out 3.7 W/m² less than it absorbs. With no feedbacks and one heat store, the top 100 m of ocean over 71% of the planet (C = 2.90 × 10⁸ J/(m²·K)), the imbalance decays as 3.71 × e^(−t/τ) W/m² with τ = C / (4σT_e³) = 2.4 years, while the surface warms towards 0.98 K. The energy stored is the imbalance added up over time. The real ocean is deeper and slower, and feedbacks bring the final warming to about 3 K: the response takes decades.

| Years after doubling | Imbalance | Surface warmer by | Stored per m² |
|---|---|---|---|
| 0 | 3.71 W/m² | 0.00 K | 0 MJ |
| 1 | 2.46 W/m² | 0.33 K | 96 MJ |
| 3 | 1.09 W/m² | 0.70 K | 202 MJ |
| 10 | 0.06 W/m² | 0.97 K | 281 MJ |

## The 5 km coincidence

| | Earth | Venus |
|---|---|---|
| Emission level | 5.10 km | 71.38 km |
| Middle of the mass | 5.48 km | 10.40 km |
| Middle-of-the-mass rule, T_e + Γ z_half | 290.72 K, off by −2.6 K | 300.94 K, off by **+434.4 K** |
| Emission-level rule, T_em + Γ z_e | 288.15 K, as measured | 735.3 K, as measured |

On Earth the two heights are 0.4 km apart, so a rule based on either almost works. On Venus they are 61 km apart. See [The Venus Test](https://github.com/Davey811/venus-greenhouse).

## If compression paid the bill

Suppose the surface were kept at 288 K by the pressure, with no greenhouse effect. It loses σT⁴ − 161 ≈ 230 W/m² more than the sunlight it absorbs. Compression supplies energy only while the air is being compressed: p₀ × v per square metre. The air would have to sink at 2.3 mm/s, 72 km a year; the whole gravitational energy of the atmosphere, 742 MJ/m² (centre of mass at 7.3 km), would last 37 days.

## The Moon test

| | Moon | Earth |
|---|---|---|
| Sunlight arriving | 1,361 W/m² | 1,361 W/m² |
| Bond albedo | 0.11 | 0.294 |
| Sunlight absorbed, planet average | 303 W/m² (26% more) | 240 W/m² |
| Black-body temperature | 270.4 K | 254.0 K (NASA, older albedo; 255.1 K with 0.294) |
| Average surface temperature | below 270 K | 288 K |
| Day–night range | 95–390 K at the equator | 283–293 K |

Same Sun, same distance: the Moon absorbs more and is colder. For a body radiating what it absorbs, the mean of T is at most the fourth root of the mean of T⁴, so its average can't exceed its black-body temperature.

## Radiation alone would be hotter

If the lapse rate set the temperature, taking convection away should cool the surface. Manabe and Strickler (1964), with the water vapour, CO₂ and ozone of Earth's air:

| | Surface |
|---|---|
| Radiation only, clear sky | 332.3 K |
| Radiation + convection at 6.5 K/km, clear sky | 300.3 K |
| Radiation + convection, average clouds | 286.9 K |
| Measured | 288 K |
| No infrared absorbers, any lapse rate | 255.1 K |

Convection cools the surface by carrying heat up to where the air can radiate it away. The lapse rate is a cap, not a stove.

## Dividing by 4 is not a flat Earth

The Sun lights Earth's disc, πR², and Earth radiates from its whole sphere, 4πR². Dividing by 4 averages the absorbed sunlight over the sphere; it doesn't say the temperature is even.

An animation on the page shows the three areas on a turning globe. The Sun sees a disc, πR², the area of Earth's shadow: 960.9 W/m² absorbed on it. The light falls on the lit half, 2πR²: 480 W/m² on average, by day only. Earth radiates from the whole sphere, 4πR², day and night: 240 W/m². Same energy, three areas:

```
960.9 × πR² = 480.4 × 2πR² = 240.2 × 4πR²
```

The 4 is the sphere. A planet with no infrared absorbers, where a share s of the sunlight is spread evenly and the rest is radiated where it falls, with no heat stored:

| Spread evenly | Average temperature | Warmest | Coldest | Sent to space |
|---|---|---|---|---|
| 0% | 144.3 K | 360.8 K | 0 K | 240.2 W/m² |
| 30% | 236.2 K | 338.5 K | 188.8 K | 240.2 W/m² |
| 50% | 246.2 K | 320.8 K | 214.5 K | 240.2 W/m² |
| 90% | 254.7 K | 272.4 K | 248.5 K | 240.2 W/m² |
| 100% | 255.1 K | 255.1 K | 255.1 K | 240.2 W/m² |

The planet always sends 240 W/m² to space; the more uneven it is, the colder its average. The even planet is the warmest case: 255 K is a ceiling, not a trick.

## The Mars test

| | Mars | Earth | Venus |
|---|---|---|---|
| Sunlight absorbed, planet average | 110 W/m² | 240 W/m² | 150 W/m² |
| Black-body temperature | 210 K | 255 K | 227 K |
| Greenhouse effect | about 5 K | 33 K | about 510 K |
| Surface pressure | 0.006 bar | 1 bar | 92 bar |
| CO₂ share of the air | 95% | 0.04% | 96.5% |
| CO₂ above each m² | about 160 kg | 6.6 kg | about 1,000 t |
| Water vapour | 210 ppm | about 1%, variable | 20 ppm |

Mars has 25 times more CO₂ above each square metre than Earth and a much smaller greenhouse effect. Absorption lines widen with pressure: at 6 millibar they are narrow and the infrared slips out between them. Mars also has almost no water vapour, and it absorbs less than half of Earth's sunlight. The share of CO₂ in the air says little; the amount, the pressure and the water decide. Mars's plain average surface temperature, about 202 K, is below its effective temperature, about 208 K, because its surface is so uneven: the fair comparison uses the fourth root of the average of T⁴ (Haberle 2013).

## Two centuries of the same physics

- **1824** Joseph Fourier: sunlight gets through the air more easily than the ground's "dark heat" gets back out.
- **1856** Eunice Foote: in sunlight, CO₂ heats more than ordinary air, and stays hot longer.
- **1859** John Tyndall: water vapour and CO₂ absorb and emit infrared; oxygen and nitrogen hardly do.
- **1879–1884** Stefan and Boltzmann: σT⁴.
- **1896** Svante Arrhenius: the first calculation of the warming from more CO₂.
- **1900** Max Planck: the spectrum of thermal radiation.
- **1964** Manabe and Strickler: radiation and convection together.
- **1967** Manabe and Wetherald: doubling CO₂ warms the surface by about 2.4 K. Manabe shared the 2021 Nobel Prize in Physics.
- **1989** Raval and Ramanathan: the greenhouse effect measured from satellites.
- **2001** Harries et al.: Earth's infrared spectrum from space, 1970 vs 1997: the greenhouse effect growing.
- **2015** Feldman et al.: CO₂'s infrared at the ground growing, 0.2 W/m² per decade.
- **2021** Loeb et al.: Earth's energy imbalance roughly doubled from 2005 to 2019.

## Objections answered on the page

Each one opens directly from its link.

- [It's the pressure: 1 bar of air keeps the surface warm.](https://davey811.github.io/earth-greenhouse/#o-pressure)
- [PV = nRT: the pressure sets the temperature.](https://davey811.github.io/earth-greenhouse/#o-ideal-gas)
- [−18 °C sits at the average height of the air, about 5 km: the lapse rate does the rest.](https://davey811.github.io/earth-greenhouse/#o-mid-mass)
- [CO₂ is only 0.04% of the air.](https://davey811.github.io/earth-greenhouse/#o-co2-trace)
- [Water vapour does it all, not CO₂.](https://davey811.github.io/earth-greenhouse/#o-water)
- [Cold air can't warm a warmer surface.](https://davey811.github.io/earth-greenhouse/#o-cold-warm)
- [Back radiation doesn't exist: it has never been measured.](https://davey811.github.io/earth-greenhouse/#o-back-radiation)
- [The greenhouse effect is just a theory: nobody has ever seen it at work.](https://davey811.github.io/earth-greenhouse/#o-never-seen)
- [Wood's 1909 experiment proved there is no greenhouse effect.](https://davey811.github.io/earth-greenhouse/#o-wood)
- [It's the Sun.](https://davey811.github.io/earth-greenhouse/#o-sun)
- [You tuned the second run to give 288 K.](https://davey811.github.io/earth-greenhouse/#o-tuned)
- [The CO₂ band is saturated: adding more changes nothing.](https://davey811.github.io/earth-greenhouse/#o-saturated)
- [CO₂ cools the planet: it radiates heat to space.](https://davey811.github.io/earth-greenhouse/#o-coolant)
- [Dividing the sunlight by 4 means a flat Earth with no night.](https://davey811.github.io/earth-greenhouse/#o-flat-earth)
- [Mars is 95% CO₂ and freezing.](https://davey811.github.io/earth-greenhouse/#o-mars)

## Using the page

Hover or touch the measured curve to read altitude, temperature and pressure; click or tap to pin the reading. "Copy link to this view" copies a link that reopens the page exactly as it is. Every section and objection has its own address, for example `#moon`, `#mars`, `#saturated`, `#imbalance`, `#divide-by-4` or `#o-co2-trace`. The sliders and buttons can be linked too: `?spread=0#divide-by-4`, `?co2=560#saturated`, `?yr=10#imbalance`, `?fp=obs#fingerprint`, `?sat=1#spectrum`. "Report an error" opens a GitHub issue already filled in.

## Files

```
index.html          interactive page (self-contained)
og.png              preview image shown when the page is shared
earth_test.py       computes every number above from the data file and draws the figure
data/
  earth_us1976.csv  U.S. Standard Atmosphere 1976, 0–50 km
results/
  numbers.txt, earth_test.png
```

```
pip install numpy matplotlib
python3 earth_test.py
```

## Method and caveats

- **Sunlight absorbed:** 1361 × (1 − 0.294) / 4 = 240.2 W/m² (NASA Earth Fact Sheet), T_e = 255.1 K. NASA's own black-body value, 254.0 K, uses the older albedo 0.306.
- **Emission level:** a sphere of radius R + h radiating the same power at T_em = T_e (R / (R + h))^½, R = 6371 km: 255.02 K at 5.097 km on the U.S. Standard Atmosphere.
- **Surface emission:** σT⁴ at 288.15 K is 391 W/m²; the measured 396 is higher because the surface is not uniform and T⁴ averages above (mean T)⁴.
- **Ledger:** "must come back from the air" is what the surface emits minus the sunlight it absorbs. The measured back radiation is larger because the surface also loses heat by rising warm air and evaporation.
- This is a test of energy bookkeeping, not a climate model. The full calculation, with spectra, water vapour and clouds, is the published models cited below.

## Sources

- NASA NSSDC Earth Fact Sheet: https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html
- NASA NSSDC Moon Fact Sheet: https://nssdc.gsfc.nasa.gov/planetary/factsheet/moonfact.html
- U.S. Standard Atmosphere 1976 (layer temperatures and lapse rates; pressures computed from the hydrostatic equation).
- K. E. Trenberth, J. T. Fasullo and J. Kiehl (2009), *Earth's global energy budget*, Bull. Amer. Meteor. Soc. 90, 311–323, doi:[10.1175/2008BAMS2634.1](https://doi.org/10.1175/2008BAMS2634.1). Surface emission 396, back radiation 333, surface absorbed solar 161 W/m², as cited by Wild et al. (2013).
- M. Wild, D. Folini, C. Schär, N. Loeb, E. Dutton and G. König-Langlo (2013), *The global energy balance from a surface perspective*, Clim. Dyn. 40, 3107–3134.
- K. E. Trenberth and J. T. Fasullo (2012), *Tracking Earth's energy: from El Niño to global warming*, Surv. Geophys. 33, 413–426, doi:[10.1007/s10712-011-9150-2](https://doi.org/10.1007/s10712-011-9150-2).
- G. A. Schmidt, R. Ruedy, R. L. Miller and A. A. Lacis (2010), *The attribution of the present-day total greenhouse effect*, J. Geophys. Res. 115, D20106, doi:[10.1029/2010JD014287](https://doi.org/10.1029/2010JD014287).
- A. A. Lacis, G. A. Schmidt, D. Rind and R. A. Ruedy (2010), *Atmospheric CO₂: principal control knob governing Earth's temperature*, Science 330, 356–359, doi:[10.1126/science.1190653](https://doi.org/10.1126/science.1190653).
- A. Raval and V. Ramanathan (1989), *Observational determination of the greenhouse effect*, Nature 342, doi:[10.1038/342758a0](https://doi.org/10.1038/342758a0).
- G. Myhre, E. J. Highwood, K. P. Shine and F. Stordal (1998), *New estimates of radiative forcing due to well mixed greenhouse gases*, Geophys. Res. Lett. 25, doi:[10.1029/98GL01908](https://doi.org/10.1029/98GL01908).
- IPCC AR6 WG1, [Chapter 7](https://www.ipcc.ch/report/ar6/wg1/chapter/chapter-7/) (2021), *The Earth's energy budget, climate feedbacks and climate sensitivity*: CO₂ forcing 1750–2019 2.16 W/m², 3.93 ± 0.47 W/m² per doubling, equilibrium climate sensitivity 3 K, likely 2.5–4 K.
- NASA NSSDC Mars Fact Sheet: https://nssdc.gsfc.nasa.gov/planetary/factsheet/marsfact.html and Venus Fact Sheet: https://nssdc.gsfc.nasa.gov/planetary/factsheet/venusfact.html
- R. M. Haberle (2013), [*Estimating the power of Mars' greenhouse effect*](https://www.sciencedirect.com/science/article/pii/S0019103513000055), Icarus.
- R. M. Haberle (2015), *Planetary atmospheres: Mars*, Encyclopedia of Atmospheric Sciences, 2nd ed., Academic Press.
- D. C. Catling and J. F. Kasting (2017), *Atmospheric Evolution on Inhabited and Lifeless Worlds*, Cambridge University Press.
- S. Manabe and R. F. Strickler (1964), *Thermal equilibrium of the atmosphere with a convective adjustment*, J. Atmos. Sci. 21, 361–385.
- S. Manabe and R. T. Wetherald (1967), *Thermal equilibrium of the atmosphere with a given distribution of relative humidity*, J. Atmos. Sci. 24, 241–259, doi:[10.1175/1520-0469(1967)024<0241:TEOTAW>2.0.CO;2](https://doi.org/10.1175/1520-0469(1967)024%3C0241:TEOTAW%3E2.0.CO;2).
- N. G. Loeb, G. C. Johnson, T. J. Thorsen, J. M. Lyman, F. G. Rose and S. Kato (2021), *Satellite and ocean data reveal marked increase in Earth's heating rate*, Geophys. Res. Lett., doi:[10.1029/2021GL093047](https://doi.org/10.1029/2021GL093047).
- K. von Schuckmann et al. (2023), *Heat stored in the Earth system 1960–2020: where does the energy go?*, Earth Syst. Sci. Data 15, 1675–1709, doi:[10.5194/essd-15-1675-2023](https://doi.org/10.5194/essd-15-1675-2023).
- J. E. Harries, H. E. Brindley, P. J. Sagoo and R. J. Bantges (2001), *Increases in greenhouse forcing inferred from the outgoing longwave radiation spectra of the Earth in 1970 and 1997*, Nature 410, 355–357, doi:[10.1038/35066553](https://doi.org/10.1038/35066553).
- S. Arrhenius (1896), *On the influence of carbonic acid in the air upon the temperature of the ground*, Phil. Mag. 41, 237–276, doi:[10.1080/14786449608620846](https://doi.org/10.1080/14786449608620846).
- E. Foote (1856), *Circumstances affecting the heat of the sun's rays*, American Journal of Science and Arts. J. Tyndall (1859), Proceedings of the Royal Society of London. J. Fourier (1824), Annales de Chimie et de Physique.
- A. K. Steiner et al. (2020), *Observed temperature changes in the troposphere and stratosphere from 1979 to 2018*, J. Climate 33, 8165, doi:[10.1175/JCLI-D-19-0998.1](https://doi.org/10.1175/JCLI-D-19-0998.1).
- IPCC AR6 WG1, [Summary for Policymakers](https://www.ipcc.ch/report/ar6/wg1/chapter/summary-for-policymakers/) (2021), A.1.3.
- R. W. Wood (1909), *Note on the theory of the greenhouse*, Phil. Mag. 17, 319–320, doi:[10.1080/14786440208636602](https://doi.org/10.1080/14786440208636602).
- D. R. Feldman, W. D. Collins, P. J. Gero, M. S. Torn, E. J. Mlawer and T. R. Shippert (2015), *Observational determination of surface radiative forcing by CO₂ from 2000 to 2010*, Nature 519, 339–343, doi:[10.1038/nature14240](https://doi.org/10.1038/nature14240).
- M. Wild et al. (2019), *The cloud-free global energy balance and inferred cloud radiative effects*, Clim. Dyn., doi:[10.1007/s00382-018-4413-y](https://doi.org/10.1007/s00382-018-4413-y).
- B. D. Santer et al. (2023), *Exceptional stratospheric contribution to human fingerprints on atmospheric temperature*, PNAS 120(20), doi:[10.1073/pnas.2300758120](https://doi.org/10.1073/pnas.2300758120).

Code under the MIT licence. Made with Python by [@splugged](https://x.com/splugged).
