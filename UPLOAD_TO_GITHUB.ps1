$ErrorActionPreference = "Stop"
$RepoName = "control-engineering-foundation-knowledge-system"

Write-Host "Control Engineering Knowledge System - GitHub Upload" -ForegroundColor Cyan

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    throw "Git is not installed. Install Git first."
}
if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
    throw "GitHub CLI (gh) is not installed. Install it from the official GitHub CLI page."
}

gh auth status 2>$null
if ($LASTEXITCODE -ne 0) {
    gh auth login --web --git-protocol https
}

$Owner = (gh api user --jq .login).Trim()
Write-Host "Account: $Owner"
Write-Host "Repository: $Owner/$RepoName"

$Visibility = Read-Host "Enter 1 for public or 2 for private"
if ($Visibility -eq "1") { $Flag = "--public" }
elseif ($Visibility -eq "2") { $Flag = "--private" }
else { throw "Invalid choice." }

$Confirm = Read-Host "Type YES to initialize and upload"
if ($Confirm -ne "YES") { throw "Cancelled." }

Set-Location $PSScriptRoot

if (-not (Test-Path ".git")) {
    git init -b main
}
git config user.name $Owner
git config user.email "$Owner@users.noreply.github.com"
git add -A

$status = git status --porcelain
if ($status) {
    git commit -m "feat: publish control engineering foundation knowledge system v1.0.0"
}

gh repo view "$Owner/$RepoName" 2>$null
if ($LASTEXITCODE -ne 0) {
    gh repo create "$Owner/$RepoName" $Flag --source . --remote origin --push
} else {
    if (-not (git remote get-url origin 2>$null)) {
        git remote add origin "https://github.com/$Owner/$RepoName.git"
    }
    git branch -M main
    git push -u origin main
}

Write-Host "Upload complete: https://github.com/$Owner/$RepoName" -ForegroundColor Green
