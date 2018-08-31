<?php

class ipSearch{
    private $redis;
    private $china_ips;

    function __construct(){
        $this->redis = new Redis();
        $this->redis->connect('127.0.0.1', 6379);
        $this->china_ips = json_decode(file_get_contents(dirname(__FILE__).'/china_ip_field.json'));
    }
    // 根据ip获取数据
    function get($ip){
        // 将ip的第四位转换成0
        $ip = substr($ip, 0, strripos($ip, '.')).'.0';
        foreach($this->china_ips as $cip){
            // 获取该ip域的所有ip地址并转成php数组
            $members = json_decode($this->redis->smembers($cip)[0]);
            if(in_array($ip, $members)){
                return $this->redis->hget('ipinfo', $cip);
                break;
            }
        }
        // 如果没找到，去淘宝ip网获取并返回结果
        return $this->search($ip);
    }

    function search($ip){
        $info = file_get_contents('http://ip.taobao.com/service/getIpInfo.php?ip='.$ip);
        if(!empty($info)){
            return $info;
        } else {
            return '暂无查询结果';
        }
    }
}
