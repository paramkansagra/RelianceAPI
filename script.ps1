$localGroups = Get-LocalGroup
$hostName = $env:COMPUTERNAME

$dataList = New-Object -TypeName 'System.Collections.ArrayList'

for($i=0 ; $i -lt $localGroups.Count ; $i++){
    $groupMember = Get-LocalGroupMember -Group $localGroups[$i]
    if($groupMember.Count -gt 0){
        for($j=0 ; $j -lt $groupMember.Count ; $j++){
            $hash = @{ "group_name" = $localGroups[$i].Name ; "user_name" = $groupMember[$j].ToString() ; "host_name" = $hostName}
            $dataList += $hash
        }
    }
}

$time = Get-CimInstance -ClassName Win32_OperatingSystem | Select LastBootUpTime

$upTime = $time.LastBootUpTime.GetDateTimeFormats("o")[0]

$finalJsonData = @{ "groups" = $dataList ; "host_name" = $hostName ; "uptime" = $upTime}


$finalJson = $finalJsonData | ConvertTo-Json

$finalJson