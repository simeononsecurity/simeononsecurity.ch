---
title: "Flock Cameras: Public Safety Tool or Warrantless Surveillance Machine?"
date: 2026-08-01
lastmod: 2026-09-20
toc: true
draft: false
description: "An independent analysis of Flock Safety ALPR cameras: how they work, what data they collect beyond license plates, how data sharing creates a shadow national database, and why the warrant question is the real issue."
genre: ["Privacy", "Surveillance", "Civil Liberties", "Law Enforcement Technology", "Digital Rights"]
tags: ["Flock Safety", "ALPR", "license plate readers", "surveillance", "privacy", "warrantless surveillance", "convoy analysis", "Bluetooth tracking", "TPMS tracking", "data sharing", "Ring cameras", "Fourth Amendment", "nothing to hide", "LPR accuracy", "wrongful accusation", "MFA", "law enforcement technology", "civil liberties", "data minimization", "DeFlock", "counter-surveillance", "public safety", "police surveillance", "privacy rights", "Fourth Amendment", "digital surveillance", "mass surveillance", "license plate recognition", "camera networks", "data retention"]
cover: "/img/cover/flock-safety-cameras-public-safety-surveillance.webp"
coverAlt: "A night cityscape featuring Flock Safety cameras on poles capturing images of passing vehicles. Glowing data streams connect the cameras to the cars, emphasizing a network of surveillance."
coverCaption: ""
canonical: "https://simeononsecurity.com/articles/flock-cameras-public-safety-or-surveillance-2026/"
---

**The debate over Flock Safety cameras divides people in a way almost nothing else does in technology policy. Those who have had a car stolen tend to love them. Those who study constitutional law tend to hate them. Both are reacting to something real.**

This is an independent analysis of what these systems do, what the evidence says about their accuracy and misuse, and why the most important question is not whether cameras photograph public streets. It is whether the government should build a searchable, warrantless database of everyone's movements.

{{< youtube id="fFuE2-xtq2w" >}}

*This topic generated significant public discussion in mid-2026. The video above covers a range of viewer perspectives and counterarguments worth considering alongside the analysis here.*

______

## Why Flock Cameras Are Different From Your Phone

The most common defense of Flock Safety cameras goes like this: your phone already tracks you everywhere. Police need a warrant to get your GPS data. Flock cameras are less precise than phone tracking. So why worry?

The argument is superficially reasonable and fundamentally wrong.

**Your phone tracks you. Flock cameras track everyone.** When police obtain your cell tower location data or GPS history, they need a warrant, a specific target, and probable cause. When an officer queries the Flock database, they do not need any of those things. They search by plate number, time window, location, or vehicle description, without a warrant, without a named suspect, without any suspicion at all.

The result is **warrantless mass surveillance of an entire population**, not targeted surveillance of a specific individual. The Fourth Amendment was specifically designed to prevent exactly this kind of general search.

Cell phone tracking also does not build a permanent, queryable record of every vehicle passing every intersection in your city over the last 30 days. Flock does. This persistent, structured database is what makes it qualitatively different from a cop writing down a plate number or a business installing a security camera.

**A photograph is not a surveillance system. A searchable, timestamped database of photographs linked by vehicle identity across hundreds of cameras is.**

______

## What "Convoy Analysis" Means

Flock Safety markets a feature called **convoy analysis**, the ability to track multiple vehicles traveling together as a group. The marketing language is bland. The implications are not.

Convoy analysis means Flock identifies when two or more specific vehicles move together, correlates their travel patterns over time, and flags when a historically associated group reconvenes. In a law enforcement context, this means tracking protest organizers who drive to the same locations, identifying which cars attend political meetings, or monitoring people who regularly gather in the same neighborhood.

None of these people need to have done anything illegal for their convoy associations to be recorded and stored.

The feature has legitimate applications, such as tracking a suspected criminal organization's vehicles. But the same feature applied to a database with no warrant requirement means it applies to anyone. It is the infrastructure for political surveillance, whether or not it is the intent today.

