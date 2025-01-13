<?php
// Scan the current directory
$files = scandir(__DIR__);

echo "<h1>Directory Listing</h1>";
echo "<ul>";

// Loop through the files
foreach ($files as $file) {
    // Exclude special directories and index files
    if ($file === '.' || $file === '..' || $file === 'index.php' || $file === 'index.html') {
        continue;
    }

    // Create a clickable link for each file/directory
    $path = htmlspecialchars($file);
    echo "<li><a href=\"$path\">$path</a></li>";
}

echo "</ul>";
?>
