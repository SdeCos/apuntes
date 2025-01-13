<?php
include_once 'GetData.php';
header('Access-Control-Allow-Origin: *');
header("Access-Control-Allow-Headers: X-API-KEY, Origin, X-Requested-With, Content-Type, Accept, Access-Control-Request-Method");
header("Access-Control-Allow-Methods: GET, POST, OPTIONS, PUT, DELETE");
header("Allow: GET, POST, OPTIONS, PUT, DELETE");
$method = $_SERVER['REQUEST_METHOD'];
//print_r('method'.$method);
if ($method == "OPTIONS") {
  die();
}
$api = new GetData();
$data = $api->getAll();
/*	echo "<pre>";
	print_r($data);
	echo "</pre>";
	/*Convertir el arreglo traído de MySql en json */
/*echo json_encode($data);*/
echo "<table>";
echo "<tr>";
echo "<th>ID</th>";
echo "<th>Name</th>";
echo "<th>Department Name</th>";
echo "<th>Address</th>";
echo "<th>Age</th>";
echo "</tr>";
echo "<td>";
for ($i = 0; $i < 26; $i++) {
  echo "<tr>";
  echo "<td>";
  # code...
  print $data[0]['address'][$i]['id'];
  echo "</td>";
  echo "<td>";
  print $data[0]['address'][$i]['name'];
  echo "</td>";
  echo "<td>";
  print $data[0]['address'][$i]['dept_name'];
  echo "</td>";
  echo "<td>";
  print $data[0]['address'][$i]['address'];
  echo "</td>";
  echo "<td>";
  print $data[0]['address'][$i]['age'];
  echo "</td>";
  echo "</tr>";
}
/*Exponer los datos en "php -S localhost:8000 index.php" */
