local DataStoreService = game:GetService('DataStoreService')
local HiveCoinsData = DataStoreService:GetDataStore('PlayerDataHiveCoins')
local FoodChipsData = DataStoreService:GetDataStore('PlayerDataChips')
local Players = game:GetService("Players")
--Assign name/variables for the datastore
--Add "playerDataWood" EXAMPLE ONLY << This DataStoreService already exists

local function PlayerJoin(player)
	local leaderstats = Instance.new("Folder")
	leaderstats.Name = 'leaderstats'
	leaderstats.Parent = player
	local Item_Inventory_Holder = player:WaitForChild('Item_Inventory')
	wait(3)
	local parent_of_leaderstats_test = leaderstats.Parent.Parent.Name
	print(parent_of_leaderstats_test)
	

	
			local coins  = Instance.new('IntValue')
			coins.Name = 'HiveCoins'
			coins.Parent = leaderstats

	
			local coinsstringvalue  = Instance.new('TextLabel')
			coinsstringvalue.Name = 'Coinsstring'
			coinsstringvalue.Parent = leaderstats
	
			local playerUserId = 'Player_'..player.UserId
			local data = HiveCoinsData:GetAsync(playerUserId)
			
			local playerUserId_1 = 'Player_'..player.UserId
			local chipsdata = FoodChipsData:GetAsync(playerUserId_1)
	
	--Check Data if existing on the upper part of this script
		if data then
		local selectcorevalue = coinsstringvalue.Text
				coins.Value = data
				coinsstringvalue.Text = data
		else
			coins.Value = 0
		end
		if chipsdata then
			Item_Inventory_Holder.Chips.Value = chipsdata
		else
			Item_Inventory_Holder.Chips.Value = 0
		end
end

local function PlayerQuit(player)
	local success, err = pcall(function()
		--Data below is being saved if it's called in here, saving data using same variables as the first part of the script
		local playerUserId = 'Player_'..player.UserId
		HiveCoinsData:SetAsync(playerUserId, player.leaderstats.HiveCoins.Value)
		
		local playerUserId_1 = 'Player_'..player.UserId
		FoodChipsData:SetAsync(playerUserId_1, player.Item_Inventory.Chips.Value)
	end)
	if not success then
		warn('Data not being saved')
	end
end

game.Players.PlayerAdded:Connect(PlayerJoin)
game.Players.PlayerRemoving:Connect(PlayerQuit)