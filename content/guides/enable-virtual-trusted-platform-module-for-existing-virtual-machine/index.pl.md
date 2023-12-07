---
title: "Zwiększ bezpieczeństwo maszyn wirtualnych dzięki vTPM: Przewodnik krok po kroku"
date: 2023-09-02
toc: true
draft: false
description: "Zwiększ bezpieczeństwo maszyn wirtualnych za pomocą vTPM dzięki naszemu kompleksowemu przewodnikowi krok po kroku, zapewniającemu poświadczenia platformy i obsługę szyfrowania BitLocker."
genre: ["Cyberbezpieczeństwo", "Wirtualizacja", "VMware", "vSphere", "Bezpieczeństwo", "Moduł zaufanej platformy", "vTPM", "Gość OS", "Szyfrowanie", "Atest platformy"]
tags: ["Moduł wirtualnej zaufanej platformy", "Przewodnik vTPM", "Zwiększone bezpieczeństwo maszyn wirtualnych", "Atest platformy", "Szyfrowanie BitLocker", "VMware vSphere", "Bezpieczeństwo wirtualizacji", "Cyberbezpieczeństwo", "Ochrona systemu operacyjnego gościa", "Sprzęt maszyny wirtualnej", "TPM 2.0", "Bezpieczny rozruch", "Operacje kryptograficzne", "Najlepsze praktyki w zakresie bezpieczeństwa maszyn wirtualnych", "vCenter Server", "ESXi Hosts", "Oprogramowanie sprzętowe EFI", "Kluczowy dostawca", "Dokumentacja VMware", "Windows Server", "Windows 7", "System operacyjny Linux", "Bezpieczna konfiguracja maszyny wirtualnej", "Funkcje zabezpieczeń", "Klient vSphere", "Wirtualny chip", "Ochrona danych", "Wykrywanie sabotażu", "Weryfikacja integralności maszyny wirtualnej", "Bezpieczeństwo VMware"]
cover: "/img/cover/enhanced-vm-security.png"
coverAlt: "Symboliczna ilustracja przedstawiająca maszynę wirtualną z błyszczącą blokadą, reprezentującą zwiększone bezpieczeństwo dzięki vTPM."
coverCaption: "Odblokuj bezprecedensowe bezpieczeństwo maszyn wirtualnych!"
---

## Włącz moduł Virtual Trusted Platform Module dla istniejącej maszyny wirtualnej

Virtual Trusted Platform Module (vTPM) to krytyczna funkcja bezpieczeństwa, która zwiększa bezpieczeństwo systemów operacyjnych gościa działających na maszynach wirtualnych. Ten artykuł poprowadzi Cię przez proces dodawania vTPM do istniejącej maszyny wirtualnej w środowisku VMware vSphere, dostarczając instrukcji krok po kroku i ważnych uwag, aby zapewnić płynną implementację.

______

## Wymagania wstępne

Przed przystąpieniem do dodawania modułu vTPM do maszyny wirtualnej należy upewnić się, że spełnione są następujące warunki wstępne:

1. **Środowisko vSphere z dostawcą kluczy:** Upewnij się, że środowisko vSphere jest skonfigurowane dla dostawcy kluczy. Krok ten ma kluczowe znaczenie dla bezpiecznego zarządzania operacjami kryptograficznymi. Zapoznaj się z sekcją [vSphere Security documentation](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-52188148-C579-4F6A-8335-CFBCE0DD2167.html) w celu uzyskania szczegółowych wskazówek.

2. **Obsługiwany system operacyjny gościa:** Sprawdź, czy system operacyjny gościa jest zgodny z vTPM. VMware vTPM jest zgodny z TPM 2.0 i obsługuje systemy Windows Server 2008 i nowsze, Windows 7 i nowsze oraz różne dystrybucje Linuksa.

3. **Status maszyny wirtualnej:** Upewnij się, że maszyna wirtualna, którą chcesz zmodyfikować, jest wyłączona przed przystąpieniem do dodawania vTPM.

4. **Wersja hosta ESXi:** Hosty ESXi w środowisku muszą być uruchomione w wersji ESXi 6.7 lub nowszej dla systemu operacyjnego gościa Windows lub ESXi 7.0 Update 2 dla systemu operacyjnego gościa Linux.

