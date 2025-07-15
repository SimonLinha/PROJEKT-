from typing import List, Dict, Optional

# Globální seznam úkolů
ukoly: List[Dict[str, str]] = []

def pridat_ukol(nazev: str, popis: str) -> bool:
    """
    Přidá nový úkol do seznamu, pokud název a popis nejsou prázdné.

    Args:
        nazev (str): Název úkolu.
        popis (str): Popis úkolu.

    Returns:
        bool: True, pokud byl úkol přidán, False pokud byl vstup neplatný.
    """
    nazev = nazev.strip()
    popis = popis.strip()
    if not nazev or not popis:
        return False
    ukol = {"nazev": nazev, "popis": popis}
    ukoly.append(ukol)
    return True

def zobraz_ukoly() -> None:
    """
    Vypíše všechny uložené úkoly, pokud existují.
    """
    if not ukoly:
        print("Žádné úkoly nejsou zadány.")
    else:
        print("Seznam úkolů:")
        for i, ukol in enumerate(ukoly, start=1):
            print(f"{i}. {ukol['nazev']} – {ukol['popis']}")

def odstranit_ukol(cislo: int) -> bool:
    """
    Odstraní úkol podle pořadového čísla.

    Args:
        cislo (int): Pořadové číslo úkolu k odstranění (1-based index).

    Returns:
        bool: True pokud byl úkol úspěšně odstraněn, False pokud číslo bylo neplatné.
    """
    if 1 <= cislo <= len(ukoly):
        odstraneny = ukoly.pop(cislo - 1)
        print(f"Úkol '{odstraneny['nazev']}' byl odstraněn.")
        return True
    else:
        return False

def hlavni_menu() -> None:
    """
    Hlavní menu programu, které zajišťuje interakci s uživatelem.
    """
    while True:
        print("\nSprávce úkolů - Hlavní menu")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")

        try:
            moznost = int(input("Vyberte možnost (1-4): "))
        except ValueError:
            print("Zadejte platné číslo.")
            continue

        if moznost == 1:
            # Vstup uživatele zde, jádro funkce bez inputu
            while True:
                nazev = input("Zadejte název úkolu: ").strip()
                popis = input("Zadejte popis úkolu: ").strip()
                if pridat_ukol(nazev, popis):
                    print("Úkol byl úspěšně přidán.")
                    break
                else:
                    print("Název i popis musí být vyplněny. Zkuste to znovu.")

        elif moznost == 2:
            zobraz_ukoly()

        elif moznost == 3:
            if not ukoly:
                print("Seznam úkolů je prázdný.")
                continue
            zobraz_ukoly()
            try:
                cislo = int(input("Zadejte číslo úkolu k odstranění: "))
                if not odstranit_ukol(cislo):
                    print("Neplatné číslo úkolu.")
            except ValueError:
                print("Zadejte platné číslo.")

        elif moznost == 4:
            print("Ukončuji program...")
            break

        else:
            print("Neplatná volba. Zkuste to znovu.")

if __name__ == "__main__":
    hlavni_menu()