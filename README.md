# Steam Inventory Query

## Deps
```shell
pip 
pip install platformdirs
```

## Fetch Steam profile ID
[Profile ID finder](https://www.steamidfinder.com/)

## Fetch  Steam API Key
[Steam API Key](https://steamcommunity.com/dev/apikey)

## How to run
```shell
set env variable $steam_api_key
python steam_inventory_query/cli.py --profile-id 123123123 --api-key AT328ATTE2888
```
<!-- python steam_inventory_query/cli.py --profile-id $steam_profile_id --api-key $steam_api_key -->

## TODO

- [ ] Add option to list the whole inventory
- [ ] Add option to filter all Heroes inside inventory
- [ ] Add option to filter Ward
- [ ] Add option to filter Courier
- [ ] Refactor display_inventory function
- [ ] Add Github actions to perform system level test
- [ ] Generate page with the inventory periodically