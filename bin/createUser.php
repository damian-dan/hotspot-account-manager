<?php
    $start = microtime(true);
    include_once 'vendor/autoload.php';
    echo "1";
    $client = new \PEAR2\Net\RouterOS\Client('192.168.15.1', 'admin', '1');
    echo "2";
    $addRequest = new \PEAR2\Net\RouterOS\Request('/ip hotspot user add profile=ProfilInexistent');
    $addRequest
        ->setArgument('name', "aaa")
        ->setArgument('password', "123456");//$argv[1])

    $errors = $client->sendSync($addRequest)->getAllOfType(\PEAR2\Net\RouterOS\Response::TYPE_ERROR);
    if (count($errors)) {
        echo "baaaaaaad";
        var_dump($errors ); echo "<br />";
        //Unable to add user. Handle errors here.
    }else{
    echo "good" . "<br />";
    var_dump($errors ); echo "<br />";
    }
    echo (microtime(true) - $start);