______

## What Flock Cameras Collect Beyond License Plates

The license plate is the most visible data point, but it is not the only one. Here is what the evidence shows about the broader signal collection by these camera networks.

### Bluetooth and WiFi MAC Address Sniffing

**This is real, documented, and frequently underreported.**

Many ALPR deployments, not only Flock, include WiFi and Bluetooth scanning capability. When your phone's WiFi or Bluetooth is enabled and not connected, it broadcasts **probe requests** containing your device's MAC address. A camera with a WiFi radio passively logs these addresses alongside the license plate read.

This matters enormously: your MAC address is linked to *you*, not your car. If you ride in someone else's vehicle, rent a car, or drive a borrowed car, your phone still broadcasts your identity. Convoy analysis now includes the device-level identities of every passenger, not only the driver.

Even if the deployment you're concerned about does not currently do this, the hardware and software capability often exists. The question of what data is *collected* and what data is *retained* are separate questions, and auditing compliance is effectively impossible without a public warrant requirement.

### TPMS Sensor Tracking

**Tire Pressure Monitoring System (TPMS) sensors** transmit a unique identifier on UHF radio frequencies. These IDs are not encrypted and are broadcast whenever the tire is rolling. Researchers have demonstrated passive TPMS sniffers alongside roadways logging vehicle identities. Unlike license plates, TPMS IDs are not visible to the public and cannot be changed without replacing the sensors.

A TPMS ID correlates to a specific set of tires. When those tires are mounted on a vehicle, the TPMS ID is functionally equivalent to a license plate you did not know you had and cannot display differently.

This is not a hypothetical future capability. RTL-SDR receivers which log TPMS signals cost around $40. The technical barrier to deploying passive TPMS monitoring alongside an ALPR network is low.

{{< figure src="flock-tpms-bluetooth-surveillance.webp" alt="Diagram showing how a roadside Flock camera passively captures license plates, Bluetooth MAC addresses from phones, and TPMS tire sensor IDs from passing vehicles simultaneously" >}}

______

## What the Camera Recorded

**In September 2026, a hacker collective removed a Flock camera from a pole, copied its storage, and published the filesystem images through Distributed Denial of Secrets.** The recovered logs gave researchers a complete operating record for a real deployment, and the numbers are larger than the public marketing implies.

*The camera was not hacked. It was unscrewed.*

### Twenty-One Days of Traffic

The recoverable logs covered roughly **21 days** of operation across several periods. Over those windows the camera photographed about **50,200 vehicles and generated roughly 1.6 million images**.

| Measure | Value |
|---------|-------|
| Vehicles photographed | **50,200** |
| Images generated | **~1.6 million** |
| Typical day | ~3,300 vehicles |
| Busiest logged day | **4,454 vehicles** |
| Images per passing vehicle | ~28 typical, **over 100 in some cases** |

Older logs had been overwritten on the device, so the camera ran longer than the captured window shows. **A single roadway position produced a million images in under a month.**

### Every Vehicle Gets Dozens of Photographs

When motion enters the frame, the camera fires a rapid burst. A typical passing vehicle produced about **28 images**, and some produced more than 100.

The camera shoots at **different exposures** so it captures the license plate and the wider scene in separate frames, then scans the results, crops useful frames, and uploads them over cellular. The device itself does not read the plate. It runs roughly **20 Flock-built apps** handling motion detection, image capture, object classification, upload, and remote updates. **Plate reading and vehicle identification happen on Flock's servers, not at the roadside.**

This distinction matters for the warrant argument. The camera is not a passive recorder of a plate number. It is a sensor feeding a remote identification pipeline.

### The Software Detects People Too

Flock states its cameras detect vehicles. The recovered code shows otherwise.

**The on-device software explicitly includes a person detector.** When it identifies a person, it records where the person appears in the frame and a confidence score for the detection. This sits separate from the vehicle, plate, and bicycle detectors, and it is a deliberate part of the product rather than an artifact of a general-purpose model.

