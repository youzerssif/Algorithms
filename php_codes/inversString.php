<?php


function solution($word){

    return strrev($word);
};

// echo solution("bonjour");

function datasctructure(){
    $cpt = 1;
    $datas = [1,2,3,4,5,6,7,8,9];
    foreach( $datas as $data){
        echo $cpt." Value ".$data;
        $cpt ++;
    };
};

echo datasctructure();