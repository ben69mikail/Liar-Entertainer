# Fix-Skript fuer alle kinderzauberer city pages
# Ausfuehren in PowerShell: cd C:\Users\ben_m\Claude\Liar-Entertainer-fresh && .\fix_kinderzauberer.ps1

$repoPath = "C:\Users\ben_m\Claude\Liar-Entertainer-fresh"
$pagesPath = "$repoPath\src\pages\kinderzauberer"

$cities = @(
    "kinderzauberer-in-bochum",
    "kinderzauberer-in-bottrop",
    "kinderzauberer-in-datteln",
    "kinderzauberer-in-dinslaken",
    "kinderzauberer-in-dorsten",
    "kinderzauberer-in-dortmund",
    "kinderzauberer-in-duesseldorf",
    "kinderzauberer-in-duisburg",
    "kinderzauberer-in-essen",
    "kinderzauberer-in-gelsenkirchen",
    "kinderzauberer-in-haltern",
    "kinderzauberer-in-herne",
    "kinderzauberer-in-herten",
    "kinderzauberer-in-marl",
    "kinderzauberer-in-moers",
    "kinderzauberer-in-muelheim",
    "kinderzauberer-in-oberhausen",
    "kinderzauberer-in-recklinghausen"
)

$fixedCount = 0
$skippedCount = 0

foreach ($city in $cities) {
    $filePath = "$pagesPath\$city\index.astro"

    if (-not (Test-Path $filePath)) {
        Write-Host "SKIP (nicht gefunden): $city" -ForegroundColor Yellow
        $skippedCount++
        continue
    }

    $content = Get-Content $filePath -Raw -Encoding UTF8
    $original = $content

    # FIX 1: karteImg Import ersetzen -> Clown-Aktion Bild
    $content = $content -replace "import karteImg from '\.\.\/\.\.\/\.\.\/assets\/images\/home\/clown-zauberer-gladbeck-karte\.jpg';", "import aktionImg from '../../../assets/images/clown/clown-bei-clownshow.jpg';"

    # FIX 2: _galleryImgAsset Import ersetzen -> Kinder-lachen Bild
    $content = $content -replace "import _galleryImgAsset from '\.\.\/\.\.\/\.\.\/assets\/images\/galerie\/fotogalerie-clown-zauberer-1\.jpg';", "import _galleryImgAsset from '../../../assets/images/clown/kinderzauberer-kindergarten-essen.jpg';"

    # FIX 3: Astro Image-Komponente: karteImg -> aktionImg
    $content = $content -replace '\{karteImg\}', '{aktionImg}'

    # FIX 4: CTA-Buttons von white-card zu echten roten Buttons
    $content = $content -replace 'class="bg-white rounded-lg px-5 py-3 shadow-sm text-\[#d7393e\] hover:underline font-medium text-sm card-hover"', 'class="bg-[#d7393e] hover:bg-[#b62e32] text-white rounded-lg px-5 py-3 font-bold text-sm transition-colors"'

    if ($content -ne $original) {
        [System.IO.File]::WriteAllText($filePath, $content, [System.Text.UTF8Encoding]::new($false))
        Write-Host "FIXED: $city" -ForegroundColor Green
        $fixedCount++
    } else {
        Write-Host "UNCHANGED: $city" -ForegroundColor Gray
        $skippedCount++
    }
}

Write-Host ""
Write-Host "=== FERTIG ===" -ForegroundColor Cyan
Write-Host "Gefixt: $fixedCount" -ForegroundColor Green
Write-Host "Unveraendert: $skippedCount" -ForegroundColor Gray
Write-Host ""
Write-Host "Jetzt deployen:" -ForegroundColor Yellow
Write-Host "  cd C:\Users\ben_m\Claude\Liar-Entertainer-fresh" -ForegroundColor White
Write-Host "  git add ." -ForegroundColor White
Write-Host "  git commit -m ""fix: replace karte image + fix CTA buttons on all kinderzauberer pages""" -ForegroundColor White
Write-Host "  git push" -ForegroundColor White