WIRED tested the claim by extracting the models from the device and running them against recovered footage and control images. **The models readily detected people, including in a reporter's selfie.** Running the models across **27,321 stored video clips** returned person detections in 11 clips, all of them motorcyclists. The low count reflects camera placement above a roadway aimed at traffic lanes, not a limitation of the detector.

**Those clips are the other finding worth noting.** They are **MP4 video files, one to two seconds long, at 1024 by 768 pixels without audio**, and they are stored separately from the high-resolution still bursts. Flock's public descriptions emphasize still images of plates. The device also records short video.

*Flock maintains its cameras do not perform face recognition, and the investigation found no evidence of face recognition beyond capabilities included by default in Android, which did not appear enabled or in use.*

### The Plate Detector Sees Plates Everywhere

The same investigation found the license plate detector interpreting graphics as plates.

**Bumper stickers, dealership frames, and other vehicle graphics were cropped out as if they were license plates.** In one video of a passing motorcycle, the detector isolated an **American flag patch on the rider's saddlebag** and treated it as a plate.

This is a technical accuracy problem and a privacy problem at once. It shows the detector's classification is loose enough to collect images of things it was not designed to collect, and those images travel to the same servers as legitimate reads.

### The Camera Was Running Out of Space

The logs show a device under constant storage pressure.

Recovered logs recorded **more than 27,000 "no space left on device" errors** while attempting to save full-resolution images, alongside tens of thousands of related errors, crashes, and reboots.

Two log messages stand out for what they say about the engineering.

- Roughly every two minutes, a service checked whether the camera was still running and logged the message **"Who's a good boy?!"**. More than **12,000** of those entries appear in the recovered logs.
- When the camera restarted, another service left the message **"A reboot was requested! ¡Adiós, Amigos!"**

The tone is informal. The substance is not. This is a surveillance device missing eight years of operating system patches, and it spends its time crashing and running out of disk while saving the images it exists to collect.

______

## The Product Line Collects More Than Plates

The recovered camera was one Falcon unit. The fleet around it is larger, and the newer products collect signals a license plate reader never touched.

### The Audio Sensor Classifies Distress

**Raven** is an audio detection device mounted separately from the cameras. It runs on an ESP32 with a Syntiant NDP120-B0 neural DSP, and it initially shipped to sort four classes of sound: gunshots, tires, background, and unknown.

**An October 2025 firmware update added a fifth class, sounds of human distress.** The sensor now scores whether a person nearby sounds like they need help, and it auto-cues co-located Condor and Falcon cameras through Flock's FlockOne platform layer.

*This expansion is the one to pay attention to. A device marketed as gunshot detection quietly became an acoustic distress monitor.*

### The Cameras Now Fly

**Alpha** is Flock's own drone, unveiled in October 2025 and flying in active deployment, including a **South Bend Police Department pilot in March 2026**. It is Flock-designed, US-assembled, and NDAA-compliant.

| Specification | Value |
|---------------|-------|
| Maximum speed | **60 MPH** |
| Flight time | ~45 minutes |
| Battery swap | **90 seconds** at a dual-battery dock |
| Cellular links | **4 independent modems** for failover |
| Plate reading altitude | **up to 2,000 feet** |
| Coverage | Up to **50 square miles per dock** |

**Aerodome** is the legacy drone line, inherited through a **$300 million acquisition in October 2024**. It flies DJI Matrice M350 and M300 RTK airframes, and the Hextronics Atlas nest holds eight batteries for continuous operation. Prosper Police and Scottsdale still operate them.

### The Network Ingests Other People's Cameras

**Wing** is not hardware. It is a software bridge announced in October 2025, and it wraps existing third-party IP cameras with Flock's analytics so non-Flock cameras feed into the same **Nova** investigation surface.

**This changes the scale of the question.** A city installing Flock cameras knows exactly what it installed. A city running Wing converts its existing camera estate into Flock sensors without buying a single new camera, and the footage lands in one searchable system.

### The Trailer Makes Deployment Trivial

