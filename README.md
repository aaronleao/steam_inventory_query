# steam_inventory_query
Steam Inventory Query

## Deps
```shell
pip 
pip install platformdirs
```

## Fetch Steam profile ID
[Profile ID finder](https://www.steamidfinder.com/)


## How to run
```shell
set env variable $steam_api_key
python steam_inventory_query/cli.py --profile-id $steam_profile_id --api-key $steam_api_key
```


## TODO

- [ ] Add option to list the whole inventory
- [ ] Add option to filter all Heroes inside inventory
- [ ] Add option to filter Ward
- [ ] Add option to filter Courier
- [ ] Refactor display_inventory function
