# Gym Rank App 💪

## 🧠 O aplikaci

Gym Rank App je mobilní aplikace která slouží k zapisování tréninků a sledování progresu jednotlivých svalových skupin.

Hlavní myšlenka aplikace je jednoduchá:

👉 každý sval má svůj **level (rank)**
👉 cvičením a zapisováním výkonů získáváš **XP (experience points)**
👉 čím víc trénuješ, tím vyšší level máš

Aplikace je navržená tak, aby byla:

* rychlá na použití v gymu
* přehledná
* motivující

---

## ⚙️ Jak aplikace funguje

1. Vybereš svalovou skupinu (např. biceps)
2. Zobrazí se seznam cviků pro daný sval
3. Vybereš cvik
4. Zadáš:

   * váhu (kg)
   * počet opakování
5. Aplikace:

   * uloží trénink
   * přidá XP
   * spočítá level

---

## 🎯 XP a level systém

XP se počítá podle vzorce:

```
XP = váha × opakování × multiplier
```

* každý cvik má vlastní **multiplier (obtížnost)**
* lehčí cviky (menší váhy) mají vyšší multiplier
* těžké cviky mají nižší multiplier

👉 systém je tak férovější mezi různými typy cviků

Level se zvyšuje každých:

```
1000 XP = +1 level
```

---

## 📊 Funkce aplikace

* 📱 Mobilní UI (optimalizované pro telefon)
* 💪 Svalové skupiny s vlastním levelem
* 🧠 XP systém s multipliery
* 🏋️‍♂️ Více než 10 cviků pro každý sval
* 📝 Ukládání tréninků
* 📈 Zobrazení:

  * posledního výkonu
  * PR (personal record)
* 💾 Ukládání dat do JSON souboru
* 🎨 Barevné rozlišení svalů
* 🔄 Scrollovatelný obsah

---

## 🛠️ Použité věci

* 🐍 Python
* 📱 Flet (frontend + UI)
* 💾 JSON (lokální ukládání dat)
* 🧠 ChatGPT – pomoc s návrhem logiky, UX a kódu

---
## 🔥 Budoucí možné plány

* ⭐ Oblíbené cviky (favorites)
* 📊 Statistiky a grafy
* 🎯 Denní cíle
* 🔥 „NEW PR“ efekty a bonus XP
* 👤 Uživatelský profil

---