The **LPR Trailer** mounts a Flock camera on an All Traffic Solutions ATS-5 chassis with **120 watts of solar**, a **47 amp-hour battery**, and a radar unit with a message sign. It attaches to a 2 inch receiver hitch and deploys with one person.

It also reports tampering and low battery, which tells you the company expects the hardware to be interfered with in the field.

______

## The Real Problem: Photography vs. Database

Taking a photo of a car on a public street is legal. A police officer writing down a license plate is legal. A neighbor's security camera recording traffic is legal.

None of those activities are the same as **building a centralized, searchable, indefinitely retained database of every vehicle movement across an entire city**.

The legal right to observe public spaces does not automatically extend to the right to aggregate those observations into a surveillance infrastructure which functions like a 30-day continuous tail on every person who drives.

The Supreme Court has recognized this distinction. In *Carpenter v. United States* (2018), the Court found the aggregation of cell tower records over time into a comprehensive record of a person's movements requires a warrant, even though each individual record was already provided to a third party. The Court noted pervasive tracking changes the constitutional calculus.

Flock Safety cameras are doing exactly what *Carpenter* warned about, at scale, automatically, without warrants, on the entire population.

______

## Data Sharing and the Shadow National Network

{{< figure src="flock-data-sharing-shadow-national-network.webp" alt="Map diagram showing how individual city and county Flock camera networks connect through data-sharing agreements into a broader regional and quasi-national searchable database" >}}

Individual Flock camera networks are not isolated. Cities and counties enter **data-sharing agreements** with neighboring jurisdictions, meaning a query in one city pulls records from dozens of others. Some of these sharing agreements are permissive enough for a single agency to effectively access a regional or quasi-national database.

**This is how a local camera network becomes a de facto national surveillance system without Congress ever voting on it.**

The data sharing is voluntary and legally murky. There is no federal statute authorizing it. There are no standardized data retention limits. There are no mandatory audit requirements. And there is no mechanism for a citizen to find out whether their vehicle's movements have been queried.

**The scale of this access is now documented.** In Alpharetta, Georgia, WIRED found records from the city's Flock cameras were reachable by **more than 2,000 agencies**, including police departments, colleges, airports, and the Office of Inspector General for the federal General Services Administration. The agency count is not a quirk of Alpharetta's own agreements. It reflects how Flock's national network is wired by default.

DeFlock.org, which crowdsources Flock camera locations, has mapped over **124,000 suspected LPR deployments** across the United States. The coverage in urban and suburban areas is dense enough for driving across most American cities to generate a near-continuous surveillance record.

______

## Ring Cameras, Flock, and Warrants

Flock Safety and Amazon Ring are different products, but they share a critical characteristic: both provide law enforcement access to data without requiring a warrant.

Ring created significant controversy when it became public Amazon had given footage to law enforcement agencies thousands of times, in many cases without the knowledge or consent of the camera owner. Amazon eventually changed some of its policies after public pressure, but the underlying legal framework has not changed.

Flock operates on a similar model. The cameras are typically installed by municipalities or HOAs, but the data infrastructure is controlled by a private company. When police request data, they get it through emergency access provisions, law enforcement portals, or simply because the local agency already has access.

**The absence of a warrant requirement is not a bug in these systems. It is the business model.**

Public records requests (FOIA in the US, FOI in Canada) sometimes reveal what agencies have queried Flock systems, but many agencies treat Flock query logs as internal investigative records and deny access to them.

______

## Debunking "Nothing to Hide"

The "nothing to hide" argument is the most common response to surveillance concerns, and it reflects a genuine misunderstanding of what privacy is for.

**Privacy is not about hiding guilt. It is about preserving autonomy.**

People have legitimate privacy interests in activities which are not criminal: attending political meetings, visiting doctors, going to religious services, speaking to journalists, or simply driving wherever they want without a permanent record being made. The legality of those activities does not give the government a legitimate interest in cataloguing them.