5. **Oprogramowanie sprzętowe EFI:** Maszyna wirtualna musi korzystać z oprogramowania sprzętowego EFI do obsługi vTPM.

6. **Wymagane uprawnienia:** Sprawdź, czy posiadasz niezbędne uprawnienia do operacji kryptograficznych w celu dodania i zarządzania modułem vTPM. Wymagane uprawnienia obejmują:
   - Operacje kryptograficzne.Klonowanie
   - Operacje kryptograficzne.Szyfrowanie
   - Operacje kryptograficzne.Szyfruj nowe
   - Operacje kryptograficzne.migracja
   - Operacje kryptograficzne.Zarejestruj maszynę wirtualną



## Dodanie wirtualnego modułu Trusted Platform Module (vTPM)

Wykonaj poniższe kroki, aby dodać moduł vTPM do istniejącej maszyny wirtualnej:

1. **Połącz się z serwerem vCenter:** Uruchom klienta vSphere i zaloguj się do serwera vCenter.

2. **Otwórz ustawienia maszyny wirtualnej:** Zlokalizuj maszynę wirtualną, którą chcesz zmodyfikować w spisie po lewej stronie klienta vSphere. Kliknij prawym przyciskiem myszy nazwę maszyny wirtualnej i wybierz "Edytuj ustawienia".

3. **Dodaj moduł Trusted Platform Module:** W oknie dialogowym "Edytuj ustawienia" kliknij przycisk "Dodaj nowe urządzenie". Z listy typów urządzeń wybierz "Trusted Platform Module" (vTPM).

4. **Potwierdź wybór:** Kliknij przycisk "OK", aby dodać urządzenie vTPM do maszyny wirtualnej.

5. **Weryfikuj dodanie:** Po pomyślnym dodaniu vTPM, zakładka Podsumowanie maszyny wirtualnej będzie teraz zawierać "Virtual Trusted Platform Module" w panelu VM Hardware.

______

## Korzyści z Virtual Trusted Platform Module (vTPM)

Włączenie modułu vTPM dla maszyny wirtualnej oferuje kilka istotnych korzyści:

1. **Zwiększone bezpieczeństwo:** vTPM tworzy zwirtualizowany układ TPM 2.0 dla maszyny wirtualnej, zapewniając sprzętowe funkcje bezpieczeństwa, takie jak bezpieczny rozruch i operacje kryptograficzne. Wzmacnia to poziom bezpieczeństwa systemu operacyjnego gościa.

2. **Platform Attestation:** vTPM umożliwia maszynie wirtualnej generowanie kryptograficznego pomiaru własnego stanu, umożliwiając poświadczenie platformy. Funkcja ta pomaga zweryfikować integralność maszyny wirtualnej, zapewniając, że nie została ona naruszona.

3. **Obsługa szyfrowania BitLocker:** Jeśli korzystasz z systemu operacyjnego gościa Windows, włączenie vTPM jest warunkiem wstępnym korzystania z szyfrowania BitLocker na dyskach maszyn wirtualnych. Dodaje to dodatkową warstwę ochrony danych.



## Wnioski

Wdrożenie modułu Virtual Trusted Platform Module (vTPM) dla istniejącej maszyny wirtualnej jest kluczowym krokiem w kierunku zwiększenia bezpieczeństwa zwirtualizowanej infrastruktury. Postępując zgodnie z opisaną procedurą i upewniając się, że wszystkie warunki wstępne są spełnione, można włączyć ulepszone funkcje bezpieczeństwa, poświadczenia platformy i obsługę szyfrowania BitLocker dla systemów operacyjnych gościa.

Pamiętaj, aby zapoznać się z oficjalną dokumentacją VMware w celu uzyskania szczegółowych informacji związanych z wersją i konfiguracją vSphere.

______

## Referencje

- [VMware vSphere Security Documentation](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-52188148-C579-4F6A-8335-CFBCE0DD2167.html)
- [VMware vSphere Documentation](https://docs.vmware.com/en/VMware-vSphere/index.html)
- [Trusted Platform Module (TPM) Overview](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vm_admin.doc/GUID-A43B6914-E5F9-4CB1-9277-448AC9C467FB.html)
- [BitLocker Encryption Overview](https://docs.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-overview)

