<?php
// Fake SQLi simulation endpoint
// No real database — logic puzzle only

$query = $_GET['q'] ?? '';

if ($query === "admin'--") {
    echo "Decoy table accessed.";
} else {
    echo "Invalid query.";
}
?>
