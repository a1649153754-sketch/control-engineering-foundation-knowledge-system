$ErrorActionPreference = "Stop"
$RepoName = "control-engineering-foundation-knowledge-system"

Write-Host "Control Engineering Knowledge System - GitHub Sync" -ForegroundColor Cyan

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    throw "Git is not installed. Install Git first."
}
if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
    throw "GitHub CLI (gh) is not installed. Install it from the official GitHub CLI page."
}

# Browser-based official authorization; never paste a token into this script.
gh auth status 2>$null
if ($LASTEXITCODE -ne 0) {
    gh auth login --web --git-protocol https
}

$Owner = (gh api user --jq .login).Trim()
$Version = (Get-Content (Join-Path $PSScriptRoot "VERSION") -Raw).Trim()
$Repo = "$Owner/$RepoName"

Write-Host "Account: $Owner"
Write-Host "Repository: $Repo"
Write-Host "Local version: v$Version"

$RepoExists = $true
gh repo view $Repo 2>$null | Out-Null
if ($LASTEXITCODE -ne 0) { $RepoExists = $false }

if (-not $RepoExists) {
    $Visibility = Read-Host "Repository does not exist. Enter 1 for public or 2 for private"
    if ($Visibility -eq "1") { $Flag = "--public" }
    elseif ($Visibility -eq "2") { $Flag = "--private" }
    else { throw "Invalid choice." }
}

$Confirm = Read-Host "Type YES to validate, commit, and push v$Version"
if ($Confirm -ne "YES") { throw "Cancelled." }

Set-Location $PSScriptRoot

if (-not (Test-Path ".git")) {
    git init -b main
}

git config user.name $Owner
git config user.email "$Owner@users.noreply.github.com"

$RemoteUrl = "https://github.com/$Repo.git"

if ($RepoExists) {
    $ExistingRemote = git remote get-url origin 2>$null
    if (-not $ExistingRemote) {
        git remote add origin $RemoteUrl
    } elseif ($ExistingRemote -ne $RemoteUrl) {
        git remote set-url origin $RemoteUrl
    }

    # Attach the unpacked project to the existing history without overwriting
    # the working tree. Missing remote files become deletions; local v1.1 files
    # become additions or updates.
    git fetch origin main
    git reset origin/main
} else {
    # Let `gh repo create --remote origin` create the remote after the first commit.
    $ExistingRemote = git remote get-url origin 2>$null
    if ($ExistingRemote) { git remote remove origin }
}

python scripts/validate_project.py
python scripts/build_bundle.py
python scripts/validate_project.py

git add -A
$status = git status --porcelain
if ($status) {
    git commit -m "feat: publish control engineering foundation knowledge system v$Version"
} else {
    Write-Host "No file changes to commit."
}

if (-not $RepoExists) {
    gh repo create $Repo $Flag --source . --remote origin --push
} else {
    git branch -M main
    git push -u origin main
}

Write-Host "Sync complete: https://github.com/$Repo" -ForegroundColor Green
Write-Host "Pages: https://$Owner.github.io/$RepoName/" -ForegroundColor Green
