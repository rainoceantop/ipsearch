<?php
ini_set('memory_limit', '256M');

$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
# 清除缓存
$redis->flushall();

// 获取ip信息文件
$ips_info = json_decode(file_get_contents(dirname(__FILE__)."/ip_info.json"), TRUE);
// 将ip对应信息记录进哈系表
foreach($ips_info as $key => $ips_info){
    $redis->hset('ipinfo', $key, json_encode($ips_info, JSON_UNESCAPED_UNICODE));
}

// 获取所有中国ip
$china_ips = json_decode(file_get_contents(dirname(__FILE__).'/china_ip.json'), TRUE);

// 将ip段下的所有ip放进集合
foreach($china_ips as $ip_field => $ips){
    $redis->sadd($ip_field, json_encode($ips));
}
// echo $redis->hget('ipinfo','1.0.8.0');

