<?php

$redis = new Redis();
$redis->connect('127.0.0.1', 6379);

// 获取ip信息文件
$ips_info = json_decode(file_get_contents(dirname(__DIR__)."/ip_info.json"), TRUE);
// 将ip对应信息记录进哈系表
foreach($ips_info as $key => $ips_info){
    $redis->hset('ipinfo', $key, json_encode($ips_info['data']));
}

// 获取所有中国ip
$china_ips = json_decode(file_get_contents(dirname(__FILE__).'/china_ip.json'), TRUE);
print_r(array_keys($china_ips));

// # 将ip段下的所有ip放进集合，再通过哈系表把集合指向ip段
foreach($china_ips as $ip_field => $ips){
    print_r($ip_field);
    print_r(json_encode($ips));
    // $redis->sadd($ip_field, json_encode($ips));
}
print_r($redis->smembers('223.248.0.0'));

// echo $redis->hget('ipinfo','1.0.8.0:2048');

