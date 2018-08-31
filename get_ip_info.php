<?php
require dirname(__FILE__).'/ip_search.php';

// header('content-type: application/json');

$ipsearch = new ipSearch();

if(isset($_GET['ip']) && !empty($_GET['ip'])){
    $ip = $_GET['ip'];
    echo $ipsearch->get($ip);
} else {
    echo '条件不足，无法查询，请确保链接请求已携带需要查询的ip参数';
}