# Commit #2 — ALT-Attribute + H2-Typo + Header Nav Titles
# Commit message: chore(seo): [autopilot 2026-05-29] ueber-mich ALT-fixes + kinderzauberer H2-typo + header-nav-titles
# Files: 3 Dateien
# SHA ueber-mich: 5aa1cfb99eebdcc3bac89174cce7c128f9bb8c09
# SHA kinderzauberer: cbd5f20668e9833affed8dc840c5db840f5ae232
# SHA Header: 955fd352a993792658047c6aefd86fbef3ae9373

---

## ÄNDERUNG 1: src/pages/ueber-mich/index.astro
### 3 ALT-Attribute ersetzen

ALT 1 (alt suchen/ersetzen):
ALT: alt="Über mich als Clown"
NEU: alt="Clown Zauberer LIAR Michael Prescler in Clown-Kostüm"

ALT 2:
ALT: alt="Über mich als Clown Zauberer"
NEU: alt="Michaël Prescler als Clown Zauberer LIAR bei Auftritt in NRW"

ALT 3:
ALT: alt="Wohnort Clown Zauberer LIAR"
NEU: alt="Standort Clown Zauberer LIAR – Gladbeck NRW Karte"

---

## ÄNDERUNG 2: src/pages/kinderzauberer/index.astro
### H2 Typo fix

SUCHEN:
WISSENWERTES über den ZAuberer für KINDER

ERSETZEN:
WISSENSWERTES über den Zauberer für Kinder

(Das vollständige H2-Tag:)
ALT:
<h2 class="font-bold text-[#1f2025] text-2xl sm:text-3xl text-center mb-10">
  WISSENWERTES über den ZAuberer für KINDER
</h2>

NEU:
<h2 class="font-bold text-[#1f2025] text-2xl sm:text-3xl text-center mb-10">
  WISSENSWERTES über den Zauberer für Kinder
</h2>

---

## ÄNDERUNG 3: src/components/Header.astro
### Nav title-Attribute ergänzen

Im menuItems-Array die label-Einträge mit title-Attributen versehen.
Da das menuItems-Array im Frontmatter (---) liegt, müssen title-Felder im Array ergänzt
UND in der Render-Logik auf <a title={item.title}> umgestellt werden.

### menuItems Array — NEU (vollständig ersetzen):

```javascript
const menuItems = [
  {
    label: 'Clown',
    href: '/clown/clownshow/',
    title: 'Clown buchen NRW',
    children: [
      { label: 'Clownshow', href: '/clown/clownshow/' },
      { label: 'Walk Act', href: '/clown/walk-act/' },
      { label: 'Ballonmodellage', href: '/clown/ballonmodellage/' },
      { label: 'Glitzer Tattoo', href: '/clown/glitzer-tattoo/' },
    ],
  },
  {
    label: 'Zauberer',
    href: '/zauberer/',
    title: 'Zauberer buchen NRW',
    children: [
      { label: 'Bühnen Zauberer', href: '/zauberer/buehnen-zauberer/' },
      { label: 'Tisch Zauberer', href: '/zauberer/tisch-zauberer/' },
    ],
  },
  {
    label: 'Kinderzauberer',
    href: '/kinderzauberer/',
    title: 'Kinderzauberer NRW',
  },
  {
    label: 'Kindergeburtstag',
    href: '/kindergeburtstag/',
    title: 'Kindergeburtstag Zauberer NRW',
  },
  {
    label: 'Preise',
    href: '/preise/',
    title: 'Preise Clown Zauberer NRW',
  },
  {
    label: 'Zaubershow',
    href: '/zauberer/zaubershow/',
    title: 'Zaubershow buchen NRW',
    children: [
      { label: 'Kindergarten – Kita', href: '/zauberer/zaubershow/kindergarten-kita/' },
      { label: 'Schule', href: '/zauberer/zaubershow/schule/' },
      { label: 'Straßen – Sommer -Fest', href: '/zauberer/zaubershow/strassen-sommer-fest/' },
      { label: 'Karneval', href: '/clown/karneval/' },
    ],
  },
  { label: 'Galerie', href: '/galerie/', title: 'Galerie LIAR Clown Zauberer' },
  { label: 'Blog', href: '/blog/' },
  { label: 'Pantomime', href: 'https://pantomime.liar-entertainer.com', external: true },
  { label: 'Kontakt', href: '/kontakt/', title: 'Clown Zauberer LIAR kontaktieren' },
];
```

### Desktop-Nav <a> Tags — title-Attribut ergänzen:

Für Dropdown-Items (mit children):
```html
<a
  href={item.href}
  title={item.title}
  class="nav-link-wp flex items-center gap-1 px-4 h-full text-[#1f2025] hover:text-[#ffb546] text-[15px] font-medium"
>
```

Für externe Links:
```html
<a
  href={item.href}
  target="_blank"
  rel="noopener noreferrer"
  title={item.title}
  class="nav-link-wp flex items-center px-4 h-14 text-[#1f2025] hover:text-[#ffb546] text-[15px] font-medium"
>
```

Für normale Links (kein Dropdown, nicht extern):
```html
<a
  href={item.href}
  title={item.title}
  class="nav-link-wp flex items-center px-4 h-14 text-[#1f2025] hover:text-[#ffb546] text-[15px] font-medium"
>
```

---

## COMMIT BEFEHL (GitHub API):

```
mcp__plugin_everything-claude-code_github__push_files:
  owner: ben69mikail
  repo: liar-entertainer-blog
  branch: main
  message: "chore(seo): [autopilot 2026-05-29] ueber-mich ALT-fixes + kinderzauberer H2-typo + header-nav-titles"
  files:
    - path: src/pages/ueber-mich/index.astro   (vollständige Datei mit 3 ALT-Änderungen)
    - path: src/pages/kinderzauberer/index.astro (vollständige Datei mit H2-Fix)
    - path: src/components/Header.astro         (vollständige Datei mit title-Attributen)
```
