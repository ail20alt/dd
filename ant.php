<?php
session_start();
$host = 'localhost';
$db = 'social_media';
$user = 'root';
$pass = '';

try {
    $pdo = new PDO("mysql:host=$host;dbname=$db", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Could not connect to the database: " . $e->getMessage());
}

// User Registration
if (isset($_POST['register'])) {
    $username = $_POST['username'];
    $password = password_hash($_POST['password'], PASSWORD_DEFAULT);
    
    $stmt = $pdo->prepare("INSERT INTO users (username, password) VALUES (?, ?)");
    $stmt->execute([$username, $password]);
    echo "Registration successful!";
}

// User Login
if (isset($_POST['login'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];
    
    $stmt = $pdo->prepare("SELECT * FROM users WHERE username = ?");
    $stmt->execute([$username]);
    $user = $stmt->fetch();
    
    if ($user && password_verify($password, $user['password'])) {
        $_SESSION['user_id'] = $user['id'];
        echo "Login successful!";
    } else {
        echo "Invalid username or password.";
    }
}

// Posting a Message
if (isset($_POST['post'])) {
    $message = $_POST['message'];
    $user_id = $_SESSION['user_id'];
    
    $stmt = $pdo->prepare("INSERT INTO posts (user_id, message) VALUES (?, ?)");
    $stmt->execute([$user_id, $message]);
    echo "Message posted!";
}

// Fetching Posts
$stmt = $pdo->query("SELECT users.username, posts.message FROM posts JOIN users ON posts.user_id = users.id ORDER BY posts.created_at DESC");
$posts = $stmt->fetchAll();

foreach ($posts as $post) {
    echo "<p><strong>{$post['username']}:</strong> {$post['message']}</p>";
}
?>


$username=$_post['uname'];
$pass=$_post['pass'];
echo"your name is :<br>.$username . "<br> your pass is :<br>".$pass; 

