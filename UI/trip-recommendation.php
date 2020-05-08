<?php
ini_set('max_input_vars','10000' );
if($_POST!=null && isset($_POST["places"])){
$file = fopen("places.csv","r");
$places=array();
while(!feof($file)){
  $places[]=fgetcsv($file);
}
fclose($file);

$file = fopen("tags.csv","r");
$tagDictionary=array();
$i=0;
while(!feof($file)){
  $tagValue=fgetcsv($file);
  if($i++==0){
	  continue;
  }
  if(is_array($tagValue)){
	$tagDictionary[str_replace(" ","-",$tagValue[1])]=$tagValue;
  }
}
fclose($file);
$placeTagRatings=$_POST['places'];
$file = fopen("place_tag_weights.csv", "a");
foreach($placeTagRatings as $placeTagRating){
	$tags=$placeTagRating["tags"];
	foreach($tags as $tag){
		//IF TAG ID REQUIRED THEN USE THE FOLLOWING LINE
		//$line=array($placeTagRating["id"],$tagDictionary[$tag["tag"]][0],$tag["weight"]);
		//IF TAG NAME REQUIRED THEN USE THE FOLLOWING LINE
		$line=array($placeTagRating["id"],$tag["tag"],$tag["weight"]);
		fputcsv($file, $line); 
	}
}
fclose($file);
return;	
}

$file = fopen("places_tag.csv","r");
$placeTags=array();
while(!feof($file)){
  $placeTags[]=fgetcsv($file);
}
fclose($file);

$i=0;
echo "<html>
<head>
<title>Tag Weights</title>
</head>
<body>";
$pageNumber=$_GET["page_number"];
$perPage=20;
$numberOfPages=ceil(sizeof($placeTags)/$perPage);

echo "<center>
			".($pageNumber>1?"<a href='trip-recommendation.php?page_number=".($pageNumber-1)."'>Prev</a>":"")."
			<h4>Page ".$pageNumber." of ".$numberOfPages."</h4>
			".($pageNumber<$numberOfPages?"<a href='trip-recommendation.php?page_number=".($pageNumber+1)."'>Next</a>":"")."
		</center>";
$skip=($pageNumber-1)*$perPage;
foreach($placeTags as $placeTag){
	if($i==0){
		echo "<table style='border:1px solid black;'>
			<thead style='border:1px solid black;'>
				<tr>
				<th style='border:1px solid black;'>Place Id</th>
				<th style='border:1px solid black;'>Place Name</th>";
				for($j=1;$j<=21;$j++){
					echo "<th style='border:1px solid black;'>Tag $j</th>";
				}
			echo "</tr>
			</thead>
			<tbody style='border:1px solid black;'>";
			$i++;
		continue;
	}
	if($i<=$skip){
		$i++;
		continue;
	}
	if(!is_array($placeTag)){
		break;
	}
	echo "<tr>
				<td style='border:1px solid black;'>".$placeTag[0]."</td>
				<td style='border:1px solid black;'>".$placeTag[1]."</td>";
				for($j=1;$j<=21;$j++){
					echo "<td style='border:1px solid black;'>".$placeTag[$j+1].
					(($placeTag[$j+1]!="")?"<input data-place-id='".$placeTag[0]."' data-tag='".$placeTag[$j+1]."' type='number' min='1' max='10' value='5'/>":"")."
					</td>";
				}
			echo "<tr>";
	if($i%$perPage==0){
		break;
	}
	$i++;
}
echo "</tbody>
		</table><br/><br/>
		<center><button onclick='submitForm()'>Save</button></center>";
echo "</body>
<script src= 
'https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js'> 
    </script> 
	<script>
		function submitForm(){
			var weights=$('input');
			var places=[]
			for(var i=0;i<weights.length;i++){
				var weight=weights[i];
				var placeId=$(weight).attr('data-place-id');
				var tag=$(weight).attr('data-tag');
				if(places[placeId]==undefined){
					places[placeId]=[];
				}
				places[placeId].push({tag:tag,weight:$(weight).val()});
			}
			var postPlaces=[];
			for(var placeId in places){
				if(places[placeId]!=undefined){
					postPlaces.push({id:placeId,tags:places[placeId]});
				}
			}
			$.post( 'trip-recommendation.php',{places:postPlaces}, function( data ) {
				alert('Data saved successfully');
				console.log(data);
			});
		}
	</script>";

?>