History provides a direct answer to "nothing to hide." Japanese Americans who were interned during World War II were not criminals. Activists surveilled by COINTELPRO were not criminals. People on No-Fly lists who turned out to be there by bureaucratic error were not criminals. The data enabling those abuses was gathered on exactly the same rationale: public safety, threat assessment, efficient law enforcement.

**Surveillance infrastructure built today will be used by whoever holds power tomorrow.** The question of whether the current government is trustworthy is irrelevant. The question is whether you would be comfortable with the most adversarial future government imaginable having access to a permanent record of everywhere you have driven for the last decade.

______

## When License Plate Recognition Gets It Wrong

ALPR systems are not perfectly accurate, and the consequences of an error are serious.

License plate recognition errors fall into several categories:

- **Misread characters**: letters and numbers which look similar under poor lighting or at speed (0/O, 1/I, 8/B, M/N/H)
- **Partial reads**: dirty, obscured, or damaged plates which only partially match
- **Database errors**: plates flagged as stolen which have since been cleared
- **Regional plate collisions**: two states or countries issue the same plate combination, and a hit on a California plate incorrectly flags a vehicle from a state with the same alphanumeric string

Real-world examples document all of these. People have had guns drawn on them during traffic stops because their vehicle was incorrectly matched to a stolen car. People have received toll bills for roads they never drove on. A person driving a powder-blue Hyundai received a toll bill for a Harley-Davidson ridden by someone with a plate differing by two letters.

**The error rate multiplied by the volume of reads produces a significant number of real people who will be incorrectly flagged, stopped, searched, or worse.**

Because most of these queries happen without warrants, there is no judicial check on the accuracy of the underlying data before action is taken.

______

## Security Failures: MFA and Shared Logins

Flock Safety's security practices have been publicly criticized on multiple grounds:

- **No mandatory multi-factor authentication** for law enforcement accounts in many deployments
- **Shared login credentials** among multiple officers at some agencies
- **No automatic session timeouts** in some configurations
- **No alerting when accounts are accessed from unusual locations or times**

These are not minor implementation details. They mean a single compromised credential, obtained through phishing, social engineering, or simple password reuse, would give an attacker access to query a regional Flock network covering millions of license plate reads.

For domestic abuse survivors, stalking victims, or journalists, the existence of a shared, minimally secured database of their vehicle movements is not an abstract concern. It is a direct physical safety risk.

The argument about "the cameras are just public data" ignores the security requirement for the *database layer* aggregating it. Even if every individual photograph is legal to take, the aggregated database requires stronger protection than a shared password.

______

## What Better Design Looks Like

**Technical controls alone are not sufficient, but they are worth considering.**

Several proposals have been discussed for making ALPR systems harder to abuse:

**Data minimization by design**: Instead of storing full license plate images with timestamps and GPS coordinates, the system stores a **cryptographic hash** of the plate paired with approximate location and time. A law enforcement query would confirm whether a specific plate was seen in a specific area in a specific time window, but not retrieve a list of everywhere the plate has been seen. This limits the utility for general fishing expeditions while preserving the ability to answer targeted investigative questions.

**Time-limited retention**: Plates not associated with any open investigation are deleted automatically after 24-72 hours rather than retained for 30 days or more. Most legitimate investigative uses require near-real-time data. Long-term retention creates disproportionate civil liberties risk.

**Warrant requirements with judicial review**: The most important control is legal rather than technical. Requiring a warrant for any query of a named individual's plate history would not prevent emergency uses (exigent circumstance exceptions already exist in law) but would prevent the routine warrantless data mining currently unchecked.

**Audit logging with public transparency**: Every query should be logged, those logs should be auditable by oversight bodies, and aggregate statistics should be publicly reported.

These measures would not make ALPR risk-free, but they would dramatically reduce the potential for routine abuse while preserving the investigative utility which proponents value.

______

## The Debate Doesn't Have to Be All-or-Nothing

The discussion around Flock cameras often collapses into two extreme positions: cameras are essential crime-fighting tools and any criticism helps criminals, or cameras are an unconstitutional surveillance state and must be removed immediately.

