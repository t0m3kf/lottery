#/bin/bash
epoch_nr=$(curl -s https://api.koios.rest/api/v0/tip?select=epoch_no | jq -r '.[0].epoch_no')

curl -s "https://api.koios.rest/api/v0/pool_delegators?_pool_bech32=pool19xyfanyp28j6j07dxgwdjp0wur6seqmyyu64qgzstzl7s47pvpj&select=stake_address,amount,active_epoch_no&order=active_epoch_no" > epoch_$epoch_nr.json 
