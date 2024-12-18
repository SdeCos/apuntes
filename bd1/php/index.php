<?php
// Scan the current directory
$files = scandir(__DIR__);

echo "<h1>Directory Listing</h1>";
echo "<ul>";

foreach ($files as $file) {
    if ($file === '.' || $file === '..' || $file === 'index.php' || $file === 'index.html') {
        continue;
    }

    $path = htmlspecialchars($file);
    echo "<li><a href=\"$path\">$path</a></li>";
}

echo "</ul>";
?>
