param(
    [Parameter(Mandatory = $true)]
    [string]$SdkExecutable
)
$ErrorActionPreference = 'Stop'
$projectPath = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..')).Path
$sdkPath = (Resolve-Path -LiteralPath $SdkExecutable).Path
if (-not (Test-Path -LiteralPath (Join-Path $projectPath 'game/options.rpy'))) {
    throw 'Project options.rpy is missing.'
}
if (-not (Test-Path -LiteralPath $sdkPath -PathType Leaf)) {
    throw 'RenPy executable is missing.'
}
$desktopPath = [Environment]::GetFolderPath('Desktop')
$shortcutPath = Join-Path $desktopPath '风从旧世来（最新版）.lnk'
$shell = New-Object -ComObject WScript.Shell
$shortcut = $shell.CreateShortcut($shortcutPath)
$shortcut.TargetPath = $sdkPath
$shortcut.Arguments = '"' + $projectPath + '" run'
$shortcut.WorkingDirectory = $projectPath
$shortcut.Description = '风从旧世来 - 当前开发工程（最新版）'
$shortcut.IconLocation = $sdkPath + ',0'
$shortcut.Save()
$verified = $shell.CreateShortcut($shortcutPath)
if ($verified.TargetPath -ne $sdkPath -or $verified.Arguments -ne ('"' + $projectPath + '" run') -or $verified.WorkingDirectory -ne $projectPath) {
    throw 'Shortcut verification failed.'
}
[pscustomobject]@{ Shortcut = $shortcutPath; Target = $verified.TargetPath; Arguments = $verified.Arguments; WorkingDirectory = $verified.WorkingDirectory }
