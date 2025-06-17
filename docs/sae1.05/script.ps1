# Script PowerShell pour lancer le programme Python d'analyse

# Spécifiez le chemin du script Python
$scriptPython = "Script-Python.py"

# Vérifiez si Python est installé et accessible
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Output "Python n'est pas installé ou accessible dans PATH."
    exit
}

# Lancer le script Python
try {
    Write-Output "Lancement du script Python..."
    python $scriptPython
} catch {
    Write-Output "Erreur lors du lancement du script Python : $_"
}
