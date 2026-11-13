---
title: "Octominer X12 Ultra PSU Compatibility: Chicony and LiteOn Field Test"
date: 2026-11-12
lastmod: 2026-11-12
toc: true
draft: false
description: "A five-fan, three-PSU Octominer X12 Ultra test found one Chicony supply started the rig while tested LiteOn units showed amber and failed to start."
genre: ["Mining Hardware", "Computer Hardware"]
tags: ["Octominer X12 Ultra", "server power supply", "PSU compatibility", "Chicony R12-1K6P2A", "LiteOn PS-2142-2L"]
cover: "/img/cover/octominer-x12-ultra-psu-compatibility.webp"
coverAlt: "Abstract illustration of three server power supplies in a chassis with green, amber, and gray status lights"
coverCaption: ""
---

**The Chicony R12-1K6P2A started my five-fan, three-PSU Octominer X12 Ultra.** The LiteOn PS-2142-2L supplies I tried showed a green light, changed to amber, and did not start the rig. This result applies to my unit with an **OCTOMINER (12PIN) 3x DPS1200 rev. 20** power backplane. A matching wattage or a listing for a separate X12 breakout board does not establish compatibility with an Octominer backplane.

The chassis was sold as a **3,600 W configuration** with three PSU bays. [Octominer lists a three-by-1,200 W option](https://octominer.eu/product/octominer-x12-ultra-used/) for the X12 Ultra, alongside other configurations. Check the label and power board in your own rig before applying these results.

## Test results

| Supply | Result in this rig |
|---|---|
| **Chicony R12-1K6P2A, 1,600 W** | Started the rig in my test. Sustained load and operation across every bay were not measured for this article. |
| **LiteOn PS-2142-2L, 1,400 W** | Tested units showed green, then amber, and the rig did not start. |
| **Dell/Delta D1200E-S0, Dell 0F37X3** | The unusual AC inlet created a cord sourcing problem. I have no recorded start or load result for this supply in this test. |
| **HP HSTNS-PD30, 1,200 W** | Tried in the same rig. It did not start the system. |
| **Other HP Common Slot units** | The 1,200 W Platinum Plus kits and 750 W HSTNS-PD22B, HSTNS-PL22B, and HSTNS-PD18 units I tried did not start this rig. The kits' exact PSU model numbers were not recorded. |

**Do not read the LiteOn result as a fault diagnosis for every PS-2142-2L.** The observed sequence identifies a failed start in this chassis. The test did not isolate the enable signal, telemetry exchange, backplane pinout, or a defective individual supply. Likewise, the Chicony result establishes a successful start, not a certified 4,800 W chassis rating or long-term reliability record.

## Which Chicony started this rig?

The successful model was **Chicony R12-1K6P2A**, also listed as part **R1K6A002L** in [Parallel Miner's compatibility table](https://parallelminer.com/uncategorized/breakout-board-compatibility-list/). Its [80 PLUS test report](https://www.clearesult.com/80plus/sites/80plus/files/manufacturer-certificate/chicony-power-r121k6p2a-5866.pdf) identifies a 1,600 W supply rated for **200 to 240 V AC**, 10 A, 50 to 60 Hz. The report measured 94.19% efficiency at half load under its 230 V test conditions. Those efficiency figures describe the tested PSU, not the complete mining rig.

The **200 to 240 V rating matters**. Do not assume this model delivers its rated output from a 120 V receptacle. The tested supply has a standard C14 inlet, according to a [server parts listing for the exact model](https://www.itcreations.com/product/142080). Use a cord and distribution equipment rated for your input voltage and current.

My test established a successful start with the Chicony in this particular backplane. The result does not establish compatibility across every X12 Ultra revision. Match the full model number and inspect the PSU label before ordering more units.

## Why the LiteOn listing misled me

The **LiteOn PS-2142-2L** appears in [Parallel Miner's X12 breakout board compatibility table](https://parallelminer.com/uncategorized/breakout-board-compatibility-list/). Its [80 PLUS report](https://www.clearesult.com/80plus/sites/80plus/files/manufacturer-certificate/liteon-technology-corporation-ps21422l-6889.pdf) identifies a 1,400 W model. These sources establish the model and its listed use with **Parallel Miner's X12 adapter**. Neither source tests the OEM Octominer power board.

My PS-2142-2L units changed from **green to amber** after insertion, and the rig did not start. Similar output blades do not establish matching start, status, or communication behavior. The observed LED sequence alone does not prove which difference caused the failed start.

The same [Parallel Miner table](https://parallelminer.com/uncategorized/breakout-board-compatibility-list/) groups the **Dell/Delta D1200E-S0**, **LiteOn PS-2142-2L**, and **Chicony R12-1K6P2A** under its eight-pin adapter family. It places **HP HSTNS-PD30** and several 750 W HP Common Slot supplies under a different six-pin adapter family. None of the HP units I tried started this rig. The table describes Parallel Miner's boards, not a replacement list for the **OCTOMINER (12PIN)** backplane.

## Check power and cabling

The [Octominer X12 Ultra troubleshooting guide](https://octominer.com/wp-content/uploads/2021/12/X12ULTRA-TROUBLESHOOTING-GUIDE-V3.pdf?v=7516fd43adaa) says the chassis alone draws up to **200 W with fans at full speed**. It recommends at least **10% power surplus** and warns against running above **90% of the installed supplies' rated output**. Account for GPU power, the chassis, and the actual PSU output at your AC voltage.

**A 1,600 W label on each Chicony supply does not raise the published 3,600 W chassis configuration to 4,800 W.** The backplane, internal wiring, connectors, AC distribution, and cooling also limit the system. I have not measured those limits on this unit. Keep the rig within its documented configuration until Octominer confirms a higher rating for the exact board revision.

The Dell/Delta **D1200E-S0 / 0F37X3** presented a different issue: its PSU-side AC inlet needed a less common mating cord. My earlier search identified the inlet as **LS-25** and the cord-side connector as **LS-26**, based on the unit and cable listings. Verify the connector shape and electrical markings before purchasing a cord. A familiar-looking C13 plug is not a substitute for the correct mating connector.

## Verify your own X12

1. **Record the exact hardware.** Photograph the chassis label, PSU label, AC inlet, output blade, and backplane revision. Count the fans and PSU bays.
2. **Check the AC supply.** Compare the PSU input rating with the outlet, cord, and PDU ratings. The Chicony R12-1K6P2A report specifies 200 to 240 V AC.
3. **Test a minimal configuration.** Shut down and disconnect every AC feed before changing a PSU, GPU, or PSON connection. [Octominer's guide](https://octominer.com/wp-content/uploads/2021/12/X12ULTRA-TROUBLESHOOTING-GUIDE-V3.pdf?v=7516fd43adaa) recommends checking PSU seating and LEDs, the six-pin PSON cable between motherboard and power board, and one PSU with one GPU when isolating a startup problem.
4. **Record what happened.** Note the PSU model, bay, LED sequence, whether the board and fans started, and whether the rig booted. Repeat the test across bays only after a safe shutdown.
5. **Measure before adding load.** Check PSU telemetry and wall power under the intended GPU load. The startup result in this article does not replace a load test.

## Conclusion

**Chicony R12-1K6P2A is the only replacement in this comparison with a reported successful start in my three-slot X12 Ultra.** The tested LiteOn PS-2142-2L units changed from green to amber and did not start. The HP Common Slot units I tried did not start the rig either. Treat other PSU listings as research leads until the exact supply and Octominer backplane pass a controlled start and load test. Start with the model labels and backplane revision, then check Octominer's power guidance before raising the GPU load.