Both of these positions are wrong, and the polarization makes it harder to have the conversation which matters.

**The cameras photograph public streets. The data must be governed by law.**

The technology is not going away. The legitimate public safety applications are real. But the current deployment model, in which a private company builds and controls a near-national surveillance database which law enforcement queries without a warrant, is constitutionally suspect and historically dangerous.

The path forward is not to destroy the cameras. It is to require warrants for individual searches, mandate short data retention windows, prohibit open-ended data sharing without case-specific justification, and create enforceable audit and oversight mechanisms.

This is a boring, procedural answer. It does not generate outrage on either side. But it is the only answer taking both public safety and constitutional liberty seriously.

If you want to know when you are near one of these cameras rather than waiting on policy reform, dedicated detection hardware exists today.

{{< stscollective-ad "flockyou" >}}

______

## Related Articles

| Article | What You'll Learn |
|---------|------------------|
| **[Flock Safety Camera Surveillance: Prevalence, Privacy Concerns, and Protection Strategies](/articles/flock-safety-camera-surveillance-prevalence-privacy-protection-2026/)** | Full deep-dive on the Flock network, documented abuse cases, and practical protection steps |
| **[Flock Finder: Map Every Suspected Flock Camera Near You](/articles/flock-finder-alpr-surveillance-mapping-tool/)** | How to use the open-source tool to visualize 40,000+ suspected cameras using WiGLE data |
| **[Flock-You Detection Hardware Guide](/articles/flock-you-detection-project-counter-surveillance-hardware-guide-2026/)** | Build or buy an ESP32-based device to detect Flock cameras in real time |
| **[How to Flash Rayhunter on IMSI Catcher Detection Devices](/articles/how-to-flash-rayhunter-devices-complete-guide/)** | Detect stingrays and IMSI catchers, the cellular equivalent of ALPR tracking |
| **[Rayhunter Device Comparison 2026](/articles/rayhunter-device-comparison-2026-complete-review/)** | Choose the right hardware for a full counter-surveillance toolkit |

______

## References

1. [Carpenter v. United States, 585 U.S. 296 (2018)](https://www.supremecourt.gov/opinions/17pdf/16-402_h315.pdf)
2. [ACLU: Automatic License Plate Readers](https://www.aclu.org/news/by-issue/automatic-license-plate-readers)
3. [Electronic Frontier Foundation: What Is ALPR?](https://www.eff.org/pages/what-alpr)
4. [DeFlock](https://deflock.org/)
5. [DeFlock Interactive Map](https://maps.deflock.org/)
6. [Flock Safety Official Site](https://www.flocksafety.com/)
7. [Security and Privacy Vulnerabilities of In-Car Wireless Networks: A Tire Pressure Monitoring System Case Study](https://www.winlab.rutgers.edu/~gruteser/papers/xu_tpms10.pdf)
8. [FBI Vault: COINTELPRO](https://vault.fbi.gov/cointel-pro)
9. [MuckRock: Flock Safety](https://www.muckrock.com/tags/flock-safety/)
10. [Flock Finder GitHub](https://github.com/simeononsecurity/flock-finder)
11. [WIRED and 404 Media - Hackers Got Inside a Flock Camera](https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/)
12. [Micah Lee - Flock cameras are riddled with security vulnerabilities and hard-coded credentials](https://micahflee.com/flock-cameras-are-riddled-with-security-vulnerabilities-and-hard-coded-credentials/)
13. [Distributed Denial of Secrets - Flock ALPR Camera Filesystem Images](https://ddosecrets.org/article/flock-alpr-camera)
14. [Hackaday - This Week In Security: Flock Cameras Are Old](https://hackaday.com/2026/09/18/this-week-in-security-flock-cameras-are-old-microsoft-patches-patches-and-researchers-attack-ssh/)
15. [WiFi Mothership - Flock Safety ALPR Detection and Device Reference](https://wifimothership.com/flock)
16. [Flock Finder Interactive Map](https://simeononsecurity.github.io/flock-finder/)
