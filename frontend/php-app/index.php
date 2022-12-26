<html>
    <head>
        <title>PHP App</title>
    </head>

    <body>
        <h1>User List</h1>
        <ul>
            <?php
            $json = file_get_contents('http://backend-service:80/');
            $users = json_decode($json);
            foreach ($users as $user) {
                echo "<li>$user->name</li>";
            }
            ?>
        </ul>
    </body>
</html>