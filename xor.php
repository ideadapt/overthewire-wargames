<?php 
function xor_encrypt($a, $b) {
    $key = $a;
    $text = $b;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}
$a=base64_decode('ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw');
$b=json_encode(Array("showpassword"=>"no","bgcolor"=>"#ffffff"));
$keyxor=xor_encrypt($a, $b);
echo "\nxored key ".$keyxor;
$key='qw8J';
echo "\nkey ".$key;
$b=json_encode(Array("showpassword"=>"yes","bgcolor"=>"#ffffff"));
$cookieraw=xor_encrypt($key, $b);
echo "\ncookie raw ".$cookieraw;
echo "\ncookie base64 ".base64_encode($cookieraw);
