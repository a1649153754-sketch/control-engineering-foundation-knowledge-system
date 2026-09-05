[CmdletBinding()]
param(
    [string]$Python = "python",
    [string]$Zensical = "zensical"
)

$ErrorActionPreference = "Stop"
$RepoName = "control-engineering-foundation-knowledge-system"
$ExpectedRepo = "a1649153754-sketch/$RepoName"

# Compatibility entry point: prepare a reviewable branch push; never upload.
function Invoke-Checked {
    param([string]$Command, [string[]]$Arguments)
    & $Command @Arguments
    if ($LASTEXITCODE -ne 0) {
        throw "$Command failed (exit $LASTEXITCODE): $($Arguments -join ' ')"
    }
}

foreach ($command in @("git", $Python, $Zensical)) {
    if (-not (Get-Command $command -ErrorAction SilentlyContinue)) {
        throw "Required command unavailable: $command"
    }
}
if (-not (Test-Path -LiteralPath (Join-Path $PSScriptRoot ".git"))) {
    throw "Use an existing Git checkout. Review an unpacked candidate in a separate branch first."
}

Push-Location $PSScriptRoot
try {
    $gitRoot = (Invoke-Checked "git" @("rev-parse", "--show-toplevel")).Trim()
    if ((Resolve-Path -LiteralPath $gitRoot).Path -ne (Resolve-Path -LiteralPath $PSScriptRoot).Path) {
        throw "The script must be in the intended repository root."
    }
    $branch = (Invoke-Checked "git" @("branch", "--show-current")).Trim()
    if (-not $branch -or $branch -in @("main", "master")) {
        throw "Use a dedicated review branch; main/master and detached HEAD are not accepted."
    }
    $head = (Invoke-Checked "git" @("rev-parse", "HEAD")).Trim()
    $version = (Get-Content -LiteralPath "VERSION" -Raw).Trim()
    if (@(Invoke-Checked "git" @("status", "--porcelain", "--untracked-files=all")).Count) {
        throw "Review and commit local changes before preparing a push."
    }

    $allowedRemote = "^(https://github\.com/|git@github\.com:)" + [regex]::Escape($ExpectedRepo) + "(\.git)?$"
    foreach ($remoteArgs in @(
        @("remote", "get-url", "--all", "origin"),
        @("remote", "get-url", "--push", "--all", "origin")
    )) {
        $urls = @(Invoke-Checked "git" $remoteArgs)
        if ($urls.Count -ne 1 -or $urls[0] -notmatch $allowedRemote) {
            throw "origin must have exactly one fetch/push URL for $ExpectedRepo. No URL was changed."
        }
    }

    Invoke-Checked "git" @("fetch", "origin", "refs/heads/main:refs/remotes/origin/main")
    $base = (Invoke-Checked "git" @("rev-parse", "origin/main")).Trim()
    $counts = (Invoke-Checked "git" @("rev-list", "--left-right", "--count", "origin/main...HEAD")).Trim() -split "\s+"
    if ($counts.Count -ne 2 -or [int]$counts[0] -ne 0 -or [int]$counts[1] -eq 0) {
        throw "The branch must contain origin/main plus at least one reviewed commit. Reconcile changes manually."
    }

    Invoke-Checked $Python @("scripts/validate_project.py")
    Invoke-Checked $Python @("scripts/build_bundle.py")
    Invoke-Checked $Zensical @("build", "--clean", "--strict")
    Invoke-Checked $Python @("scripts/validate_project.py")
    Invoke-Checked "git" @("diff", "--check", "origin/main...HEAD")
    if (@(Invoke-Checked "git" @("status", "--porcelain", "--untracked-files=all")).Count) {
        throw "The build changed the worktree. Review generated files before preparing a push."
    }
    if ((Invoke-Checked "git" @("rev-parse", "HEAD")).Trim() -ne $head -or
        (Invoke-Checked "git" @("branch", "--show-current")).Trim() -ne $branch) {
        throw "HEAD or the current branch changed during validation. Run preparation again."
    }

    Write-Host "Preparation passed: $ExpectedRepo v$version" -ForegroundColor Green
    Write-Host "Base: $base"
    Write-Host "Branch: $branch"
    Write-Host "Reviewed HEAD: $head"
    Write-Host "After explicit approval, push this commit and open a pull request targeting main:"
    Write-Host "git push --no-follow-tags --recurse-submodules=no origin ${head}:refs/heads/$branch"
    Write-Host "No commits, branches, repository settings, or remote content were changed; only fetch and local builds ran."
}
finally {
    Pop-Location
}
