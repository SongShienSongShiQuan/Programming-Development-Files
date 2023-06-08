local DataStoreService = game:GetService('DataStoreService')
local HiveCoinsData = DataStoreService:GetDataStore('PlayerDataHiveCoins')
local FoodChipsData = DataStoreService:GetDataStore('PlayerDataChips')
local Key101Data = DataStoreService:GetDataStore('PlayerDataKey_101')
local Players = game:GetService("Players")

--Assign name/variables for the datastore
--Add "playerDataWood" EXAMPLE ONLY << This DataStoreService already exists

local function PlayerJoin(player)
	
	local leaderstats = Instance.new("Folder")
	leaderstats.Name = 'leaderstats'
	leaderstats.Parent = player
	wait(3)
	local Item_Inventory_Holder = player:WaitForChild('Item_Inventory')

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
			
			local playerUserId = 'Player_'..player.UserId
			local chipsdata = FoodChipsData:GetAsync(playerUserId)
	
			local playerUserId = 'Player_'..player.UserId
			local key101 = Key101Data:GetAsync(playerUserId)
			
	
	--Check Data if existing on the upper part of this script
		if data then
		local selectcorevalue = coinsstringvalue.Text
			coins.Value = data
			coinsstringvalue.Text = data	
			player.PlayerGui.Inventory_GUI.ScrollingFrame.HC_INV_STR.Text = data
		else
			coins.Value = 0
		end
		if chipsdata then
		local Item_1_GUI = player.PlayerGui.Inventory_GUI.ScrollingFrame.Item_1
		local Item_2_GUI = player.PlayerGui.Inventory_GUI.ScrollingFrame.Item_2
		local Item_3_GUI = player.PlayerGui.Inventory_GUI.ScrollingFrame.Item_3
		local Item_4_GUI = player.PlayerGui.Inventory_GUI.ScrollingFrame.Item_4
		local Item_5_GUI = player.PlayerGui.Inventory_GUI.ScrollingFrame.Item_5
		local Item_6_GUI = player.PlayerGui.Inventory_GUI.ScrollingFrame.Item_6
		local Item_7_GUI = player.PlayerGui.Inventory_GUI.ScrollingFrame.Item_7
		local Item_8_GUI = player.PlayerGui.Inventory_GUI.ScrollingFrame.Item_8
		local Item_9_GUI = player.PlayerGui.Inventory_GUI.ScrollingFrame.Item_9
		local Item_10_GUI = player.PlayerGui.Inventory_GUI.ScrollingFrame.Item_10
			Item_Inventory_Holder.Chips.Value = chipsdata
			if Item_1_GUI.Item_Frame_Used.Text == "false" then
				Item_1_GUI.Item_Name.Text = "Chips"
				Item_1_GUI.Item_Count.Text = chipsdata
				Item_1_GUI.Item_Frame_Used.Text = "true"
				Item_1_GUI.Item_Name.None.Name = "Chips"
			elseif Item_2_GUI.Item_Frame_Used.Text == "false" then
				Item_2_GUI.Item_Name.Text = "Chips"
				Item_2_GUI.Item_Count.Text = chipsdata
				Item_2_GUI.Item_Frame_Used.Text = "true"
				Item_2_GUI.Item_Name.None.Name = "Chips"
			elseif Item_3_GUI.Item_Frame_Used.Text == "false" then
				Item_3_GUI.Item_Name.Text = "Chips"
				Item_3_GUI.Item_Count.Text = chipsdata
				Item_3_GUI.Item_Frame_Used.Text = "true"
				Item_3_GUI.Item_Name.None.Name = "Chips"
			elseif Item_4_GUI.Item_Frame_Used.Text == "false" then
				Item_4_GUI.Item_Name.Text = "Chips"
				Item_4_GUI.Item_Count.Text = chipsdata
				Item_4_GUI.Item_Frame_Used.Text = "true"
				Item_4_GUI.Item_Name.None.Name = "Chips"
			elseif Item_5_GUI.Item_Frame_Used.Text == "false" then
				Item_5_GUI.Item_Name.Text = "Chips"
				Item_5_GUI.Item_Count.Text = chipsdata
				Item_5_GUI.Item_Frame_Used.Text = "true"
				Item_5_GUI.Item_Name.None.Name = "Chips"
			elseif Item_6_GUI.Item_Frame_Used.Text == "false" then
				Item_6_GUI.Item_Name.Text = "Chips"
				Item_6_GUI.Item_Count.Text = chipsdata
				Item_6_GUI.Item_Frame_Used.Text = "true"
				Item_6_GUI.Item_Name.None.Name = "Chips"
			elseif Item_7_GUI.Item_Frame_Used.Text == "false" then
				Item_7_GUI.Item_Name.Text = "Chips"
				Item_7_GUI.Item_Count.Text = chipsdata
				Item_7_GUI.Item_Frame_Used.Text = "true"
				Item_7_GUI.Item_Name.None.Name = "Chips"
			elseif Item_8_GUI.Item_Frame_Used.Text == "false" then
				Item_8_GUI.Item_Name.Text = "Chips"
				Item_8_GUI.Item_Count.Text = chipsdata
				Item_8_GUI.Item_Frame_Used.Text = "true"
				Item_8_GUI.Item_Name.None.Name = "Chips"
			elseif Item_9_GUI.Item_Frame_Used.Text == "false" then
				Item_9_GUI.Item_Name.Text = "Chips"
				Item_9_GUI.Item_Count.Text = chipsdata
				Item_9_GUI.Item_Frame_Used.Text = "true"
				Item_9_GUI.Item_Name.None.Name = "Chips"
			elseif Item_10_GUI.Item_Frame_Used.Text == "false" then
				Item_10_GUI.Item_Name.Text = "Chips"
				Item_10_GUI.Item_Count.Text = chipsdata
				Item_10_GUI.Item_Frame_Used.Text = "true"
				Item_10_GUI.Item_Name.None.Name = "Chips"
		else
			Item_Inventory_Holder.Chips.Value = 0
		end
		if key101 then
		local Item_1_GUI = player.PlayerGui.Inventory_GUI.ScrollingFrame.Item_1
		local Item_2_GUI = player.PlayerGui.Inventory_GUI.ScrollingFrame.Item_2
		local Item_3_GUI = player.PlayerGui.Inventory_GUI.ScrollingFrame.Item_3
		local Item_4_GUI = player.PlayerGui.Inventory_GUI.ScrollingFrame.Item_4
		local Item_5_GUI = player.PlayerGui.Inventory_GUI.ScrollingFrame.Item_5
		local Item_6_GUI = player.PlayerGui.Inventory_GUI.ScrollingFrame.Item_6
		local Item_7_GUI = player.PlayerGui.Inventory_GUI.ScrollingFrame.Item_7
		local Item_8_GUI = player.PlayerGui.Inventory_GUI.ScrollingFrame.Item_8
		local Item_9_GUI = player.PlayerGui.Inventory_GUI.ScrollingFrame.Item_9
		local Item_10_GUI = player.PlayerGui.Inventory_GUI.ScrollingFrame.Item_10
			Item_Inventory_Holder.Key_101.Value = key101
			if Item_1_GUI.Item_Frame_Used.Text == "false" then
				Item_1_GUI.Item_Name.Text = "Key_101"
				Item_1_GUI.Item_Count.Text = key101
				Item_1_GUI.Item_Frame_Used.Text = "true"
				Item_1_GUI.Item_Name.None.Name = "Key_101"
			elseif Item_2_GUI.Item_Frame_Used.Text == "false" then
				Item_2_GUI.Item_Name.Text = "Key_101"
				Item_2_GUI.Item_Count.Text = key101
				Item_2_GUI.Item_Frame_Used.Text = "true"
				Item_2_GUI.Item_Name.None.Name = "Key_101"
			elseif Item_3_GUI.Item_Frame_Used.Text == "false" then
				Item_3_GUI.Item_Name.Text = "Key_101"
				Item_3_GUI.Item_Count.Text = key101
				Item_3_GUI.Item_Frame_Used.Text = "true"
				Item_3_GUI.Item_Name.None.Name = "Key_101"
			elseif Item_4_GUI.Item_Frame_Used.Text == "false" then
				Item_4_GUI.Item_Name.Text = "Key_101"
				Item_4_GUI.Item_Count.Text = key101
				Item_4_GUI.Item_Frame_Used.Text = "true"
				Item_4_GUI.Item_Name.None.Name = "Key_101"
			elseif Item_5_GUI.Item_Frame_Used.Text == "false" then
				Item_5_GUI.Item_Name.Text = "Key_101"
				Item_5_GUI.Item_Count.Text = key101
				Item_5_GUI.Item_Frame_Used.Text = "true"
				Item_5_GUI.Item_Name.None.Name = "Key_101"
			elseif Item_6_GUI.Item_Frame_Used.Text == "false" then
				Item_6_GUI.Item_Name.Text = "Key_101"
				Item_6_GUI.Item_Count.Text = key101
				Item_6_GUI.Item_Frame_Used.Text = "true"
				Item_6_GUI.Item_Name.None.Name = "Key_101"
			elseif Item_7_GUI.Item_Frame_Used.Text == "false" then
				Item_7_GUI.Item_Name.Text = "Key_101"
				Item_7_GUI.Item_Count.Text = key101
				Item_7_GUI.Item_Frame_Used.Text = "true"
				Item_7_GUI.Item_Name.None.Name = "Key_101"
			elseif Item_8_GUI.Item_Frame_Used.Text == "false" then
				Item_8_GUI.Item_Name.Text = "Key_101"
				Item_8_GUI.Item_Count.Text = key101
				Item_8_GUI.Item_Frame_Used.Text = "true"
				Item_8_GUI.Item_Name.None.Name = "Key_101"
			elseif Item_9_GUI.Item_Frame_Used.Text == "false" then
				Item_9_GUI.Item_Name.Text = "Key_101"
				Item_9_GUI.Item_Count.Text = key101
				Item_9_GUI.Item_Frame_Used.Text = "true"
				Item_9_GUI.Item_Name.None.Name = "Key_101"
			elseif Item_10_GUI.Item_Frame_Used.Text == "false" then
				Item_10_GUI.Item_Name.Text = "Key_101"
				Item_10_GUI.Item_Count.Text = key101
				Item_10_GUI.Item_Frame_Used.Text = "true"
				Item_10_GUI.Item_Name.None.Name = "Key_101"
			else
				Item_Inventory_Holder.Chips.Value = 0
			end
		end
	end
end

local function PlayerQuit(player)
	local success, err = pcall(function()
		--Data below is being saved if it's called in here, saving data using same variables as the first part of the script
		local playerUserId = 'Player_'..player.UserId
		HiveCoinsData:SetAsync(playerUserId, player.leaderstats.HiveCoins.Value)
		
		local playerUserId_1 = 'Player_'..player.UserId
		FoodChipsData:SetAsync(playerUserId_1, player.Item_Inventory.Chips.Value)
		
		local playerUserId_1 = 'Player_'..player.UserId
		Key101Data:SetAsync(playerUserId_1, player.Item_Inventory.Key_101.Value)
	end)
	if not success then
		warn('Data not being saved')
	end
end

game.Players.PlayerAdded:Connect(PlayerJoin)
game.Players.PlayerRemoving:Connect(PlayerQuit)