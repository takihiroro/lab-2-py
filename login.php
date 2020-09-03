<?php 
	$host = 'db';
	$user = 'devel';
	$password = 'bazinga';
	$db = 'proj';
	$conn = new mysqli($host,$user,$password,$db);
	if ($conn->connect_error) {
		echo 'connection failed: ' . $conn->connect_error;
	}
	if (isset($_POST["user"]) && isset($_POST["password"]) && $_POST["user"] && $_POST["password"]) {
		$user = $conn->real_escape_string($_POST["user"]);
		$password = $conn->real_escape_string($_POST["password"]);
		$query = "SELECT * FROM creds WHERE username='$user' AND password='$password'";
		$result = $conn->query($query);
		echo "before check<br>";
		if ($result->num_rows > 0) {
			echo "<h2>YAY! pass: $password</h2>";
		}
		else {
			echo '<p>Wrong creds..<br> login: ' . $user . '; pass: ' . $password . '</p><a href="/index.php">Proceed back to index page</a>';
		}
	}
?>
