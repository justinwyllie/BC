<?php


$data = json_decode(file_get_contents('php://input'), true);


$data["errors"] = implode("-",$data["errors"]);

$email_data = <<<EOT
name: {$data["name"]}
drink: {$data["drink"]}
food: {$data["food"]}
EOT;

$res = mail('justinwyllie@hotmail.co.uk', "Menu Order", $email_data);
echo json_encode(array('success' => $res));