---
title: "Îmbunătățiți securitatea mașinilor virtuale cu vTPM: Ghid pas cu pas"
date: 2023-09-02
toc: true
draft: false
description: "Îmbunătățiți securitatea mașinilor virtuale utilizând vTPM cu ajutorul ghidului nostru complet pas cu pas, care oferă atestare a platformei și suport pentru criptarea BitLocker."
genre: ["Securitatea cibernetică", "Virtualizare", "VMware", "vSphere", "Securitate", "Modulul de platformă de încredere", "vTPM", "OS invitat", "Criptare", "Atestarea platformei"]
tags: ["Modulul de platformă virtuală de încredere", "Ghid vTPM", "Securitate îmbunătățită pentru VM", "Atestarea platformei", "Criptarea BitLocker", "VMware vSphere", "Securitatea virtualizării", "Securitatea cibernetică", "Protecția sistemului de operare invitat", "Hardware VM", "TPM 2.0", "Boot securizat", "Operațiuni criptografice", "Cele mai bune practici de securitate VM", "Server vCenter", "Gazde ESXi", "Firmware EFI", "Furnizor de chei", "Documentația VMware", "Windows Server", "Windows 7", "Linux OS", "Configurarea securizată a VM", "Caracteristici de securitate", "Client vSphere", "Cip virtual", "Protecția datelor", "Detectarea sabotajului", "Verificarea integrității VM", "Securitatea VMware"]
cover: "/img/cover/enhanced-vm-security.png"
coverAlt: "O ilustrație simbolică care arată o mașină virtuală cu un sistem de blocare strălucitoare, reprezentând securitatea sporită prin vTPM."
coverCaption: "Deblocați o securitate fără precedent pentru VM!"
---

## Activați modulul virtual Trusted Platform Module pentru o mașină virtuală existentă

Virtual Trusted Platform Module (vTPM) este o caracteristică de securitate esențială care îmbunătățește securitatea sistemelor de operare invitate care rulează pe mașini virtuale. Acest articol vă va ghida prin procesul de adăugare a unui vTPM la o mașină virtuală existentă într-un mediu VMware vSphere, oferind instrucțiuni pas cu pas și considerații importante pentru a asigura o implementare fără probleme.

______

## Condiții prealabile

Înainte de a continua cu adăugarea unui vTPM la mașina virtuală, asigurați-vă că îndepliniți următoarele condiții prealabile:

1. **Mediu vSphere cu furnizor de chei:** Asigurați-vă că mediul vSphere este configurat pentru un furnizor de chei. Acest pas este crucial pentru gestionarea în siguranță a operațiunilor criptografice. Consultați pagina [vSphere Security documentation](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-52188148-C579-4F6A-8335-CFBCE0DD2167.html) pentru îndrumări detaliate.

2. **Sistemul de operare invitat compatibil:** Verificați dacă sistemul de operare invitat este compatibil cu vTPM. VMware vTPM este compatibil cu TPM 2.0 și acceptă Windows Server 2008 și versiunile ulterioare, Windows 7 și versiunile ulterioare și diverse distribuții Linux.

3. **Starea mașinii virtuale:** Asigurați-vă că mașina virtuală pe care doriți să o modificați este oprită înainte de a proceda la adăugarea vTPM.

4. **ESXi Host Version:** Gazdele ESXi din mediul dumneavoastră trebuie să ruleze fie ESXi 6.7 sau o versiune ulterioară pentru sistemul de operare invitat Windows, fie ESXi 7.0 Update 2 pentru sistemul de operare invitat Linux.

5. **Firmware EFI:** Mașina virtuală trebuie să utilizeze firmware EFI pentru suportul vTPM.

6. **Privilegii necesare:** Verificați dacă aveți privilegiile necesare pentru operațiile criptografice pentru a adăuga și gestiona vTPM. Privilegiile necesare includ:
   - Operațiuni criptografice.Clonare
   - Operațiuni criptografice.Encrypt
   - Cryptographic operations.Encrypt new (Operațiuni criptografice.Criptare nouă)
   - Operațiuni criptografice.Migrare
   - Operațiuni criptografice.Register VM

______
{{< inarticle-dark >}}
______

## Adăugarea modulului virtual Trusted Platform Module (vTPM)

Urmați acești pași pentru a adăuga un vTPM la mașina virtuală existentă:

1. **Conectați-vă la vCenter Server:** Lansați vSphere Client și conectați-vă la vCenter Server.

2. **Open Virtual Machine Settings (Deschideți Virtual Machine Settings): ** Localizați mașina virtuală pe care doriți să o modificați în inventarul din partea stângă a vSphere Client. Faceți clic dreapta pe numele mașinii virtuale și selectați "Edit Settings".

3. **Adaugați Trusted Platform Module:** În caseta de dialog "Edit Settings", faceți clic pe butonul "Add New Device". Din lista de tipuri de dispozitive, selectați "Trusted Platform Module" (vTPM).

4. **Confirmă selecția:** Faceți clic pe butonul "OK" pentru a adăuga dispozitivul vTPM la mașina virtuală.

5. **Verificarea adăugării:** După adăugarea cu succes a dispozitivului vTPM, fila Summary a mașinii virtuale va include acum "Virtual Trusted Platform Module" în panoul VM Hardware.

______

## Beneficiile modulului virtual Trusted Platform Module (vTPM)

Activarea unui vTPM pentru mașina dvs. virtuală oferă mai multe beneficii semnificative:

1. **Securitate sporită:** vTPM creează un cip TPM 2.0 virtualizat pentru mașina virtuală, oferind caracteristici de securitate bazate pe hardware, cum ar fi pornirea securizată și operațiunile criptografice. Acest lucru consolidează poziția de securitate a sistemului de operare invitat.

2. **Atestarea platformei:** vTPM permite mașinii virtuale să genereze o măsurătoare criptografică a propriei stări, permițând atestarea platformei. Această caracteristică ajută la verificarea integrității mașinii virtuale, asigurându-se că nu a fost modificată.

3. **Suport pentru criptare BitLocker:** Dacă rulați un sistem de operare invitat Windows, activarea vTPM este o condiție prealabilă pentru utilizarea criptării BitLocker pe discurile mașinii virtuale. Acest lucru adaugă un nivel suplimentar de protecție a datelor.

______
{{< inarticle-dark >}}
______

## Concluzie

Implementarea unui modul virtual Trusted Platform Module (vTPM) pentru o mașină virtuală existentă este un pas crucial pentru consolidarea securității infrastructurii virtualizate. Urmând procedura descrisă și asigurându-vă că sunt îndeplinite toate condițiile prealabile, puteți activa caracteristici de securitate îmbunătățite, atestarea platformei și suportul de criptare BitLocker pentru sistemele de operare invitate.

Nu uitați să consultați documentația oficială VMware pentru detalii specifice legate de versiunea și configurația vSphere.

______

## Referințe

- [VMware vSphere Security Documentation](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-52188148-C579-4F6A-8335-CFBCE0DD2167.html)
- [VMware vSphere Documentation](https://docs.vmware.com/en/VMware-vSphere/index.html)
- [Trusted Platform Module (TPM) Overview](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vm_admin.doc/GUID-A43B6914-E5F9-4CB1-9277-448AC9C467FB.html)
- [BitLocker Encryption Overview](https://docs.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-overview)

