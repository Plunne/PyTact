#!/bin/bash

ble_interface=hci0
ble_mac_adress=FA:28:91:E3:0F:3D
ble_handle=0x001f

stop_frame="0000000000000000000000000000000000000000"

connectToBLE(){

	echo "Connexion starting ..."
	sudo hciconfig $ble_interface up
}

frameToBLE(){

	sudo gatttool -i $ble_interface -b $ble_mac_adress -t random --char-write-req --value=$1 --handle=$ble_handle
}

iterateToBLE(){

	for (( i=0; i<$2; i++ )); do
		frameToBLE $1
	done
}

sendToBLE(){

	if [ $2 -eq '-n' ] ; then
		iterateToBLE $1 $3
	else
		frameToBLE $1
	fi
}

case $1 in
	"-c")
		connectToBLE
		;;
	"-f")
		frameToBLE $2