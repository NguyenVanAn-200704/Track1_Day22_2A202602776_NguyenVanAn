$docPath = "d:\NguyenVanAn\2026_Vin_AI_ThucChien\TongHop_LAB\Track1_Day22_2A202602776_NguyenVanAn\NguyenVanAn_Day22_onepager.docx"
$pdfPath = "d:\NguyenVanAn\2026_Vin_AI_ThucChien\TongHop_LAB\Track1_Day22_2A202602776_NguyenVanAn\NguyenVanAn_Day22_onepager.pdf"

try {
    $word = New-Object -ComObject Word.Application
    $word.Visible = $false
    $doc = $word.Documents.Open($docPath)
    # wdFormatPDF = 17
    $doc.SaveAs([ref]$pdfPath, [ref]17)
    $doc.Close()
    $word.Quit()
    Write-Host "Successfully converted docx to pdf via Word COM: $pdfPath"
} catch {
    Write-Host "Word COM failed: $_"
}
