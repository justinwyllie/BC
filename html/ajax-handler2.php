<?php


$data = json_decode(file_get_contents('php://input'), true);


$data["errors"] = implode("-",$data["errors"]);

$email_data = "";

$email_data = "name: " . $data["name"];

if ($data["tea"] != "Select..")
{
    $email_data = $email_data . "tea: " . $data["tea"];
}

if ($data["coffee"] != "Select..")
{
    $email_data = $email_data . "coffee " . $data["coffee"];
}





$res = mail('justinwyllie@hotmail.co.uk', "Menu Order", $email_data);
echo json_encode(array('success' => $res));