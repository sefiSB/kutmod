import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------------------------------------------------
# 1. Adatok betöltése
# ----------------------------------------------------------------------
excel_file_name = "tests2.xlsx"

try:
    # Betöltés a tests2.xlsx-ből
    df = pd.read_excel(excel_file_name)
    print(f"Sikeresen betöltve a '{excel_file_name}' fájl.")
except FileNotFoundError:
    print(f"Hiba: A '{excel_file_name}' fájl nem található. Győződjön meg róla, hogy a megfelelő könyvtárban van.")
    exit()

# ----------------------------------------------------------------------
# 2. Adatok előkészítése
# ----------------------------------------------------------------------
# Kiszűrjük azokat a sorokat, ahol a 'bugcount' nulla (0).
df_filtered = df[df['bugcount'] > 0]

# Kinyerjük a különböző, nem nulla hibaszámokat (bugcount értékeket)
bugcounts = sorted(df_filtered['bugcount'].unique())

# ----------------------------------------------------------------------
# 3. Szórástáblák készítése a bugcount-ok szerint
# ----------------------------------------------------------------------

# Minden egyedi (nem nulla) bugcount értékre készítünk egy külön ábrát
for count in bugcounts:
    # Kiszűrjük az aktuális bugcount-hoz tartozó adatokat
    df_subset = df_filtered[df_filtered['bugcount'] == count]

    # Ábra létrehozása
    plt.figure(figsize=(10, 7))

    # Szórástábla elkészítése seaborn segítségével
    sns.scatterplot(
        x='thinking time',
        y='patch accuracy',
        hue='llm name',
        data=df_subset,
        s=100,              # A körök mérete
        style='llm name'    # Különböző jelölő formák
    )

    # Címek és feliratok beállítása
    plt.title(f'LLM teljesítmény (Bugcount: {count}): Pontosság vs. Idő', fontsize=16)
    plt.xlabel('Gondolkodási idő (másodperc)', fontsize=12)
    plt.ylabel('Javítási pontosság (%)', fontsize=12)

    # Jelmagyarázat (Legend) elhelyezése
    # A 'bugcount' szerint változhat az LLM-ek száma, de érdemes fixen tartani a helyet
    plt.legend(title='LLM neve', loc='upper left', bbox_to_anchor=(1.05, 1))

    # Rács hozzáadása
    plt.grid(True, linestyle='--', alpha=0.6)

    # Az ábra szegélyeinek finomhangolása
    plt.tight_layout()

    # Az ábra megjelenítése
    plt.show()

print("\nAz ábrák elkészültek a nem nulla 'bugcount' értékekre.")