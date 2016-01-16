#!/usr/bin/env php
<?php
    if (!$argv[1]) || !$argv[2]))
        exit();
    
    $start = microtime(true);
    include_once __DIR__ . '/../vendor/autoload.php';
    $client = new \PEAR2\Net\RouterOS\Client('192.168.15.120', 'admin', 'pcnet1010');
    $addRequest = new \PEAR2\Net\RouterOS\Request('/ip hotspot user add profile=uprof1 server=server1');
    $addRequest
        ->setArgument('name', $argv[1]))
        ->setArgument('password', $argv[2]));

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
